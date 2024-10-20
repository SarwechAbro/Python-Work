import yt_dlp
import os
import requests
from colorama import init, Fore

init(autoreset=True)

def get_playlist_videos(playlist_id, apikey):
    video_links = []
    url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={playlist_id}&key={apikey}'

    while url:
        response = requests.get(url)
        data = response.json()

        for item in data.get('items', []):
            video_id = item['snippet']['resourceId']['videoId']
            video_links.append(f'https://www.youtube.com/watch?v={video_id}')

        # Check for next page token
        url = (f'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50'
               f'&playlistId={playlist_id}&key={apikey}&pageToken={data.get("nextPageToken")}' if 'nextPageToken' in data else None)

    return video_links

def is_video_available(video_id, apikey):
    url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={apikey}&part=status'
    response = requests.get(url)
    data = response.json()
    if 'items' in data and len(data['items']) > 0:
        status = data['items'][0]['status']
        return status['privacyStatus'] == 'public' and status['embeddable']
    return False

def download_video(video_url, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_path = os.path.join(output_folder, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'outtmpl': output_path,
        'ignore_errors': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading Video from {video_url}...")
        ydl.download([video_url])

def download_playlist(playlist_id, api_key, output_folder):
    video_urls = get_playlist_videos(playlist_id, api_key)
    total_videos = len(video_urls)

    for idx, url in enumerate(video_urls, start=1):
        video_id = url.split('v=')[1]
        if is_video_available(video_id, api_key):
            print(f"Downloading Video {Fore.LIGHTBLUE_EX}{idx}{Fore.RESET} from {Fore.LIGHTBLUE_EX}{total_videos}{Fore.RESET}")
            download_video(url, output_folder)
        else:
            print(f"{Fore.RED}Video {url} is unavailable or hidden.")


if __name__ == "__main__":
    api_key = 'AIzaSyDGQz5bbHF1LA8bE7MMQEKmSHx9YRKhtb0'
    input_url = input("Enter the YouTube video or playlist URL: ")
    
    download_folder = input("Enter the folder where you want to save the video (default is 'Videos'): ")
    default_folder = os.path.expanduser(f'~/Videos/{download_folder}')
    if 'list' in input_url:
        playlist_id = input_url.split('list=')[1].split('&')[0]  # Extract the playlist ID
        download_playlist(playlist_id, api_key, output_folder=default_folder)
    else:
        download_video(input_url, output_folder=default_folder)

      
