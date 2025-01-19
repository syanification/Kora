import speech_recognition as sr

# Initialize recognizer class (for recognizing speech)


# Use the microphone as the audio source
def getAudioString() -> str:

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Calibrating microphone... Please wait.")
        recognizer.adjust_for_ambient_noise(
            source, duration=1
        )  # Adjusts to background noise

        # Fine-tune silence detection
        recognizer.pause_threshold = 1  # Waits 2 sec after speech ends before stopping
        recognizer.non_speaking_duration = 1  # Extra 1 sec buffer before stopping

        print("Please say a command...")
        audio = recognizer.listen(source, timeout=10)  # Waits indefinitely for speech

        print("Recognizing command...")
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
            return ""
        except sr.RequestError:
            print("Error connecting to Google API.")
            return ""

        # finally:
        #     microphone = None  # This releases the microphone object
