from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

from twitterAPIKeys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


def percentage(part, whole):
    return 100 * float(part)/float(whole)



consumerKey = CONSUMER_KEY
consumerSecret = CONSUMER_SECRET
accessToken = ACCESS_TOKEN
accessTokenSecret = ACCESS_TOKEN_SECRET

print(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

print("Connected to Twitter API")

searchTerm = input("Enter keyword/hashtag to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))



tweets = tweepy.Cursor(api.search, q=searchTerm, lang="de").items(noOfSearchTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)