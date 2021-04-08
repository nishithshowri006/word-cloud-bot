import tweepy
from dotenv import load_dotenv
import os
import pandas as pd
CONSUMER_KEY = os.getenv("API_KEY")
CONSUMER_SECRET = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

def get_tweet_list(api:tweepy.API,username:str) -> list:
    """
    This returns list of tweets for the given username.
    """
    pass

def make_df(tweets_list:list) ->pd.DataFrame:
    """
    This takes a list and return the dataframe that is 
    required for the word cloud.
    """
    pass

def get_saved_image(df:pd.DataFrame):
    """
    Okay I am assuming we call the word cloud start here.
    """
    pass

def reply(api:tweepy.API, image:bytes):
    """
    I am assuming here is where when the bot is mentioned 
    it replies with the image.
    """
    pass

def main():
    """
    Authentication and calling the helper function
    """
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
