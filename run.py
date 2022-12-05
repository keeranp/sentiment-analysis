import os
import tweepy as tw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("api_key")
api_secret = os.getenv("api_key_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

auth = tw.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
