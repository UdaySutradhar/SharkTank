🦈 Shark Tank India Pitch Analyzer

A multimodal AI tool that analyzes startup pitches using Audio Signal Processing and Large Language Models (LLMs). The system evaluates vocal delivery (energy, confidence) and business content to simulate feedback from specific Shark Tank India judges.

🚀 Features

1. Audio Signal Processing:

-> Calculates Energy Levels (Josh Meter).

-> Detects Silence & Hesitation (Nervousness Index).

2. Hinglish Transcription: Uses Google's Speech Recognition to transcribe mixed Hindi-English pitches.

3. AI Shark Panel (Gemini 2.5 Pro):

-> Ashneer Grover: Roasts low margins and nervousness ("Doglapan").

-> Namita Thapar: Opts out if the pitch is confusing ("Expertise nahi hai").

-> Aman Gupta: Focuses on energy and branding.

4. Final Verdict: automatically generates an INVEST or NOT INVEST decision.

🛠️ Prerequisites

Before running the project, ensure you have the following installed:

1. Python 3.8+

2. FFmpeg (Required for audio processing):

-> Mac: brew install ffmpeg

-> Windows: Download FFmpeg and add it to your System PATH.

📦 Installation

1. Clone or Download this repository.

2. Install the required Python libraries:

pip install -r requirements.txt


⚙️ Configuration

1. Open Main.py.

2. The code is pre-configured to look for an audio file named pitch3.wav.

-> Ensure your audio recording is in the same folder as the script.

-> You can Rename your file to pitch2.wav or pitch1.wav as required.

3. API Key: The script is currently set up with a Google Gemini API key. If you wish to use your own, replace the value in os.environ["GOOGLE_API_KEY"].

🏃‍♂️ How to Run

1. Open your terminal or command prompt.

2. Navigate to the project folder.

3. Run the script:

python Main.py


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
