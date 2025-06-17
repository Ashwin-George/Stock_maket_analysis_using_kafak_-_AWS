import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from time import sleep
from json import dumps
import json


import constants
# S3_FILE_PATH=f's3://{S3_BUCKET}/{S3_STORAGE_FILENAME}'
producer = KafkaProducer(bootstrap_servers=[constants.BOOTSTRAP_SERVER],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

# producer.send(constants.KAFKA_TOPIC_NAME,value={'hello':'world'})

df=pd.read_csv('datasets/indexProcessed.csv')
df.head()

while True:
    dict_stock=df.sample(1).to_dict(orient='records')[0]
    producer.send(constants.KAFKA_TOPIC_NAME,value=dict_stock)
    sleep(1)

# producer.flush()