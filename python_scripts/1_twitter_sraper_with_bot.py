# importing libraries and packages
import os
import snscrape.modules.twitter as sntwitter
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

class TwitterBotScraper:
    def create_dataset(self, output_file_path, hashtag_phrase_list,number_of_tweets_to_download):
        
        """Input: Collects search items and Output file details 
        Output: CSV file with tweets matching input details
        

        Args:
            hashtag_phrase_list (list): List of Hashtags to search for using the API
            number_of_tweets_to_download (integer): Maximum number of tweets to download for each search phrase
        """
        # Creating list to append tweet data to
        tweets_list2 = []
        
        
        for hashtag in hashtag_phrase_list:
            # Using TwitterSearchScraper to scrape data and append tweets to list
            for i,tweet in enumerate(sntwitter.TwitterSearchScraper(hashtag + ' ' + os.environ.get('TWITTER_SEARCH_FROM_DATE')).get_items()):
                # pprint(tweet)
                if i>int(number_of_tweets_to_download):
                    break
                tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.username])

            print ( i, " tweets collecgted.")   
            # Creating a dataframe from the tweets list above
            tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

            tweets_df_looong = tweets_df2

            # Write tweets to CSV file
            tweets_df_looong.to_csv((output_file_path), index=False)
            
t = TwitterBotScraper
t.create_dataset(os.environ.get('CSV_WRITE_PATH'), os.environ.get('TWITTER_SEARCH_LIST'), os.environ.get('NUMBER_OF_TWEETS_TO_DOWNLOAD'))