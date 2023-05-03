# Set up the prompt
prompt = f"Please ignore all previous instructions. Please respond only in the English language. You are an Instagrammer with a large fan following. You have a cheerful tone of voice. You have an informative writing style. Write an Instagram post description in just a few sentences for this movie or TV show {title}.\n{overview}\nRelease date: {release_date}\nRating: {rating}. Make the description readable by formatting with new lines. Include emojis and the Instagram hashtags in the description. Try to use unique emojis in the description. The description should have a hook and entice the readers. Do not repeat yourself. Do not self-reference. Do not explain what you are doing. Do not explain what you are going to do. Start directly by writing down the description."

# Loop through movies and TV shows
for item in movies + tv_shows:
    # Extract details
    title = item.get('title', item.get('name', 'Unknown title'))
    overview = item.get('overview', '')
    release_date = item.get('release_date', item.get('first_air_date', 'Unknown release date'))
    rating = item.get('vote_average', 'Unknown rating')
    poster_path = item.get('poster_path', '')
    poster_url = f'https://image.tmdb.org/t/p/original{poster_path}'

    # Generate caption using GPT
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt.format(title=title, overview=overview, release_date=release_date, rating=rating),
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()

    # Download movie poster and post to Facebook
    response = requests.get(poster_url)
    img = response.content
    graph.put_photo(image=img, message=message)

    # Add the posted item ID to the set of posted item IDs
    if 'id' in item:
        if item in movies:
            posted_movies.add(item['id'])
        else:
            posted_tv_shows.add(item['id'])

    # Delay next post by 5 seconds 
    time.sleep(5)

# Write the set of posted movie and TV show IDs to the text files
with open('posted_movies.txt', 'w') as f:
    f.write('\n'.join(str(movie_id) for movie_id in posted_movies))

with open('posted_tv_shows.txt', 'w') as f:
    f.write('\n'.join(str(tv_show_id) for tv_show_id in posted_tv_shows))

print("FB: %d movies posted, %d TV shows posted" % (len(posted_movies), len(posted_tv_shows)))
