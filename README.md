# Description
This is a border expanding plugin made for Roman @ihavenoeyebrows to use for his Hardcore Captive Minecraft gameplay.

# Prerequisites for the Plugin
You need to download the following:
Java 21 - https://adoptium.net/en-GB/temurin/releases (once downloaded, open the file and follow the Setup Wizard instructions)

# Instructions (for everytime you need to start a new world)
1. Download the zip file and extract all.
2. Press windows button and type in cmd then press enter (your Command Prompt should pop up)
3. In the command prompt, if it says something like C:\Users\roman, you need to change directory (folder) until it says something like \MinecraftServer at the end.
4. To do this, use the commands and press enter after each command: cd Downloads, cd MinecraftServer (depends on where your MinecraftServer unzipped folder is.
5. Finally, to boot up the server, type in the exact command: java -jar paper.jar
6. Boot up minecraft and go to multiplayer, and add server: server address is localhost
7. Once the server has booted up, you should be able to join. Enjoy!
8. (P.S, if you die delete all files besides eula.txt, plugins folder (you have to delete everything besides the BorderExpand jar file inside that folder), and paper.jar)

# Commands (for everytime you need to start a new world)
1. /teleport -> teleports you to a random spot in the world
2. /startborder -> sets up the 3x3 border at the beginning (do once you found a good spot to start)
3. /borderstats -> shows a list of what expanded the border and by how much

# Prerequisites for the Twitch Part
You need to download the following:
1. Python (if you don't have already) - https://www.python.org/downloads/

# Twitch Instructions
1. Find the python file inside the MinecraftServer folder.
2. Run the following command in your Command Prompt once you are inside the Minecraft Server folder: pip install twitchAPI 
3. Open the python file and make sure you edit the following variables: CLIENT_ID, CLIENT_SECRET, STREAMER_LOGIN
4. To figure out what to edit the variables to, you must open Twitch Developer Console and register for an application: name can be whatever, OAuth Redirect URL should be http://localhost:17563, category should be Website Integration, Client Type is Confidential. 
5. Once you finish it, save it and then go back in your applications to find the Client ID and Client_Secret, streamer login is just your username on twitch.
6. Lastly, just make sure this python file is in your downloads folder along with the MinecraftServer folder. 
7. Open up a second command prompt while the other one is running and cd until you get to MinecraftServer, then just type in: python twitch.py
