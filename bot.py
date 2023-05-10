from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#from aiogram.dispatcher import FSMContext
#from aiogram.dispatcher.filters import Text
#from aiogram.dispatcher.filters.state import State, StatesGroup
import requests
import time


bot = Bot(token='5845574074:AAGvEJMGc3o1sJ3eKOm7CB7pl8L5WcdBz_Q')
dp = Dispatcher(bot)

# Language selection
lang1 = KeyboardButton('🇺🇸 English')  
lang2 = KeyboardButton('🇫🇷 Français')
lang3 = KeyboardButton('🇪🇸 Español')
lang_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(lang1).add(lang2).add(lang3)

# Streaming services images
netflix_image = 'https://www.freepnglogos.com/uploads/netflix-logo-history-32.png'
hulu_image = 'https://www.freepnglogos.com/uploads/hulu-logo-18.png'
prime_video_image = 'https://www.freepnglogos.com/uploads/prime-video-logo-png-21.png'

# Options selection: English
en_options1 = KeyboardButton('🎬 Showtimes')
en_options2 = KeyboardButton('🔍 Search')
en_options3 = KeyboardButton('📰 News')
en_options4 = KeyboardButton('🔥 Popular')
en_options_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(en_options1).add(en_options2).add(en_options3).add(en_options4)

# Sends welcome message after start
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f'👋 Welcome {user_name} to 10 Fox Movies! This is a build-up mode, stay tuned for more features! 🎉\n\n'
                         f'🎥 Our bot provides you with the latest showtimes, news, and popular movies from top streaming services. '
                         f'You can also search for specific movies and get the details.\n\n'
                         f'📺 Streaming services we cover:\n'
                         f'Netflix: {netflix_image}\n'
                         f'Hulu: {hulu_image}\n'
                         f'Prime Video: {prime_video_image}\n'
                         f'Look to catch up with other services you would recommend in future\n\n'
                         
                         f'👉 To get started, please select your language below.', reply_markup = lang_kb)
    
# Sends help message
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(f'Thank you for using 10 Fox Movies! We are always here to help. '
                         f'Please send us a message at @nurainomar09 if you need any assistance. '
                         f'You can also support us by sharing the bot and joining our WhatsApp group: '
                         f'https://chat.whatsapp.com/C0WfYBriwqUFXugiQdnySD')

# Options selection: English
@dp.message_handler(regexp='🇺🇸 English')
async def english(message: types.Message):
    await message.answer('👉 What do you need?', reply_markup = en_options_kb)

# Other language options
@dp.message_handler(regexp='🇫🇷 Français')
async def french(message: types.Message):
    await message.answer('👉 Fonctionnalités à venir bientôt!')

@dp.message_handler(regexp='🇪🇸 Español')
async def spanish(message: types.Message):
    await message.answer('👉 ¡Características próximamente!')
    



# Define the search command
@dp.message_handler(regexp='🔍 Search') 
async def search(message: types.Message):
    # Prompt user to enter search query
    await message.answer("Enter a movie or TV show name to search for:")

    # Register handler for the user's search query
    @dp.message_handler(lambda message: message.text)
    async def search_handler(message: types.Message):
        query = message.text.strip()
        if not query:
            return

        # Call the search_movies function and send the results back to the user
        results = search_movies(query)
        await message.answer(results)

    # Set the handler to only respond to the user who initiated the command
    await dp.current_state(user=message.from_user.id).set_state("search")
    await dp.current_state(user=message.from_user.id).update_data(regexp='🔍 Search')
    await dp.register_next_step_handler(message, search_handler)

async def search_movies(query):
    api_key = 'aa987a7052db48e0194a06791c4e979e' # Replace with your own API key
    url = f'https://api.themoviedb.org/3/search/multi?api_key={api_key}&query={query}'
    response = requests.get(url)
    results = response.json().get('results', [])

    if len(results) == 0:
        return 'Sorry, no results found.'
    
    elif len(results) == 1:
        result = results[0]
        return result
    else:
        message = "Multiple search results found:\n"
        for i, result in enumerate(results):
            title = result.get("title", result.get("name", ""))
            media_type = result.get("media_type", "")
            return f"{i+1}. {title} ({media_type})\n"
        message += "Please choose a result by typing /choose <number>."
        time.sleep(10)
        return message


# Run the bot
if __name__ == "__main__":
    executor.start_polling(dp)