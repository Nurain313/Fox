import json
import os
import time
from twilio.rest import Client

# Set up the Twilio client
account_sid = 'AC18a94259bf3eb65e431a4f581f15cdb3'
auth_token = 'aadf92116b06046f02ca8cc26e530483'
twilio_number = '+15074618480'
destination_number = '+254716905605'
client = Client(account_sid, auth_token)

# Define the path to the upcoming.json file
parent_dir = os.path.dirname(os.getcwd())
movie_file_dir = os.path.join(parent_dir, 'movie_file')
json_file = os.path.join(movie_file_dir, 'upcoming_movies.json')
#with open(json_file_path, 'r') as f:
    #data = json.load(f)

# Define a function to read JSON data from a file
def read_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data

# Define a function to send an SMS
def send_sms(message):
    client.messages.create(
        to=destination_number,
        from_=twilio_number,
        body=message)

# Read the initial JSON data
data = read_json(json_file)

# Extract the movie and TV show titles
titles = {item['title'] for item in data}

# Keep checking the JSON file every 30 seconds
while True:
    # Wait for 30 seconds
    #time.sleep(5)
    print("Sms is checking for updates...")
    
    # Read the current JSON data
    current_data = read_json(json_file)
        
    # Extract the current movie and TV show titles
    current_titles = {item['title'] for item in current_data}
    
    # Check if the titles have changed
    new_titles = current_titles - titles
    if new_titles== True:
        # Create the SMS message
        message= f"New movie/TV show(s) added: {', '.join(new_titles)}"
        
        # Send the SMS message
        send_sms(message)
        
        # Update the titles set
        titles = current_titles
    else:
      
        #Create the SMS message 
        message= 'update checked, no updates found'
        # Send the SMS message
        send_sms(message)
        
        print("No updates found.")

    print("sms sent...")
    time.sleep(12 * 60 * 60)
