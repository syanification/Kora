import sendPrompt
import SpeechToText
from spotifyconnect import SpotifyConnect
from setup import loadBasicInfo
from Actions import 


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

    def handleVoiceCommands(self):
        """get voice input user"""
        # call the voice shit to get the speech to text input
        query = ""
        result = SpeechToText.getAudioString()
        print("Speech to text result: %s" % (result))

        command = sendPrompt.getCommand(result)
        print("Command: %s" % command)

        if command[:4] == "play":
            query = command[5:]
            command = command[:4]

        try:
            match command:
                case "play":
                    self.play(query)

                case "pause":
                    self.pause()

                case "resume":
                    self.resume()

                case "skip":
                    self.skip()

                case "None":
                    pass

        except SpotifyConnect.PlaybackError as e:
            print(e)

        except SpotifyConnect.SearchError as e:
            print(e)

    def play(self, query):
        self.sp.findAndPlaySong(query)
        print("Playing song")

    def pause(self):
        self.sp.pausePlayback()
        print("Pausing")

    def resume(self):
        self.sp.resumePlayback()
        print("Resuming")

    def skip(self):
        self.sp.skipSong()
        print("Skipping")
