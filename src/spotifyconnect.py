import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import SpotifyException


class SpotifyConnect:

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
        except Exception as e:
            print(e)

    def searchTracks(self, query: str):
        return self.__sp.search(q=query, type="track", limit=10)["tracks"]["items"]


    def playSong(self, uri: str):
        try:
            self.__sp.
        except:
