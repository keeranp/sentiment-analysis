import os
import tweepy as tw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from dotenv import load_dotenv
load_dotenv()

bearer_token = os.getenv("bearer_token")

client = tw.Client(bearer_token)

hashtag = "#FRAPOL -is:retweet"
tweets = client.search_recent_tweets(query=hashtag,tweet_fields=['created_at'])
tweets = [{"Tweets": tweet.text, "Timestamp": tweet.created_at} for tweet in tweets.data]
print(tweets)
