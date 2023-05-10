import os
import json
import requests
from googleapiclient.discovery import build
import random 
from pytube import YouTube

# Set up the YouTube API client
developer_key = 'AIzaSyAlxGtZStu15GagMaR9SbFfCHKm0JCxbyg'
youtube = build('youtube', 'v3', developerKey=developer_key)


access_token = "EAANEn3OKwSgBABPoEezed16dsvrkZC6nY8c47QvC7KXYhGonXgSaNuuDM5a85Sof2GeLQ00FnYGgxyawXZAIQsb4vzniTU85EQR6mTGOZCYCBQrv8tkZCaNaIWCt90pxazhBvnmCSoMzBWoqsYJWrKpwEaFolQ32G8UcnrW6r1ZBcgzjjIZAy5Cvtob1sx0VWCTu3cWudQQgZDZD"
instagram_account_id = "17841451329532194"

graph_url = 'https://graph.facebook.com/v15.0/'

   
parent_dir = os.path.dirname(os.getcwd())
movie_file_dir = os.path.join(parent_dir, 'movie_file')
json_file = os.path.join(movie_file_dir, 'upcoming_movies.json')

with open(json_file, 'r') as f:
    upcoming_movies = json.load(f)


# Load previously posted movie IDs from a text file
try:
    with open('posted_movies.txt', 'r') as f:
        posted_movies = set(f.read().splitlines())
except FileNotFoundError:
    posted_movies = set()

movies = []
while len(movies) < 1:
    movie = random.choice(upcoming_movies)
    movies.append(movie)

for movie in movies:
    # Extract movie details
    title = movie['title']
    overview = movie['overview']
    release_date = movie['release_date']
    rating = movie['vote_average']
    poster_path = movie['poster_path']
    image_url = f'https://image.tmdb.org/t/p/original{poster_path}'
    
    # Define query parameters
    query = f"{title}+trailer"
    max_results = 10
    print(f"Movie name: {title}\nRelease date: {release_date}")

    # Call the YouTube Data API to search for videos
    youtube = build('youtube', 'v3', developerKey= developer_key)
    request = youtube.search().list(
        part='id',
        q=query,
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    
    # Extract the url of the first video in the response
    if response['items']:
        video_id = response['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        print(video_url)
    else:
        print(f"No video found for query '{query}'")

    DOWNLOADS_DIR = 'downloads'
    def download_video(youtube_link):
        pass
    video_title = download_video(youtube_link)
    print(video_title)
    def download_video(youtube_link):
        try:
            yt = YouTube(youtube_link)
            video = yt.streams.get_highest_resolution()
            if not os.path.exists('downloads'):
                os.mkdir('downloads')
            video_title = os.path.join('downloads', yt.title)
            file_path = os.path.join('downloads', video.default_filename)
            video.download(output_path='downloads')
            print(video_title)
            print(f'Downloaded video to: {file_path}')
            
            return file_path
            
        except Exception as e:
            print('Error downloading video:', e)
    

    # Function to post a video to Instagram using the Graph API
    def post_video(file_path, caption=''):
        try:
            url = graph_url + instagram_account_id + '/media'
            params = {
                'access_token': access_token,
                'caption': caption,
                'media_type': 'VIDEO'
            }
            files = {
                'video_file': open(file_path, 'rb')
            }
            response = requests.post(url, params=params, files=files).json()
            if response.get('id'):
                print('Video has been posted successfully!')
            else:
                print('Error: Could not post video to Instagram.')
        except Exception as e:
            print('Error posting video:', e)



    youtube_link = video_url
    caption =  f" | #movie \n {title}\n {overview}\nRelease date: {release_date} \nRating: {rating} \n.\n.\n.\n #10foxmovies #movietoday #follow #updates #10foxmovies_bot @nurainomar09"

    # Download the video from the YouTube link
    video_title = download_video(youtube_link)

    if video_title:
        # Post the video to Instagram
        post_video(video_title, caption=caption)

        # Delete the downloaded video file
        os.remove(video_title)
    else:
        print('Could not post video to Instagram.')

    
    
    