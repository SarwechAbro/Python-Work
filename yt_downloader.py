import yt_dlp
import os

def download_video(url, output_folder, output_filename='%(title)s.%(ext)s'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the folder if it doesn't exist

    output_path = os.path.join(output_folder, output_filename)

    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Download video with 720p or lower
        'outtmpl': output_path,  # Output file name template with folder path
        'noplaylist': True,      # Download only the single video, not a playlist
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_folder = input("Enter the folder where you want to save the video (default is 'Videos'): ")
    default_folder = '/home/sarwechabro/Videos/' + download_folder
    download_video(video_url, output_folder=default_folder)
