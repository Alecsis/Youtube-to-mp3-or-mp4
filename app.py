from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("Views: ", yt.views)

print("Uploaded: ", yt.publish_date)

quality = input("Type mp4 or mp3 for video type: ")

if quality == 'mp4':
    yd = yd = yt.streams.get_highest_resolution()
elif quality == 'mp3':
    yd = yt.streams.get_audio_only()
else:
    print("go eat trash")

yd.download("C:/Users/User/documents/ytdownloads")
