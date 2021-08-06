from src.DiscordUserAPI.send_message import send_message

import json

with open('message.json') as f:
    data = json.load(f)

token = data['token']
channel_id = data['channel_id']
content = data['content']

send_message(token, channel_id, content)
