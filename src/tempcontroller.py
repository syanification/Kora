from setup import loadBasicInfo
from spotifyconnect import SpotifyConnect


def main():
    spConnectInfo = loadBasicInfo()
    if not spConnectInfo:
        return 1  # spotify creds couldn't load
    sp = SpotifyConnect(spConnectInfo)
    sp.searchTracks("basil pesto sedge warbler")


if __name__ == "__main__":
    main()
