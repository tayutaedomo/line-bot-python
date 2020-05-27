# line-bot-python
Try line-bot-sdk with Python

## Reference
- https://qiita.com/shimajiri/items/cf7ccf69d184fdb2fb26

## Setup
```
$ git clone https://github.com/tayutaedomo/line-bot-python
$ cd line-bot-python
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## ENV
You have to set the following.
```
$ export LINE_CHANNEL_ACCESS_TOKEN=<YOUR_CHANNEL_ACCESS_TOKEN>
$ export LINE_CHANNEL_SECRET=<YOUR_CHANNEL_SECRET>
```

You should set the appropriate ENV of config.
```
$ export APP_SETTINGS="config.DevelopmentConfig"
# or
$ export APP_SETTINGS=config.StagingConfig
# or
$ export APP_SETTINGS=config.ProductionConfig
```

## Local Server
```
$ cd line-bot-python
$ python app.py
$ open "http://127.0.0.1:5000/"
```

