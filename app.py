import os
from logging.config import dictConfig
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

dictConfig({
    'version': 1,
    'formatters': {'default': {
        # 'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        'format': '%(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        # 'level': 'INFO',
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)
APP_SETTINGS = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
app.config.from_object(APP_SETTINGS)

LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', 'aaa')
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET', 'bbb')

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@app.route('/')
def hello_world():
    return 'hello world!'


@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    app.logger.info('handle_message: ' + event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == '__main__':
    app.run()

