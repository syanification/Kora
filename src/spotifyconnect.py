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

    def __init__(self, basicInfo: dict):
        # initializing the spotify session
        try:
            self.__sp = spotipy.Spotify(
                auth_manager=SpotifyOAuth(
                    client_id=basicInfo.get("cid"),
                    client_secret=basicInfo.get("secret"),
                    redirect_uri=basicInfo.get("redirectURI"),
                    scope=basicInfo.get("scope"),
                )
            )
            user = self.__sp.current_user()
        except Exception as e:
            print("ERROR")
            print(e)

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

        songUri = self.searchTracks(songQuery)[0]["uri"]
        self.playSong(songUri)

    def playSong(self, uri: str):
        """plays the song with uri 'uri'"""
        try:
            self.__sp.start_playback(uris=[uri])
        except SpotifyException as e:
            print(e)
            raise self.PlaybackError("Error playing song")

    def pauseSong(self):
        """Pauses the song currently playing"""
        try:
            self.__sp.pause_playback()
        except SpotifyException as e:
            print(e)
            raise self.PlaybackError("Error pausing playback")

    def skipSong(self):
        """Skips to the next song in queue"""
        try:
            self.__sp.next_track()
        except SpotifyException as e:
            print(e)
            raise self.PlaybackError("Error skipping to next song")
