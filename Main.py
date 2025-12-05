import os
import json
import librosa
import numpy as np
import speech_recognition as sr
import google.generativeai as genai
import soundfile as sf

os.environ["GOOGLE_API_KEY"] = "AIzaSyAn66efYRXNxmKt0Ild1iVWApu5U-27Z0k" 
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-2.5-pro')

def transcribe_audio_free(audio_path):
    print("🎤 Transcribing audio...")
    recognizer = sr.Recognizer()
    
    try:
        y, sr_rate = librosa.load(audio_path)
        sf.write('temp_pitch.wav', y, sr_rate)
    except Exception as e:
        return f"Error loading audio file: {e}"
    
    with sr.AudioFile('temp_pitch.wav') as source:
        audio_data = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            return "Could not understand audio."
        except sr.RequestError:
            return "Speech API unavailable."

def analyze_audio_signal(audio_path):
    print("🔊 Analyzing voice energy...")
    y, sr = librosa.load(audio_path)
    
    rms = librosa.feature.rms(y=y)
    energy = int(np.mean(rms) * 1000)
    
    non_silent = librosa.effects.split(y, top_db=20)
    speech_len = sum([(e - s) for s, e in non_silent]) / sr
    total_len = librosa.get_duration(y=y, sr=sr)
    
    if total_len == 0: return {"energy": 0, "silence": 0}
    silence_pct = int(((total_len - speech_len) / total_len) * 100)
    
    return {"energy": energy, "silence": silence_pct}

def run_shark_tank(audio_path):
    try:
        audio_stats = analyze_audio_signal(audio_path)
        transcript = transcribe_audio_free(audio_path)
    except Exception as e:
        print(f"Error processing inputs: {e}")
        return

    print(f"\n📝 TRANSCRIPT: \"{transcript}\"")
    print(f"📊 METRICS: Energy={audio_stats['energy']}/100 | Silence={audio_stats['silence']}%\n")
    
    prompt = f"""
    Act as the Shark Tank India panel evaluating a startup pitch.
    
    PITCH DATA:
    - Transcript: "{transcript}"
    - Audio Stats: Energy {audio_stats['energy']}/100 (Low energy < 30 is bad), Silence {audio_stats['silence']}% (High silence > 15% is nervous)
    
    INSTRUCTIONS:
    1. **Ashneer Grover:** If 'Silence' > 15%, roast them for being nervous ("Doglapan"). If no 'Profit' mentioned in transcript, say "Bhai tu dhanda band kar de."
    2. **Namita Thapar:** If the idea is confusing or purely technical, say "Isme meri expertise nahi hai".
    3. **Aman Gupta:** If Energy > 50, say "Killer Energy!". Focus on branding/packaging.
    
    Reply in Hinglish (Hindi+English).
    
    At the very end of your response, you MUST add this section explicitly:
    ----------------------------------------
    **FINAL RECOMMENDATION:** [Choose one: INVEST / NOT INVEST / NEED MORE INFO]
    ----------------------------------------
    """

    print("🧠 The Sharks are deciding...")
    try:
        response = model.generate_content(prompt)
        print("\n" + "="*40)
        print(response.text)
        print("="*40 + "\n")
    except Exception as e:
        print(f"AI Error: {e}")
    
    if os.path.exists("temp_pitch.wav"):
        os.remove("temp_pitch.wav")

if __name__ == "__main__":
    file_name = "pitch3.wav"
    
    if os.path.exists(file_name):
        run_shark_tank(file_name)
    else:
        print(f"❌ Error: '{file_name}' file not found. Please make sure the audio file is in this folder.")
