# Chad MC host

## About
This is the flask server that the Minecraft mod ChadMC uses to send and receive data to a Google Gemini chatbot

## Setup (NOT READY). MacOS/Windows not currently supported
### For Linux
run `apt install -y python-is-python3 python3.10-venv`

Download/clone the hosting branch

Run the setup script via `sudo sh setup.sh`.\
This will copy files to /usr/local/gemini-mc and create an env file and a venv.

In the `.env` file create a new entry `GEMINI_KEY=[KEY]` and replace `[KEY]` with your Gemini API key

To start the server run `sudo sh start.sh`.\
To stop the server run `sudo sh stop.sh`

## Update
To update the server simply pull the GitHub repo. Easiest way to do this is with the GitHub CLI using\
`gh repo sync`\
If git or the GitHub CLI complain delete the folder and re-clone the repo.