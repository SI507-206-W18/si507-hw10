import sqlite3

DB_NAME = 'tweets.sqlite'

try:
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
except Error as e:
    print(e)

def get_most_retweeted_tweet():
    #prints the tweet with the most number of retweets (just tweet text will do)

def get_most_followed_user():
    #print the user’s screen name who is most followed

def get_most_retweeted_user():
    #print the user’s screen name who’s tweet had the highest retweet count

def get_tweets_from_most_followed():
    #print the 5 tweets that belong to authors with highest number of followers. Order this in the the descending order.

def get_trending_location():
    #print the top 5 locations that are tweeting about us/ Going Blue. Order in the descending order.


get_most_retweeted_tweet()
get_tweets_from_most_followed()
get_most_followed_user()
get_most_retweeted_user()
get_trending_location()
