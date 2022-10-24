### Commands to find basic tweet info

Before attempting these commands, open your terminal and make sure that you have installed mongosh from [here](https://www.mongodb.com/docs/mongodb-shell/install/#std-label-mdb-shell-install).

```
// Log in to the MongoDB shell
1. mongosh  

// List all DBs and select the DB we will use
2. show dbs 
3. use tweets_db

// List all collections and select the collections we will use
4. show collections;  
5. db.trump_biden_tweets.createIndex({ "Text": "text" });

// Query and print out trump and biden tweets
6. db.trump_biden_tweets.find({$text: {$search: "biden"} });
7. db.trump_biden_tweets.find({$text: {$search: "trump"} });
```