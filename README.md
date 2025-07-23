# Description
This is a border expanding plugin made for Roman @ihavenoeyebrows to use for his Hardcore Captive Minecraft gameplay.

# Prerequisites for the Plugin
You need to download the following:
Java 21 - https://adoptium.net/en-GB/temurin/releases (once downloaded, open the file and follow the Setup Wizard instructions)

# Instructions (for everytime you need to start a new world)
1. Download the zip file and extract all.
2. Load up a new minecraft world in 1.21.8 (newest version). (you are going to have to do this everytime you die)
3. Press windows button and search %appdata%, and go into minecraft, followed by saves.
4. Find the folder of your world and copy that folder.
5. Paste this world's folder into the unzipped file.
6. (Ignore this if it is your first world using this plugin) If there is already a world in the unzipped file because you died, delete everything besides the listed folders/files: eula.txt, plugins folder, paper.jar
7. Now you should have eula.txt, plugins folder, paper.jar, and your new Minecraft world's folder in this MinecraftServer (unzipped) folder.
8. Press windows button and type in cmd then press enter (your Command Prompt should pop up)
9. In the command prompt, if it says something like C:\Users\roman, you need to change directory (folder) until it says something like \MinecraftServer at the end.
10. To do this, use the commands and press enter after each command: cd Downloads, cd MinecraftServer (depends on where your MinecraftServer unzipped folder is.
11. Finally, to boot up the server, type in the exact command: java -jar paper.jar
12. Boot up minecraft and go to multiplayer, and add server: server address is localhost
13. Once the server has booted up, you should be able to join. Enjoy!

# Commands (for everytime you need to start a new world)
1. /teleport -> teleports you to a random spot in the world
2. /startborder -> sets up the 3x3 border at the beginning (do once you found a good spot to start)

# Prerequisites for the Twitch Part
You need to download the following:
1. Python (if you don't have already) - https://www.python.org/downloads/

# Twitch Instructions
1. Download the python file.
2. Open the python file and make sure you edit the following variables: CLIENT_ID, CLIENT_SECRET, STREAMER_LOGIN
3. To figure out what to edit the variables to, you must open Twitch Developer Console and register for an application: name can be whatever, OAuth Redirect URL should be http://localhost:17563, category should be Website Integration, Client Type is Confidential. 
4. Once you finish it, save it and then go back in your applications to find the Client ID and Client_Secret, streamer login is just your username on twitch.
5. Lastly, just make sure this python file is in your downloads folder along with the MinecraftServer folder. 
6. Open up a second command prompt while the other one is running and cd until you get to Downloads, then just type in: python twitch.py
