import speech_recognition as sr

# Initialize recognizer class (for recognizing speech)
recognizer = sr.Recognizer()


#
# Function to simulate controlling music based on command
def control_music(command):
    if "play song" in command:
        print("Playing song...")
    elif "pause song" in command:
        print("Pausing song...")
    # elif "skip song" in command:
    #     print("Skipping to next song...")
    # elif "resume song" in command:
    #     print("Resuming song...")
    # elif "volume up" in command:
    #     print("Increasing volume...")
    # elif "volume down" in command:
    #     print("Decreasing volume...")
    # elif "search song" in command:
    #     song = command.replace("search song", "").strip()  # Extract song name after "search song"
    #     print(f"Searching for song: {song}...")
    else:
        print("Command not recognized!")


# Use the microphone as the audio source
try:
    with sr.Microphone() as source:
        print("Please say a command...")
        recognizer.adjust_for_ambient_noise(
            source
        )  # Adjust for ambient noise in the environment
        audio = recognizer.listen(source)  # Capture the audio

        try:
            print("Recognizing command...")
            # Using Google Web Speech API to convert audio to text (requires an internet connection)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")

            # Call the control_music function to perform the action based on the recognized command
            control_music(command)

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results from Google Web Speech API.")

finally:
    microphone = None  # This releases the microphone object

if __name__ == "__main__":
    control_music("play song")
