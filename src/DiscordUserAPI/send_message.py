import requests


def send_message(token, channel_id, content):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
    payload = {'content': content}
    header = {"authorization": token}

    request = requests.post(url, data=payload, headers=header)

    if request.status_code != 200:
        if request.status_code == 404:
            print('{}: Channel not found'.format(request.status_code))
        else:
            print(request.status_code)
