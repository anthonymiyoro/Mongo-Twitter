import os
from dotenv import load_dotenv

load_dotenv()


# class QueryAndExportMongoDBToCSV:
#     def query_and_export(self, db_name, collection_name, president_name, export_location):
        
#         query_string = ("mongoexport --db=" + str(db_name) +" --collection=" + str(collection_name) + ''' --type=csv --fields=Datetime,Text,Username --query='{ "Text": {"$regularExpression":{"pattern": ''' + '"' + str(president_name) + '"' + "," +''' "options":""}}}' --out=data/''' + str(export_location))
#         print (query_string)
        
#         # os.system('''mongoexport --db=''' + str(db_name) +'''--collection=''' + str(collection_name) + '''--type=csv --fields=Datetime,Text,Username --query='{ "Text": {"$regularExpression":{"pattern":''' + str(president_name) + ''', "options":""}}}' --out=data/''' + str(export_location) +''')
        
#         #os.system('''mongoexport --db=tweets_db --collection=trump_biden_tweets --type=csv --fields=Datetime,Text,Username --query='{ "Text": {"$regularExpression":{"pattern":"biden", "options":""}}}' --out=data/exported_biden_tweets.csv ''')
        
# q = QueryAndExportMongoDBToCSV()
# q.query_and_export((os.environ.get('MONGO_DB_DATABASE_NAME')), (os.environ.get('MONGO_DB_COLLECTION_NAME')), "trump", "data/exported_trump_tweets.csv")
# q.query_and_export((os.environ.get('MONGO_DB_DATABASE_NAME')), (os.environ.get('MONGO_DB_COLLECTION_NAME')), "biden", "data/exported_biden_tweets.csv")


class QueryAndExportMongoDBToCSV:
    def query_and_export(self, db_name, collection_name, president_name, export_location):
        
        query_string = ("mongoexport --db=" + str(db_name) +" --collection=" + str(collection_name) + ''' --type=csv --fields=Datetime,Text,Username --query='{ "Text": {"$regularExpression":{"pattern": ''' + '"' + str(president_name) + '"' + "," +''' "options":""}}}' --out=data/''' + str(export_location))
        print (query_string)
        
        os.system(query_string)
        
q = QueryAndExportMongoDBToCSV()
q.query_and_export((os.environ.get('MONGO_DB_DATABASE_NAME')), (os.environ.get('MONGO_DB_COLLECTION_NAME')), "trump", "data/exported_trump_tweets.csv")
q.query_and_export((os.environ.get('MONGO_DB_DATABASE_NAME')), (os.environ.get('MONGO_DB_COLLECTION_NAME')), "biden", "data/exported_biden_tweets.csv")