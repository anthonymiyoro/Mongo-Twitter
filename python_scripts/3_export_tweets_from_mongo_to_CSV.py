from dotenv import load_dotenv

load_dotenv()
import os


class QueryAndExportMongoDBToCSV:
    def query_and_export(self, db_url, db_port,db_name, collection_name, president_name, export_location):
        
        query_string = ("mongoexport --uri=" + '"'+ str(db_url) + '"' + " --port=" +str(db_port)+" --db=" + str(db_name) +" --collection=" + str(collection_name) + ''' --type=csv --fields=Datetime,Text,Username --query='{ "Text": {"$regularExpression":{"pattern": ''' + '"' + str(president_name) + '"' + "," +''' "options":""}}}' --out=data/''' + str(export_location))
        print (query_string)
        
        os.system(query_string)
        
q = QueryAndExportMongoDBToCSV()
q.query_and_export((os.environ.get('MONGO_DB_URL')),(os.environ.get('MONGO_DB_PORT')),(os.environ.get('MONGO_DB_DATABASE_NAME')), (os.environ.get('MONGO_DB_COLLECTION_NAME')), "trump", "data/exported_trump_tweets.csv")
q.query_and_export((os.environ.get('MONGO_DB_URL')),(os.environ.get('MONGO_DB_PORT')),(os.environ.get('MONGO_DB_DATABASE_NAME')), (os.environ.get('MONGO_DB_COLLECTION_NAME')), "biden", "data/exported_biden_tweets.csv")