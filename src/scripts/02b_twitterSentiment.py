import tweepy
from textblob import TextBlob as tb
import csv

consumer_key = "QfNCetLHJSayC8yC8YEbIQ8pd"
consumer_secret = "haORWdlWc79Vnm7OAlWgqRnXdMd7hUweoiKa03PHNXUJBaUmfX"

access_token = "2998870596-7SM8anbzPdxoDTRkBYpWC1l5Xw05N24MxTestiN"
access_token_secret = "LIxHQN42evo7Ch83CS6x7jIjrDSvoYyjBjDkuaMFa4RWN"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


with open("02c_twitterSentiment.csv", "w", newline="") as csvfile:
    tweetWriter = csv.writer(csvfile, delimiter=" ",
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)

    public_tweets = api.search("trump", "eng")

    for tweet in public_tweets:
        inputText = tweet.text
        print(inputText)

        tweetWriter.writerow(inputText)

        #analysis = tb(tweet.text)
        #print(analysis.sentiment)

