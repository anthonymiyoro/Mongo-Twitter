# importing libraries and packages
import os
import snscrape.modules.twitter as sntwitter
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

hashtag_string  = "#stopthesteal Trump"
start_date = "since:2019-01-30"

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(hashtag_string + ' ' + start_date).get_items()):
    # pprint(tweet)
    if i>int(os.environ.get('NUMBER_OF_TWEETS_TO_DOWNLOAD')):
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.username])

print ("i", i)   
# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

tweets_df_looong = tweets_df2

# Write tweets to CSV file
tweets_df_looong.to_csv((os.environ.get('CSV_WRITE_PATH')), index=False)