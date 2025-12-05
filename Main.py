import os
import json
import librosa
import numpy as np
import speech_recognition as sr
import google.generativeai as genai
import soundfile as sf

# --- 1. CONFIGURATION ---
# 🔴 IMPORTANT: Paste your key inside the quotes below
os.environ["GOOGLE_API_KEY"] = "AIzaSyAn66efYRXNxmKt0Ild1iVWApu5U-27Z0k" 
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Use Gemini Pro for smarter logic
model = genai.GenerativeModel('gemini-2.5-pro')

# --- 2. SPEECH TRANSCRIPTION (FREE) ---
def transcribe_audio_free(audio_path):
    print("🎤 Transcribing audio...")
    recognizer = sr.Recognizer()
    
    # Load and convert audio to WAV for processing
    y, sr_rate = librosa.load(audio_path)
    sf.write('temp_pitch.wav', y, sr_rate)
    
    with sr.AudioFile('temp_pitch.wav') as source:
        audio_data = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            return "Could not understand audio."
        except sr.RequestError:
            return "Speech API unavailable."

# --- 3. AUDIO SIGNAL ANALYSIS ---
def analyze_audio_signal(audio_path):
    print("🔊 Analyzing voice energy...")
    y, sr = librosa.load(audio_path)
    
    # Calculate Energy
    rms = librosa.feature.rms(y=y)
    energy = int(np.mean(rms) * 1000)
    
    # Calculate Silence
    non_silent = librosa.effects.split(y, top_db=20)
    speech_len = sum([(e - s) for s, e in non_silent]) / sr
    total_len = librosa.get_duration(y=y, sr=sr)
    
    if total_len == 0: return {"energy": 0, "silence": 0}
    silence_pct = int(((total_len - speech_len) / total_len) * 100)
    
    return {"energy": energy, "silence": silence_pct}

# --- 4. THE SHARK TANK PANEL ---
def run_shark_tank(audio_path):
    # Get the data
    try:
        audio_stats = analyze_audio_signal(audio_path)
        transcript = transcribe_audio_free(audio_path)
    except Exception as e:
        print(f"Error: {e}")
        return

    print(f"\n📝 TRANSCRIPT: \"{transcript}\"")
    print(f"📊 METRICS: Energy={audio_stats['energy']}/100 | Silence={audio_stats['silence']}%\n")
    
    # The Prompt for Gemini
    prompt = f"""
    Act as the Shark Tank India panel.
    
    PITCH DATA:
    - Transcript: "{transcript}"
    - Audio Stats: Energy {audio_stats['energy']}/100, Silence {audio_stats['silence']}%
    
    INSTRUCTIONS:
    1. **Ashneer Grover:** If 'Silence' > 15%, roast them for being nervous ("Doglapan"). If no 'Profit' mentioned, say "Bhai tu dhanda band kar de."
    2. **Namita Thapar:** If the idea is confusing, say "Isme meri expertise nahi hai".
    3. **Aman Gupta:** If Energy > 50, say "Killer Energy!". Focus on branding.
    
    Reply in Hinglish (Hindi+English).
    """

    print("🧠 The Sharks are deciding...")
    response = model.generate_content(prompt)
    print("\n" + "="*40)
    print(response.text)
    print("="*40 + "\n")
    
    if os.path.exists("temp_pitch.wav"):
        os.remove("temp_pitch.wav")

# --- EXECUTION ---
if __name__ == "__main__":
    # Ensure you have 'pitch.mp3' in the same folder
    if os.path.exists("pitch3.wav"):
        run_shark_tank("pitch3.wav")
    else:
        print("❌ Error: 'pitch3.wav' file not found in this folder.")