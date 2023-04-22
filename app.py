import requests

from image_upload import ImageTweet
from utilities import *

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

def tweet():

    file = getRandomFile()

    if file['extension'] == 'png':
        imageTweet = ImageTweet(file['title'])
        imageTweet.tweet()

def ping():

    try:
        r = requests.head("render website")
        print(r.status_code)

    except requests.ConnectionError:
        print("failed to connect")

scheduler.add_job(tweet, 'interval', seconds=840)
scheduler.add_job(ping, 'interval', seconds=7200)
scheduler.start()

if __name__ == '__main__':
    app.run()