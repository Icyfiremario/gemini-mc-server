# Chad MC host

## About
This is the flask server that the Minecraft mod ChadMC uses to send and receive data to a Google Gemini chatbot

## Setup. MacOS/Windows not currently supported
### For Linux
install the dependencies with `apt install -y python-is-python3 python3.10-venv`

Clone the repo:\
With git: `git clone https://github.com/icyfiremario/gemini-mc-server` \
With gh: `gh repo clone icyfiremario/gemini-mc-server` 

Open the cloned folder and checkout to the hosting branch with `git checkout hosting`

Run the setup script via `sudo sh setup.sh`.\
This will copy files to /usr/local/gemini-mc and create a virtual environment and open an .env file

In the `.env` file create a new entry `GEMINI_KEY=[KEY]` and replace `[KEY]` with your Gemini API key

Use ctrl+x to close and save the file

To start the server run `sudo sh start.sh`.\
To stop the server run `sudo sh stop.sh`

## Update
To update the server simply pull the GitHub repo. Easiest way to do this is with the GitHub CLI using\
`gh repo sync`\
If git or the GitHub CLI complain delete the folder and re-clone checkout the hosting branch and re-run `setup.sh`.
