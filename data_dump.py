import pymongo

import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME="airPressureSensor"
COLLECTION_NAME="sensor"

import pandas as pd

#File path
DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    #To check dataframe rows and columns
    print(f"Rows and Columns: {df.shape}")

    #To convert dataframe to json so that we can dump these records in MongoDB
    #Dropping index from df
    #import json (at the top)
    df.reset_index(drop=True, inplace=True)

    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #Insert converted json record in mongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)