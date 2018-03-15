import tweepy
import json
import sys
import sqlite3
from secrets import *

DB_NAME = 'tweets.sqlite'

def get_tweets(search_term, num_tweets):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=search_term).items(num_tweets)]
    return searched_tweets

def init_db(db_name):
    pass
    #code to create a new database goes here
    #handle exception if connection fails by printing the error

    #code to test whether table already exists goes here
    #if exists, prompt to user: "Table exists. Delete?yes/no"
    #if user input is yes, drop table. Else, use move on and use existing table

    #code to create table(if not exists) goes here

    #close database connection

    #this function is not expected to return anything, you can modify this if you want

def insert_tweet_data(tweets):
    pass
    #add code to connect to database and get a Cursor

    #Uncomment to see our data of interest from the Tweepy Result Set.
    #Comment these print statements when you submit code to us.
    # for tweet in tweets:
    #     print("Tweet ID:", tweet.id)
    #     print("Tweet Text:", tweet.text.encode('utf8'))
    #     print ("Retweet Count:", tweet.retweet_count)
    #     print("User ID:", tweet.user.id)
    #     print("User Screen Name:", tweet.user.screen_name)
    #     print("User Location:", tweet.user.location)
    #     print("User Follower Count:", tweet.user.followers_count)

        #Add code to insert each of these data of interest to the Tweets table

    #Close database connection

    #Not expecting return, you can modify if you wish

if __name__ == "__main__":
    search_term = input("Enter search term: ")
    num_tweets = int(input("Enter number of tweets to retrieve: "))
    #fetch tweets
    tweets =get_tweets(search_term, num_tweets)
    print("Fetched",len(tweets),"tweets")
    #create database and table
    init_db(DB_NAME)
    #insert data into table
    insert_tweet_data(tweets)
