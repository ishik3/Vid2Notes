from pytube import YouTube
import os

def youtube_mp3(ytlink):
    print('\nYoutube to Mp3 Format Downloader\n')
    yt = YouTube(ytlink)

    try:
        print("\nDownloading....")
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download()
        base, ext = os.path.splitext(out_file)
        file_name = base + ".mp3"
        os.rename(out_file, file_name)
        return file_name

    except:
        print("\nSomething Went Wrong Please Try Again....\n")
    