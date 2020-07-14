import sys
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

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

    line_bot_api = LineBotApi(channel_access_token)

    try:
        line_bot_api.push_message(user_id, TextSendMessage(text=text))
    except LineBotApiError as e:
        print(e)

