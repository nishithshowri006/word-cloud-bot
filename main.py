import tweepy
from dotenv import load_dotenv
import os
import pandas as pd
from tweepy.streaming import Stream, StreamListener
from word_cloud import *
load_dotenv()
CONSUMER_KEY = os.getenv("API_KEY")
CONSUMER_SECRET = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")


class MyListner(StreamListener):

    def __init__(self, api:tweepy.API):
        super().__init__(api=api) 
        self.api = api
        self.me = api.me()
        self.key_words = ["Word-cloud","word cloud","Word Cloud"]


    def on_status(self, status:tweepy.Status):
        tweet_text = status.text
        flag = any([True if key in tweet_text else False for key in self.key_words])
        screen_name = status.user.screen_name
        tweet_id = status.id_str
        if flag:
            username = status.user.screen_name
            tweet_list = get_tweet_list(api,username)
            df = make_df(tweet_list)
            img = start_cloud(df)
            reply(self.api,tweet_id,img,screen_name)
        

def get_tweet_list(api:tweepy.API,username:str) -> list:
    """
    This returns list of tweets for the given username.
    """
    user_tweets = api.user_timeline(screen_name=username,count=200,include_rts=False,exclude_replies=True)
    tweet_list = []
    tweet_list.extend(user_tweets)
    oldest = tweet_list[-1].id - 1
    while len(user_tweets) > 0:
        user_tweets = api.user_timeline(screen_name=username,max_id=oldest,count=200,include_rts=False,exclude_replies=True)
        tweet_list.extend(user_tweets)
        oldest = tweet_list[-1].id - 1
    result = [str(tweet.text.split("http")[0]) for tweet in tweet_list]
    print("Got the list of tweets")
    return result


def make_df(tweets_list:list) ->pd.DataFrame:
    """
    This takes a list and return the dataframe that is 
    required for the word cloud.
    """
    df = pd.DataFrame(tweets_list,columns=["text"])
    return df

def reply(api:tweepy.API, tweet_id:str, image:str, screen_name:str):
    """
    I am assuming here is where when the bot is mentioned 
    it replies with the image.
    """
    api.update_with_media(status=f"@{screen_name}",filename = image,in_reply_to_status_id_str=tweet_id)
    print("Done")


def main(api:tweepy.API,main_user):
    """
    Authentication and calling the helper function
    """
    listner = MyListner(api)
    stream = Stream(auth,listner)
    ans = stream.filter(follow=[f"{main_user}"],is_async=True)


if __name__=="__main__":
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    main_user = api.get_user(screen_name="corner1705").id_str
    username = "coner1705"
    if username:
        main(api,main_user)
    print("Exited")
