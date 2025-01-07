mkdir /usr/local/gemini-mc
cp main.py /usr/local/gemini-mc/main.py
cp chad.py /usr/local/gemini-mc/chad.py

python -m venv /usr/local/gemini-mc/.venv
/usr/local/gemini-mc/.venv/bin/python -m pip install -r requirements.txt

touch /usr/local/gemini-mc/.env
nano /usr/local/gemini-mc/.env

cp chad-mc.service /etc/systemd/system/chad-mc.service
systemctl enable chad-mc.service