from logging import exception
from pymongo import MongoClient
import os, csv
from dotenv import load_dotenv

load_dotenv()


def mongoimport(csv_path, db_name, coll_name, db_url='localhost', db_port=27017):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documants in the new collection
    """
    client = MongoClient(db_url, db_port)
    
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
        print ("CSV FILE " + os.environ.get('CSV_READ_PATH') + " DOES NOT EXIST!!!")
        return (exception("ERROR"))
        
    

mongoimport(os.environ.get('CSV_READ_PATH'), os.environ.get('DB_NAME'), os.environ.get('COLLECTION_NAME'), db_url='localhost', db_port=27017)
