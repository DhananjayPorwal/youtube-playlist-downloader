import os
from pytube import Playlist


def make_alpha_numeric(string):
    return ''.join(char for char in string if char.isalnum())


link = input("Enter YouTube Playlist URL: ✨")

yt_playlist = Playlist(link)

folderName = make_alpha_numeric(yt_playlist.title)
os.mkdir(folderName)

totalVideoCount = len(yt_playlist.videos)
print("Total videos in playlist: 🎦", totalVideoCount)

for index, video in enumerate(yt_playlist.videos, start=1):
    print("Downloading:", video.title)
    video_size = video.streams.get_highest_resolution().filesize
    print("Size:", video_size // (1024 ** 2), "🗜 MB")
    video.streams.get_highest_resolution().download(output_path=folderName)
    print("Downloaded:", video.title, "✨ successfully!")
    print("Remaining Videos:", totalVideoCount - index)

print("All videos downloaded successfully! 🎉")
