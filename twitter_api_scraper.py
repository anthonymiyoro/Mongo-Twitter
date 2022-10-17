import os
import tweepy, csv
from dotenv import load_dotenv
from pprint import pprint
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

consumer_key = os.environ.get("API_KEY")
consumer_secret = os.environ.get("API_KEY_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
search_query = os.environ.get("TWITTER_SEARCH_STRING")
number_of_tweets_to_download = os.environ.get("NUMBER_OF_TWEETS_TO_DOWNLOAD")

class TwitterScraper:  
    def create_dataset(self, consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase,number_of_tweets_to_download):
        
        # Twitter authentication and the connection to Twitter API
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        # Initializing Tweepy API
        api = tweepy.API(auth, wait_on_rate_limit=True)
        
        # Name of csv file to be created
        fname = "dataset"
        
        # Open the spreadsheet
        with open('%s.csv' % (fname), 'w', encoding="utf-8") as file:
            w = csv.writer(file)
            
            # Write header row (feature column names of your choice)
            w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'location', 
                        'followers_count', 'retweet_count', 'favorite_count'])
            
            # For each tweet matching hashtag, write relevant info to the spreadsheet
            for tweet in tweepy.Cursor(api.search_tweets, q=hashtag_phrase+' -filter:retweets', lang="en", tweet_mode='extended').items(int(number_of_tweets_to_download)):
                w.writerow([tweet.created_at, 
                            tweet.full_text.replace('\n',' ').encode('utf-8'), 
                            tweet.user.screen_name.encode('utf-8'), 
                            [e['text'] for e in tweet._json['entities']['hashtags']],  
                            tweet.user.location, 
                            tweet.user.followers_count, 
                            tweet.retweet_count, 
                            tweet.favorite_count])

    # Enter your hashtag here
    hashtag_phrase= ""
            
            
t = TwitterScraper()
t.create_dataset(consumer_key, consumer_secret,access_token,  access_token_secret, search_query, number_of_tweets_to_download)