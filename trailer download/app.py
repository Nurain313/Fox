from flask import Flask, request, render_template
from run import search_movie, get_movie_data, download_trailer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route for the home page
@app.route('/search', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        query = request.form.get('query')
        search_results = search_movie(query)
        return render_template('result.html', search_results=search_results, query=query)
    else:
        return render_template('index.html')


# Route for the result page
@app.route('/result')
def result():
    movie_id = request.args.get('id')
    movie_data = get_movie_data(movie_id)
    print("Movie title:", movie_data["title"])
    print("Overview:", movie_data["overview"])
    print("Poster URL:", f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}")
    if "videos" in movie_data and len(movie_data["videos"]["results"]) > 0:
        trailer_key = movie_data["videos"]["results"][0]["key"]
        trailer_url = f"https://www.youtube.com/watch?v={trailer_key}"
        download_trailer(trailer_url, "./trailers")
        return render_template('trailer.html', trailer_url=trailer_url, title=movie_data["title"])
    else:
        print("Trailer not found.")
        return render_template('error.html', message="Trailer not found")

@app.route('/download')
def download():
    trailer_url = request.args.get('trailer_url')
    download_trailer(trailer_url, "./trailers")
    return "Trailer downloaded successfully"

if __name__ == '__main__':
    app.run(debug=True)
