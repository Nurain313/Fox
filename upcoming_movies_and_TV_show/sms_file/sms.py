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
tv_show_file_dir = os.path.join(parent_dir, 'tv_show_file')
Ids_dir = os.path.join(parent_dir, 'sms_file')

# JSON file paths
movie_file =os.path.join(movie_file_dir, 'upcoming_movies.json')
tv_show_file = os.path.join(tv_show_file_dir, 'upcoming_tv_shows.json')

# Text file to keep track of IDs in the JSON files
id_file = os.path.join (Ids_dir, 'id_file.txt') 

print ("sms has started........ ")

# Function to send an SMS via Twilio
def send_sms():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="The Database has been updated.",
        from_=twilio_number,
        to=destination_number
    )
    print("SMS sent:", message.sid)
    
def send_sms_no():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="No new updates found, database upto date",
        from_=twilio_number,
        to=destination_number
    )
    print("SMS sent:", message.sid)

# Check if the ID file exists, if not create it
if not os.path.exists(id_file):
    with open(id_file, "w") as f:
        f.write("")

# Read the last IDs from the ID file
with open(id_file, "r") as f:
    last_ids = f.read().splitlines()

# Read the current IDs from the movie JSON file
with open(movie_file, "r") as f:
    movie_data = json.load(f)
    current_ids = [str(movie["id"]) for movie in movie_data]

# Read the current IDs from the TV show JSON file
with open(tv_show_file, "r") as f:
    tv_show_data = json.load(f)
    current_ids += [str(tv_show["id"]) for tv_show in tv_show_data]

# Compare the current IDs to the last IDs
if set(current_ids) != set(last_ids):
    # Update the ID file with the current IDs
    with open(id_file, "w") as f:
        f.write("\n".join(current_ids))

    # Send an SMS via Twilio
    send_sms()
else:
  print ("No new updates found, database upto date")
  # Send an SMS via Twilio
  send_sms_no()
    
    
print ("sms complete ")

