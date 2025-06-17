import pandas as pd
from kafka import KafkaConsumer
from time import sleep
from json import dumps, loads
import constants

import json
from s3fs import S3FileSystem

# S3_FILE_PATH=f's3://{S3_BUCKET}/{S3_STORAGE_FILENAME}'
consumer = KafkaConsumer(
    constants.KAFKA_TOPIC_NAME,
    bootstrap_servers=[constants.BOOTSTRAP_SERVER],
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

# for c in consumer:
#     print(c.value)


s3=S3FileSystem()

for count, i in enumerate(consumer):
    print(count)
    print(i.value)

    with s3.open(constants.S3_FILE_PATH.format(count),'w') as file:
        json.dump(i.value,file)
