# 🗣️ Simple Speech Recognition Command Tool

This is a **basic voice-controlled Python tool** that uses your microphone input to recognize speech and execute simple commands like saying "hello", telling the time, or exiting the program.

## 📂 Project Overview
The project uses the **`speech_recognition`** library to capture audio from the microphone and interpret it using Google's Web Speech API.

### ✅ Features
- Listens to voice commands via your microphone
- Recognizes and responds to commands like:
  - `hello` → Responds with a greeting
  - `time` → Tells the current system time
  - `exit` or `quit` → Ends the program
- Simple and interactive command loop

---

## 🛠️ Requirements
Make sure you have the following Python packages installed:

```bash
pip install SpeechRecognition
pip install PyAudio
