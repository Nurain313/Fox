import json
import requests
import random
import os

# Set up access token and graph API
access_token = "EAANEn3OKwSgBABPoEezed16dsvrkZC6nY8c47QvC7KXYhGonXgSaNuuDM5a85Sof2GeLQ00FnYGgxyawXZAIQsb4vzniTU85EQR6mTGOZCYCBQrv8tkZCaNaIWCt90pxazhBvnmCSoMzBWoqsYJWrKpwEaFolQ32G8UcnrW6r1ZBcgzjjIZAy5Cvtob1sx0VWCTu3cWudQQgZDZD"
instagram_account_id = "17841451329532194"

# Load upcoming movies from JSON file
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
    


# Randomly select two movies that haven't been posted before
movies = []
while len(movies) < 2:
    movie = random.choice(upcoming_movies)
    if movie['id'] not in posted_movies:
        movies.append(movie)

# Loop over selected movies and post to Instagram
print("Instagram started.......")
for movie in movies:
    # Extract movie details
    title = movie['title']
    overview = movie['overview']
    release_date = movie['release_date']
    rating = movie['vote_average']
    poster_path = movie['poster_path']
    image_url = f'https://image.tmdb.org/t/p/original{poster_path}'
    caption = f" | #movie \n {title}\n {overview}\nRelease date: {release_date} \nRating: {rating} \n.\n.\n.\n #10foxmovies #movietoday #follow #updates #10foxmovies_bot @nurainomar09"    
    graph_url = 'https://graph.facebook.com/v15.0/'
    url = graph_url + instagram_account_id + '/media'
    param = dict()
    param['access_token'] = access_token
    param['caption'] = caption
    param['image_url'] = image_url
    response = requests.post(url, params=param)
    response = response.json()
    print(response)
    creation_id = response ['id']
    url = f"https://graph.facebook.com/{instagram_account_id}/media_publish"
    params = dict()
    params = {'creation_id': creation_id, 'access_token': access_token}
    headers = None  # No headers needed for POST /media_publish API
    r = requests.post(url, headers=headers, params=params)
    r.raise_for_status()

    # Add the posted movie ID to the set of posted movie IDs
    posted_movies.add(movie['id'])

# Write the set of posted movie IDs to the text file
with open('posted_movies.txt', 'w') as f:
    #f.write('\n'.join(posted_movies))
    f.write('\n'.join(str(movie_id) for movie_id in posted_movies))

print("Instagram: 2 movies posted")

# posting tv_show

tv_file_dir = os.path.join(parent_dir, 'tv_show_file')
tv_json_file = os.path.join(tv_file_dir, 'upcoming_tv_shows.json')

with open(tv_json_file, 'r') as f:
    upcoming_tv_shows = json.load(f)

try:
    with open('posted_tv_shows.txt', 'r') as f:
        posted_tv_shows = set(f.read().splitlines())
except FileNotFoundError:
    posted_tv_shows = set()

tv_shows = []
while len(tv_shows) < 2:
    tv_show = random.choice(upcoming_tv_shows)
    if tv_show['id'] not in posted_tv_shows:
        tv_shows.append(tv_show)


for tv_show in tv_shows:
    # Extract tv_show details
    name = tv_show['name']
    overview = tv_show['overview']
    first_air_date = tv_show['first_air_date']
    rating = tv_show['vote_average']
    poster_path = tv_show['poster_path']
    poster_url_tv= f'https://image.tmdb.org/t/p/original{poster_path}'
    
    caption = f" | #tv_show \n {name}\n {overview}\nRelease date: {release_date} \nRating: {rating} \n.\n.\n.\n #10foxmovies #movietoday #follow #updates #10foxmovies_bot @nurainomar09" 
    graph_url = 'https://graph.facebook.com/v15.0/'
    url = graph_url + instagram_account_id + '/media'
    param = dict()
    param['access_token'] = access_token
    param['caption'] = caption
    param['image_url'] = poster_url_tv
    response = requests.post(url, params=param)
    response = response.json()
    print(response)
    creation_id = response ['id']
    url = f"https://graph.facebook.com/{instagram_account_id}/media_publish"
    params = dict()
    params = {'creation_id': creation_id, 'access_token': access_token}
    headers = None  # No headers needed for POST /media_publish API
    r = requests.post(url, headers=headers, params=params)
    r.raise_for_status()

    # Add the posted movie ID to the set of posted movie IDs
    posted_tv_shows.add(tv_show['id'])
    
    # Write the set of posted movie IDs to the text file
with open('posted_tv_shows.txt', 'w') as f:
    #f.write('\n'.join(posted_movies))
    f.write('\n'.join(str(tv_show_id) for tv_show_id in posted_tv_shows))

print("Instagram: 2 tv_shows posted")