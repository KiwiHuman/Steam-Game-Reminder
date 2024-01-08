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

## Setting up the config file
Edit the example config using a text editor of your choice

```
nano Example_Config.py
```
### Steam Config

Replace `Steam API Key` with your Steam API key

Replace `Your User ID` with your steam user ID (this can be found by visiting https://steamcommunity.com/ and searching your username in the "search for freinds" box after clicking on yourself your steam user ID can be found in the URL. For example on my profile https://steamcommunity.com/profiles/76561199084170401 my steam user ID is 76561199084170401

Replace the number after `Game_app_id = ` with the app id of the game you want to be notified of. You can find the app ID by visiting https://steamdb.info/ and searching for the game. 

### Email Config (for gmail) 

On the Gmail account you want to use to send the email notifications follow [these instructions](https://support.google.com/accounts/answer/185833?hl=en) to genertate and use an app password

in the config file replace `SenderEmail@gmail.com` with the email of the Gmail account used to send the notification emails
replace `YourPassword - Sending email account` with the app password you created earlier
replace `RecipiantEmail@gmail.com` with the email you want to recive the notifications. This can be from any provider Gmail is just an example. 

### Saving the file
save the file as `Config.py` this can be done in nano with `ctrl + x` to exit `Y` to save and under `file name to write` remove `Example_` from the filename

## Testing the program
run `Python3 Game_Autoreminder.py` and after a while you should see an output simaler to the following

```
API request Success
Beat Saber timestamp success
time since last played =324139.53461790085
Sending Email
```
Or 
```
API request Success
Beat Saber timestamp success
time since last played =4.283659934997559
played in the last 48h checking again in 172795.716340065 seconds
```

If you see the output is close to this then you can procede to setup the scrypt to run as a service. 

## Autorunning the scrypt with systemd

Create the file /etc/systemd/system/GameAutoreminder.service using the command
```
sudo touch /etc/systemd/system/GameAutoreminder.service
```
Edit the newly created file using 
```
sudo nano /etc/systemd/system/GameAutoreminder.service
```
in /etc/systemd/system/GameAutoreminder.service input the following. Remember to replace `KiwiHuman' with the user that should run the service.
```
[Unit]
Description=Steam game reminder program] 
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=KiwiHuman
ExecStart=/home/KiwiHuman/Steam-Game-Reminder/bin/python3 /home/KiwiHuman/Steam-Game-Reminder/Game_Autoreminder.py

[Install]
WantedBy=multi-user.target
```
Save and exit the file. now run the following to check the service has been created successfully
```
sudo systemctl status GameAutoreminder
```
the output should show the following. 
```
○ GameAutoreminder.service - Steam game reminder program]
     Loaded: loaded (/etc/systemd/system/GameAutoreminder.service; disabled; preset: enabled)
     Active: inactive (dead)
```
if this is working then run 
```
sudo systemctl enable GameAutoreminder
sudo systemctl start GameAutoreminder
sudo systemctl status GameAutoreminder
```
That should output the following. 
```
KiwiHuman@KiwiHumansServer:~$ sudo systemctl status GameAutoreminder
KiwiHuman@KiwiHumansServer:~$ sudo systemctl enable GameAutoreminder
Created symlink /etc/systemd/system/multi-user.target.wants/GameAutoreminder.service → /etc/systemd/system/GameAutoreminder.service.
KiwiHuman@KiwiHumansServer:~$ sudo systemctl start GameAutoreminder
KiwiHuman@KiwiHumansServer:~$ sudo systemctl status GameAutoreminder
● GameAutoreminder.service - Steam game reminder program]
     Loaded: loaded (/etc/systemd/system/GameAutoreminder.service; enabled; preset: enabled)
     Active: active (running) since Mon 2024-01-08 16:30:28 GMT; 9s ago
   Main PID: 1179 (python3)
      Tasks: 1 (limit: 6950)
     Memory: 16.0M
        CPU: 285ms
     CGroup: /system.slice/GameAutoreminder.service
             └─1179 /home/KiwiHuman/Steam-Game-Reminder/bin/python3 /home/KiwiHuman/Steam-Game-Reminder/Game_Autoreminder.py

Jan 08 16:30:28 KiwiHumansServer systemd[1]: Started GameAutoreminder.service - Steam game reminder program].
```
