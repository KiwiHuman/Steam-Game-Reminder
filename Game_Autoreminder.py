#General setup
import time
from datetime import datetime

#Steam setup
import requests

from Config import user_id
from Config import api_key
from Config import Game_app_id


def GetGameName(app_id, api_key):

    url = f'http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key={api_key}&appid={app_id}'

    response = requests.get(url)
    data = response.json()

    # Extract the name of the game from the JSON response
    game_name = data['game']['gameName']

    return (game_name)


#Email setup
from email.message import EmailMessage
import ssl 
import smtplib

from Config import email_sender
from Config import email_password
from Config import email_recipient


Game_Name = GetGameName(Game_app_id, api_key)

Subject = f'{Game_Name} Reminder'
body = f'''
It has Been 48 Hours or more since you last played {Game_Name}, You should consider Playing again soon.
'''
em = EmailMessage()
em['From'] = email_sender
em['To'] =  email_recipient
em['subject'] = Subject
em.set_content(body)

context = ssl.create_default_context()

# Function Definition
def get_time_since_last_played(api_key, user_id, app_id):
    # URL for the GetOwnedGames endpoint
    url = f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={user_id}&format=json'

    # Make the request to get the list of owned games
    response = requests.get(url)
    data = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        print("API request Success")
        # Find the specified app_id in the user's game list
        game_info = next((game for game in data['response']['games'] if game['appid'] == app_id), None)

        if game_info:
            # Extract the last played timestamp
            last_played_timestamp = game_info.get('rtime_last_played')

            if last_played_timestamp is not None:
                print(f"{Game_Name} timestamp success")
                # Calculate the time since last played
                current_timestamp = datetime.now().timestamp()
                time_since_last_played = current_timestamp - last_played_timestamp
                print(f'time since last played ={time_since_last_played}')
                return time_since_last_played
            else:
                return None
        else:
            print(f"User does not own the game with app_id {app_id}")
            return None
    else:
        print(f"Error getting game list: {data.get('error', 'Unknown error')}")
        return None

def Email_Notify():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_recipient ,em.as_string())


#Program Start
while True:
    time_since_last_played = get_time_since_last_played(api_key, user_id, Game_app_id)
    if time_since_last_played >= 172800:
        while time_since_last_played >= 172800:
            Email_Notify()
            print('Sending Email')
            time.sleep(86400)
            time_since_last_played = get_time_since_last_played(api_key, user_id, Game_app_id)
    else:
        print(f'played in the last 48h checking again in {172800 - time_since_last_played} seconds')
        time.sleep(172800 - time_since_last_played)



