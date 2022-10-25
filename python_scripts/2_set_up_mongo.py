from logging import exception
from pymongo import MongoClient
import os, csv

from dotenv import load_dotenv

load_dotenv()

class SetUpMongoDB:
    def mongoimport(self, csv_path, db_name, coll_name, db_url=os.environ.get('MONGO_DB_URL'), db_port=os.environ.get('MONGO_DB_PORT')):
        """ Imports a csv file from path csv_name to a new or existing mongo DataBase named db_name
            returns: count of the documants in the new collection
        """
        client = MongoClient(db_url, int(db_port))
        
        dbnames = client.list_database_names()
        if db_name not in dbnames:
            # Create a new DB with this name
            db = client[db_name]
        else:
            # Getting the database instance
            db = client[db_name]

        
        # Open CSV file 
        if os.path.exists(csv_path):
            with open(csv_path, 'r') as csvfile:
                header = [ "Datetime",	"Tweet Id",	"Text",	"Username"]
                reader = csv.reader(csvfile)
                for row in reader:
                    doc={}
                    for n in range(0,len(header)):
                        doc[header[n]] = row[n]

                    db.trump_biden_tweets.insert_one(doc)
        else:
            print ("CSV FILE " + os.environ.get('ALL_TWEETS_DATASET') + " DOES NOT EXIST!!!")
            return (exception("ERROR"))
            
    
s = SetUpMongoDB()
s.mongoimport(os.environ.get('ALL_TWEETS_DATASET'), os.environ.get('MONGO_DB_DATABASE_NAME'), os.environ.get('MONGO_DB_COLLECTION_NAME'), db_url=os.environ.get('MONGO_DB_URL'), db_port=os.environ.get('MONGO_DB_PORT'))
