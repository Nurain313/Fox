import requests
import json
import os.path

API_KEY = 'aa987a7052db48e0194a06791c4e979e'

def get_upcoming_tv(api_key):
    url = f'https://api.themoviedb.org/3/tv/on_the_air?api_key={api_key}&language=en-US&page=1'
    url_1 = f'https://api.themoviedb.org/3/tv/on_the_air?api_key={api_key}&language=en-US&page=2'
    url_2 = f'https://api.themoviedb.org/3/tv/on_the_air?api_key={api_key}&language=en-US&page=3'
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
    old_titles = set([d['name'] for d in old_data])
    return [d for d in data if 'name' in d and d['name'] not in old_titles]

def extract_data_from_json(data):
    extracted_data = []
    for item in data:
        if 'name' in item:
            name = item['name']
        elif 'name' in item:
            name = item['name']
        else:
            continue
        release_date = item.get('release_date') or item.get('first_air_date')
        overview = item.get('overview', 'N/A')
        extracted_data.append(f"{name}\nRelease date: {release_date}\nOverview: {overview}\n")
    return extracted_data

#while True:
if True:
    print("updating tv_shows...")
    tv_shows = get_upcoming_tv(API_KEY)

    old_data = load_from_file('upcoming_tv_shows.json')
    filtered_tv_shows = filter_duplicates(tv_shows, old_data)

    num_new_tv_shows = len(filtered_tv_shows)

    if num_new_tv_shows > 0:
        data_to_save = old_data + filtered_tv_shows
        save_to_file(data_to_save, 'upcoming_tv_shows.json')
        print(f"Added {num_new_tv_shows} new TV shows to upcoming_tv_shows.json")

        extracted_data = extract_data_from_json(data_to_save)
        with open('upcoming_tv_shows.txt', 'a') as f:
            f.writelines(extracted_data)
        print(f"Added {num_new_tv_shows} new TV shows to upcoming.txt")
    else:
        print("No new titles found.")

    print("Tv_show database updated.")
   # time.sleep(12 * 60 * 60) # wait 12 hours before scraping again
    #time.sleep(30 * 60) # wait for 30 minutes before scraping again 
