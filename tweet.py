import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session


def tweet(a,b):
    

    CONSUMER_KEY = os.environ["CONSUMER_KEY"]
    CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]
    
    url = "https://api.twitter.com/1.1/statuses/update.json"
    twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    tweet = a+" "+b #ツイート内容
    
    params = {"status" : tweet}

    req = twitter.post(url, params = params) #ここでツイート

    if req.status_code == 200: #成功
        print("Succeed!")
    else: #エラー
        print("ERROR : %d"% req.status_code) 
