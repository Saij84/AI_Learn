import os
import csv
import tweepy
from textblob import TextBlob as tb


consumer_key = os.environ["TW_CONSUMER_KEY"]
consumer_secret = os.environ["TW_CONSUMER_SECRET"]
access_token = os.environ["TW_ACCESS_TOKEN"]
access_token_secret = os.environ["TW_ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# with open("02c_twitterSentiment.csv", "w", newline="") as csvfile:
#     tweetWriter = csv.writer(csvfile, delimiter=" ",
#                              quotechar='|', quoting=csv.QUOTE_MINIMAL)

def getTweet(quary):
    """
    :param quary: what to search for : type->str
    :return: return tweets
    """
    public_tweets = api.search(q=quary, count=100)

    if not public_tweets:
        pass


    for tweet in public_tweets:
        inputText = tweet.text
        print(inputText)

        #analysis = tb(tweet.text)
        #print(analysis.sentiment)

getTweet("Trains")