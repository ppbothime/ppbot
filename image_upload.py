import os
import requests
import tweepy
from dotenv import load_dotenv

# Load the .env file into environment variables
load_dotenv()

from auth import *

class ImageTweet(object):

    def __init__(self, filename):
		
        '''
        Defines image tweet properties
        '''
        self.image_filename = filename

    def tweet(self):
        '''
        Publishes Tweet with attached image
        '''
        image_path = self.image_filename
        print(image_path)
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_secret = os.getenv('CONSUMER_SECRET')
        access_token = os.getenv('ACCESS_TOKEN')
        access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

        client = tweepy.Client(
            consumer_key=consumer_key, consumer_secret=consumer_secret,
            access_token=access_token, access_token_secret=access_token_secret
        )

        auth = tweepy.OAuth1UserHandler(
            consumer_key, consumer_secret, access_token, access_token_secret
        )
        api = tweepy.API(auth)

        media = api.media_upload(filename=image_path)

        # Create Tweet with media
        response = client.create_tweet(
            text=image_path.split('.')[0],
            media_ids=[media.media_id],
        )
        print(f"https://twitter.com/user/status/{response.data['id']}")
        os.remove(self.image_filename)