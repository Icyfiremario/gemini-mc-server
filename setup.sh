python -m venv ./.venv
./.venv/bin/python -m pip install -r requirements.txt
touch .env
cp chad-mc.service /etc/systemd/system/chad-mc.service
systemctl enable chad-mc.service