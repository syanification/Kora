from setup import loadBasicInfo
from spotifyconnect import SpotifyConnect
from aladeen import Aladeen


def main():
    spConnectInfo = loadBasicInfo()
    if not spConnectInfo:
        return 1  # spotify creds couldn't load
    sp = SpotifyConnect(spConnectInfo)
    sp.findAndPlaySong("holy star grandmaster")


def main2():
    spConnectInfo = loadBasicInfo()
    if not spConnectInfo:
        return 1  # sotify creds couldn't load
    sp = SpotifyConnect(spConnectInfo)
    while True:
        query = input("Enter song name: ")
        sp.findAndPlaySong(query)


def main3():
    aladeen = Aladeen()
    aladeen.handleVoiceCommands()


if __name__ == "__main__":
    main3()
