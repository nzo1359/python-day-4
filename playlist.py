
def playlist_name():
    playlist = ["Good News", "Oh Comely", "Tenohira"]
    count = len(playlist)
    print("Playlist length = ", count)

    playlist.append("Storm")

    count = len(playlist)
    print("Playlist length = ", count)

    print(playlist)


playlist_name()