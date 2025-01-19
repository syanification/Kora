from kivy.event import EventDispatcher
import sendPrompt
import SpeechToText
from spotifyconnect import SpotifyConnect
from setup import loadBasicInfo


class Aladeen(EventDispatcher):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_play")
        self.register_event_type("on_pause")
        self.register_event_type("on_resume")
        self.register_event_type("on_skip")
        self.register_event_type("on_launch")

        self.sp = self.initializeSpotify()
        title, length, coverurl, isPlaying, progress = self.getPlaybackState()
        self.dispatch("on_launch", title, length, coverurl, isPlaying, progress)  # Notify UI

    def on_play(self, *args):
        pass

    def on_pause(self, *args):
        pass

    def on_resume(self, *args):
        pass

    def on_skip(self, *args):
        pass

    def on_launch(self, *args):
        pass

    def initializeSpotify(self):
        spConnectInfo = loadBasicInfo()
        if not spConnectInfo:
            return None
        try:
            return SpotifyConnect(spConnectInfo)
        except Exception as e:
            print(e)
            return None

    def handleVoiceCommands(self):
        """Handles voice commands."""
        query = ""
        result = SpeechToText.getAudioString()
        print("Speech to text result: %s" % result)

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
        title, length, coverurl = self.sp.findAndPlaySong(query)
        print("Playing song")

        self.dispatch("on_play", title, length, coverurl)

    def pause(self):
        self.sp.pausePlayback()
        print("Pausing")
        self.dispatch("on_pause")

    def resume(self):
        self.sp.resumePlayback()
        print("Resuming")
        self.dispatch("on_resume")

    def skip(self):
        title, length, coverurl, isPlaying, progress = self.sp.skipSong()
        print("Skipping")
        self.dispatch("on_skip", title, length, coverurl, isPlaying, progress)

    def getPlaybackState(self):
        try:
            state = self.sp.getCurrentPlaybackState()
        except SpotifyConnect.PlaybackError as e:
            print(e)
            return
        return state
