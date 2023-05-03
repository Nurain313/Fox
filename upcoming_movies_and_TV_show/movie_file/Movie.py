import requests
import json
import os.path
import time

API_KEY = 'aa987a7052db48e0194a06791c4e979e'

def get_upcoming_movies(api_key):
    url = f'https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}&language=en-US&page=1'
    url_1 = f'https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}&language=en-US&page=2'
    url_2 = f'https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}&language=en-US&page=3'
    response = [requests.get(url), requests.get(url_1), requests.get(url_2)]
    data = []
    for response in response:
        data.extend(response.json()['results'])
    return data

def save_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def filter_duplicates(data, old_data):
    old_titles = set([d['title'] for d in old_data])
    return [d for d in data if 'title' in d and d['title'] not in old_titles]

def extract_data_from_json(data):
    extracted_data = []
    for item in data:
        if 'title' in item:
            title = item['title']
        elif 'name' in item:
            title = item['name']
        else:
            continue
        release_date = item.get('release_date') or item.get('first_air_date')
        overview = item.get('overview', 'N/A')
        extracted_data.append(f"{title}\nRelease date: {release_date}\nOverview: {overview}\n")
    return extracted_data

#while True
if True:
    print("updating movies...")
    movies = get_upcoming_movies(API_KEY)

    old_data = load_from_file('upcoming_movies.json')
    filtered_movies = filter_duplicates(movies, old_data)

    num_new_movies = len(filtered_movies)

    if num_new_movies > 0:
        data_to_save = old_data + filtered_movies
        save_to_file(data_to_save, 'upcoming_movies.json')
        print(f"Added {num_new_movies} new movies to upcoming_movies.json")

        extracted_data = extract_data_from_json(data_to_save)
        with open('upcoming_movies.txt', 'a') as f:
            f.writelines(extracted_data)
        print(f"Added {num_new_movies} new movies to upcoming_movies.txt")
    else:
        print("No new titles found.")

    print("Movie database updated.")
    #time.sleep(12 * 60 * 60) # wait 12 hours before scraping again
    #time.sleep(30 * 60) # wait for 30 minutes before scraping again 

