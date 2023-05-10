import requests
from pytube import YouTube

API_KEY = "aa987a7052db48e0194a06791c4e979e"
API_BASE_URL = "https://api.themoviedb.org/3"


def search_movie(query):
    search_url = f"{API_BASE_URL}/search/multi"
    params = {"api_key": API_KEY, "query": query}
    response = requests.get(search_url, params=params).json()
    search_results = response.get("results", [])
    if len(search_results) == 0:
        print("No results found")
        return None
    else:
        print("Multiple search results found:")
        for i, result in enumerate(search_results):
            title = result.get("title", result.get("name", ""))
            media_type = result.get("media_type", "")
            print(f"{i+1}. {title} ({media_type})")
        choice = int(input("Enter the number of the result to choose: "))
        search_result = search_results[choice - 1]
        return search_result


def get_movie_data(movie_id):
    movie_url = f"{API_BASE_URL}/movie/{movie_id}"
    params = {"api_key": API_KEY}
    response = requests.get(movie_url, params=params).json()
    return response


def download_trailer(trailer_url, output_path):
    yt = YouTube(trailer_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if stream:
        print("Downloading trailer...")
        stream.download(output_path)
        print("Trailer downloaded successfully")
    else:
        print("No suitable streams found to download")


def main():
    query = input("Enter a movie or TV show name to search: ")
    search_result = search_movie(query)
    if search_result is None:
        return
    movie_data = get_movie_data(search_result["id"])
    youtube_key = None
    videos = movie_data.get("videos", {}).get("results", [])
    if len(videos) > 0:
        youtube_key = videos[0].get("key", None)
    print ("ID:", movie_data.get("id", "")) 
    print("Movie title:", movie_data.get("title", ""))
    print("Overview:", movie_data.get("overview", ""))
    print("Poster URL:", f"https://image.tmdb.org/t/p/w500{movie_data.get('poster_path', '')}")
    if youtube_key:
        trailer_url = f"https://www.youtube.com/watch?v={youtube_key}"
        download_trailer(trailer_url, "./trailers")
    else:
        print("Trailer not found")


if __name__ == "__main__":
    main()

