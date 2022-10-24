import os
from logging import exception
import pandas as pd
from sqlalchemy import create_engine

from dotenv import load_dotenv

load_dotenv()

class ExportCSVToSQL:
    def export_csv_to_sql(self, csv_locations_list):
        """input: list of csv locations
        output: results of a select query on all the tweets saved to the default SQLite DB

        Args:
            csv_locations_list (list): list of CSV files containing tweets on specific topics
        """

        # csv_location = "biden_mongo.csv" # Replace with any csv containing transformed tweets
        for csv_location in csv_locations_list:

            engine = create_engine('sqlite://', echo=False)
            
            with engine.begin() as connection:
                df = pd.read_csv(csv_location)
                df.to_sql('biden_tweets', con=engine, if_exists="append")
                
                print ("SQL executed successfully!")
            try:
                print(engine.execute("SELECT * FROM biden_tweets").fetchall())
            except exception as e:
                print ("ERROR: ", e)

csv_locations_list = [(os.environ.get('EXPORTED_TRUMP_TWEETS_CSV_LOCATION')),(os.environ.get('EXPORTED_BIDEN_TWEETS_CSV_LOCATION'))]
e = ExportCSVToSQL()
e.export_csv_to_sql(csv_locations_list)
