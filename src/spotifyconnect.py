import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import SpotifyException


class SpotifyConnect:

    class PlaybackError(Exception):
        """Exception for any playback errors"""

        def __init__(self, message="Playback error"):
            self.__msg = message

        def __str__(self):
            return self.__msg

    class SearchError(Exception):
        """Exception for any errors found while searching"""

        def __init__(self, message="Search error"):
            self.__msg = message

        def __str__(self):
            return self.__msg

    def __init__(self, connectionInfo: dict):
        # initializing the spotify session
        try:
            self.__sp = spotipy.Spotify(
                auth_manager=SpotifyOAuth(
                    client_id=connectionInfo.get("cid"),
                    client_secret=connectionInfo.get("secret"),
                    redirect_uri=connectionInfo.get("redirectURI"),
                    scope=connectionInfo.get("scope"),
                )
            )
        except SpotifyException as e:
            print(e)
            raise Exception("Unable to initialize connection to Spotify API")

    def __getRelevantAttrs(self, track: dict) -> tuple:
        title = track["name"]
        length = track["duration_ms"]
        coverurl = track["album"]["images"][0]["url"]
        return (title, length, coverurl)

    def getCurrentPlaybackState(self):
        try:
            playbackState = self.__sp.current_playback()
            if not playbackState:
                return (None, None, None, None)

            isPlaying = playbackState["is_playing"]
            uri = playbackState["item"]["uri"]
            track = self.__sp.track(uri)
        except SpotifyException as e:
            print(e)
            raise self.PlaybackError("Error getting current playback state")

        title, length, coverurl = self.__getRelevantAttrs(track)
        return (title, length, coverurl, isPlaying)

    def searchTracks(self, query: str):
        """Returns the first 10 tracks received from the search"""
        try:
            return self.__sp.search(q=query, type="track", limit=10)["tracks"]["items"]
        except SpotifyException as e:
            print(e)
            raise self.SearchError("Error while searching for song")

    def findAndPlaySong(self, songQuery: str):
        """Searches the song using the query in songQuery
        and plays the top result"""

        track = self.searchTracks(songQuery)[0]
        songUri = track["uri"]
        self.playSong(songUri)
        return self.__getRelevantAttrs(track)

    def playSong(self, uri: str):
        """plays the song with uri 'uri'"""
        try:
            self.__sp.start_playback(uris=[uri])
        except SpotifyException as e:
            print(e)
            raise self.PlaybackError("Error playing song")

    def pausePlayback(self):
        """Pauses the song currently playing"""
        try:
            self.__sp.pause_playback()
        except SpotifyException as e:
            print(e)
            raise self.PlaybackError("Error pausing playback")

    def resumePlayback(self):
        try:
            self.__sp.start_playback()
        except SpotifyException as e:
            print(e)
            raise self.PlaybackError("Error resuming playback")

    def skipSong(self):
        """Skips to the next song in queue"""
        try:
            self.__sp.next_track()
            return self.getCurrentPlaybackState()

        except SpotifyException as e:
            print(e)
            raise self.PlaybackError("Error skipping to next song")
