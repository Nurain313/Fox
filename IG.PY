# Import the required libraries
import openai
import random

# Set up the OpenAI API credentials
openai.api_key = "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"

# Define the function to generate the caption
def generate_caption(movie_title, movie_overview, release_date, rating):
    # Define the prompt for GPT-3 to generate the caption
    prompt = (f"Generate a movie-themed Instagram caption for the movie {movie_title}. The caption should be creative, unique, and engaging. "
              f"The movie's overview is {movie_overview}. It was released on {release_date} and has a rating of {rating} on IMDb. ")
    
    # Generate the caption using GPT-3
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )

    caption = response.choices[0].text.strip()
    
    return caption

# Test the function
movie_title = "The Dark Knight"
movie_overview = "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."
release_date = "2008"
rating = "9.0"
caption = generate_caption(movie_title, movie_overview, release_date, rating)
print(caption)
