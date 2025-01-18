import sendPrompt
import SpeechToText
from spotifyconnect import SpotifyConnect
from setup import loadBasicInfo


class Aladeen:

    def __init__(self):
        self.sp = self.initializeSpotify()

    def initializeSpotify(self):
        spConnectInfo = loadBasicInfo()
        if not spConnectInfo:
            return None  # spotify creds couldn't load
        try:
            return SpotifyConnect(spConnectInfo)
        except Exception as e:
            print(e)
            return None

    def getCommand(self):
        """get command from ai"""
        pass

    def handleVoiceCommands(self):
        """get voice input user"""
        # call the voice shit to get the speech to text input
        query = ""
        result = SpeechToText.getAudioString()
        print(result)
        command = sendPrompt.getCommand(result)

        if command[:4] == "play":
            query = command[5:]

        try:
            match command:
                case "play":
                    self.sp.findAndPlaySong(query)
                    print("Playing song")

                case "pause":
                    self.sp.pausePlayback()
                    print("Pausing")

                case "resume":
                    self.sp.resumePlayback()
                    print("Resuming")

                case "None":
                    pass

        except SpotifyConnect.PlaybackError as e:
            print(e)

        except SpotifyConnect.SearchError as e:
            print(e)

    def executeVoiceCommand(self):
        """transform voice input into command
        to spotify"""
