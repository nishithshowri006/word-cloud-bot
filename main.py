import tweepy
from dotenv import load_dotenv
import os
import pandas as pd
from tweepy.streaming import Stream, StreamListener
load_dotenv()
CONSUMER_KEY = os.getenv("API_KEY")
CONSUMER_SECRET = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")


class MyListner(StreamListener):

    def on_status(self, status):
        print(status.__dir__())
        return "nishith" 

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
        print(f"{len(tweet_list)} tweets are loaded so far")
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
    # listner = MyListner()
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
    # stream = Stream(auth,listner)
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    main_user = api.get_user(screen_name="corner1705").id
    # ans = stream.filter(follow=[f"{main_user}"],track=["word cloud","word-cloud"],is_async=True)
    
    # print(ans)
    tweet_list = get_tweet_list(api,"corner1705")
    df = make_df(tweet_list)
    # image = get_saved_image(df)

if __name__=="__main__":
    main()