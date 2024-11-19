# Chad MC host

## About
This is the flask server that the Minecraft mod ChadMC uses to send and receive data to a Google Gemini chatbot

## Setup
### For Windows
TBD

### For Linux
Run the setup script via `sudo sh setup.sh`.\
This will create a python virtual environment, install the required packages, and copy a service file to `/etc/systemd/system` and enable the service. 

In the `.env` file create a new entry `GEMINI_KEY=[KEY]` and replace `[KEY]` with your Gemini API key

To start the server run `sudo sh start.sh`.\
To stop the server run `sudo sh stop.sh`

## Update
To update the server simply pull the GitHub repo. Easiest way to do this is with the GitHub CLI using\
`gh repo sync`\
If git or the GitHub CLI complain delete the folder and re-clone the repo.