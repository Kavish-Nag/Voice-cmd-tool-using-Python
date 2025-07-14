import speech_recognition as sr
import datetime

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Say something...")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Use Google Web Speech API
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
    return ""

def run_command(command):
    if "hello" in command:
        print("Hi there!")
    elif "time" in command:
        print("Current time is:", datetime.datetime.now().strftime("%H:%M:%S"))
    elif "exit" in command or "quit" in command:
        print("Goodbye!")
        return False
    else:
        print("Command not recognized.")
    return True

def main():
    print("Simple Speech Recognition Tool")
    print("Commands: hello, time, exit")

    while True:
        command = recognize_speech_from_mic()
        print("DEBUG: Recognized command =", command)
        if not run_command(command):
            break

if __name__ == "__main__":
    main()
