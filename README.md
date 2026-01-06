# Description
This is a border expanding plugin made for Roman @ihavenoeyebrows to use for his Hardcore Captive Minecraft gameplay.

# Prerequisites for the Plugin
You need to download the following:
1. Java 21 - https://adoptium.net/en-GB/temurin/releases (once downloaded, open the file and follow the Setup Wizard instructions)
2. Paper Minecraft Server - https://papermc.io/downloads/paper

# Instructions (for everytime you need to start a new world)
1. Download the jar file.
2. Make a folder in Downloads called Captive.
3. Drag twitch.py and the BorderExpand-1.0.jar file into the Captive folder.
4. Rename the paper download to paper.
5. Insert paper.jar into the Captive folder as well (you should have twitch.py, the border expand jar, and the paper.jar).
6. Make a new folder inside Captive called plugins and drag BorderExpand-1.0.jar into plugins.
7. Run the following command after opening command prompt: cd Downloads && cd Captive && java -jar paper.jar
8. If asked to agree to eula, open eula.txt and change false to true (then save) and do java -jar paper.jar afterwards in command prompt (ignore if eula.txt is already true). 
9. Boot up minecraft and go to multiplayer, and add server: server address is localhost
10. Once the server has booted up, you should be able to join. Enjoy!
11. (P.S, if you die delete all files besides eula.txt, plugins folder (you have to delete everything besides the BorderExpand jar file inside that folder), and paper.jar)

# Commands (for everytime you need to start a new world)
1. /teleport -> teleports you to a random spot in the world
2. /startborder -> sets up the 1x1 border at the beginning (do once you found a good spot to start)
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
