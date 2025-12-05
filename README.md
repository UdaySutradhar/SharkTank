🦈 Shark Tank India Pitch Analyzer

A multimodal AI tool that analyzes startup pitches using Audio Signal Processing and Large Language Models (LLMs). The system evaluates vocal delivery (energy, confidence) and business content to simulate feedback from specific Shark Tank India judges.

🚀 Features

Audio Signal Processing:

Calculates Energy Levels (Josh Meter).

Detects Silence & Hesitation (Nervousness Index).

Hinglish Transcription: Uses Google's Speech Recognition to transcribe mixed Hindi-English pitches.

AI Shark Panel (Gemini 2.5 Pro):

Ashneer Grover: Roasts low margins and nervousness ("Doglapan").

Namita Thapar: Opts out if the pitch is confusing ("Expertise nahi hai").

Aman Gupta: Focuses on energy and branding.

Final Verdict: automatically generates an INVEST or NOT INVEST decision.

🛠️ Prerequisites

Before running the project, ensure you have the following installed:

Python 3.8+

FFmpeg (Required for audio processing):

Mac: brew install ffmpeg

Windows: Download FFmpeg and add it to your System PATH.

📦 Installation

Clone or Download this repository.

Install the required Python libraries:

pip install -r requirements.txt


⚙️ Configuration

Open SharkTank_Final_Update.py.

The code is pre-configured to look for an audio file named pitch3.wav.

Ensure your audio recording is in the same folder as the script.

Rename your file to pitch3.wav.

API Key: The script is currently set up with a Google Gemini API key. If you wish to use your own, replace the value in os.environ["GOOGLE_API_KEY"].

🏃‍♂️ How to Run

Open your terminal or command prompt.

Navigate to the project folder.

Run the script:

python SharkTank_Final_Update.py


📊 Sample Output

🎤 Transcribing audio...
🔊 Analyzing voice energy...

📝 TRANSCRIPT: "Hi Sharks, humara product hai chai-gpt..."
📊 METRICS: Energy=65/100 | Silence=12%

🧠 The Sharks are deciding...

========================================
**Ashneer Grover:** Bhai kya kar raha hai tu? 15% Margin? Yeh dhanda nahi hai...
**Namita Thapar:** I connect with the founder, but the technology is messy...
**Aman Gupta:** Killer Energy boss! I like the branding...

----------------------------------------
**FINAL RECOMMENDATION:** INVEST
----------------------------------------
========================================
