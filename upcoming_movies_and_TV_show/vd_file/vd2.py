import os
import json
import google.auth
import google.auth.transport.requests
import requests
import re
from googleapiclient.discovery import build
import random 
import youtube_dl 

# Set up the YouTube API client
developer_key = 'AIzaSyAlxGtZStu15GagMaR9SbFfCHKm0JCxbyg'
youtube = build('youtube', 'v3', developerKey=developer_key)

graph_url = 'https://graph.facebook.com/v15.0/'

parent_dir = os.path.dirname(os.getcwd())
movie_file_dir = os.path.join(parent_dir, 'movie_file')
json_file = os.path.join(movie_file_dir, 'upcoming_movies.json')

with open(json_file, 'r') as f:
    upcoming_movies = json.load(f)

movies = []
while len(movies) < 1:
    movie = random.choice(upcoming_movies)
    movies.append(movie)

def delete_downloaded_videos():
    if not os.path.exists('downloads'):
        return
    for filename in os.listdir('downloads'):
        os.remove(os.path.join('downloads', filename))
    print("All downloaded videos have been deleted.")



for movie in movies:
    delete_downloaded_videos()
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




    # URL of the video to be downloaded
    video_url = video_url
    
    # Options for downloading the video
    ydl_opts = {
        "format": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "outtmpl": "downloads/%(title)s.%(ext)s"
    }
    
    # Create the downloads folder if it doesn't exist
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    
    # Create a YoutubeDL object and download the video
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
     
