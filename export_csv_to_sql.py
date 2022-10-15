from logging import exception
import pandas as pd
from sqlalchemy import create_engine

csv_location = "biden_mongo.csv" # Replace with any csv containing transformed tweets

engine = create_engine('sqlite://', echo=False)
 
with engine.begin() as connection:
    df = pd.read_csv(csv_location)
    df.to_sql('biden_tweets', con=engine, if_exists="append")
    
    print ("SQL executed successfully!")
try:
    print(engine.execute("SELECT * FROM biden_tweets").fetchall())
except exception as e:
    print ("e ", e)

