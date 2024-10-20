import requests

api_key = 'AIzaSyDGQz5bbHF1LA8bE7MMQEKmSHx9YRKhtb0'
video_id = "H2jkONa2tQQ"
url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=status'
response = requests.get(url)
data = response.json()
print(data)
if 'items' in data and len(data['items']) > 0:
    status = data['items'][0]['status']
    status['privacyStatus'] == 'public' and status['embeddable']
    print('Ok')
else:
    print('video not available')    