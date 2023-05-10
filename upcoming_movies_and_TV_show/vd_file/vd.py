import os
import json
import google.auth
import google.auth.transport.requests
import requests
import re
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

    def delete_downloaded_videos():
        if not os.path.exists(DOWNLOADS_DIR):
            return
        for filename in os.listdir(DOWNLOADS_DIR):
            os.remove(os.path.join(DOWNLOADS_DIR, filename))
        print("All downloaded videos have been deleted.")

    def download_youtube_video(url):
        delete_downloaded_videos()  # delete previously downloaded videos
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not os.path.exists(DOWNLOADS_DIR):
            os.mkdir(DOWNLOADS_DIR)
        video_filename = f"{yt.title}.mp4"
        video_filepath = os.path.join(DOWNLOADS_DIR, video_filename)
        video.download(video_filepath)
        print(f"Video {yt.title} has been downloaded.")
        print(f"The video is stored in the {DOWNLOADS_DIR} folder.")

    if __name__ == "__main__":
        url = video_url
        download_youtube_video(url)
 
 
    
    
    