import yt_dlp
import os

# Set the download folder (Change this path as needed)
download_folder = os.path.join(os.getcwd(), "F:\\testytdownloadDownloads")
os.makedirs(download_folder, exist_ok=True)  # Create folder if it doesn't exist

link = input("Enter the video URL: ")


ydl_opts = {
    "outtmpl": os.path.join(download_folder, "%(title)s.%(ext)s"), # Save the file with the video title
    "format": "best",  # Download best available single file (video + audio)
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print(f"Download complete! Video saved in: {download_folder}")
