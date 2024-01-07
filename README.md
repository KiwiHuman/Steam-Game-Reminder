# Steam-Game-Reminder
To get started with Steam Game Reminder clone the repo and setup a venv in the Project folder. 
```
git clone https://github.com/KiwiHuman/Steam-Game-Reminder
cd Steam-Game-Reminder
python3 -m venv .
source ./bin/activate
```
Then install the requierments 
```
pip install --upgrade -r Requirements.txt
```

Edit the config using a text editor of your choice

```
nano Example_Config.py
```
Replace `Steam API Key` with your Steam API key

Replace `Your User ID` with your steam user ID (this can be found by visiting https://steamcommunity.com/ and searching your username in the "search for freinds" box after clicking on yourself your steam user ID can be found in the URL. For example on my profile https://steamcommunity.com/profiles/76561199084170401 my steam user ID is 76561199084170401

Replace the number after `Game_app_id = ` with the app id of the game you want to be notified of. You can find the app ID by visiting https://steamdb.info/ and searching for the game. 

