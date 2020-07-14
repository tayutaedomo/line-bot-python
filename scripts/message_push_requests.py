import sys
import requests
import json


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Channel access token and user_id are required.')
        print('Usage: python message_push.py "<channel_access_token>" "<user_id>" ')
        sys.exit()

    channel_access_token = sys.argv[1]
    user_id = sys.argv[2]

    text = 'Hello'
    if len(sys.argv) > 3:
        text = sys.argv[3]

    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Authorization': 'Bearer {}'.format(channel_access_token),
        'Content-Type': 'application/json'
    }
    data = {
        'to': user_id,
        'messages': [
            {
                'type': 'text',
                'text': text
            }
        ]
    }

    res = requests.post(url, headers=headers, data=json.dumps(data))
    print(res.text)

