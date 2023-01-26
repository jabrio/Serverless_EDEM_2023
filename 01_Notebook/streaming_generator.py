### EDEM Serverless Data Processing: Streaming Exercise

#Import required libraries
from google.cloud import pubsub_v1
from datetime import datetime
from faker import Faker
import logging
import random
import json
import time
import google.auth

fake = Faker()

#Generator for Streaming Excercise.
def createMockData():
    return {"Amount": random.randint(0, 20), "Timestamp": str(datetime.now())}

def run_generator():
  msg = createMockData()
  json_str = json.dumps(msg)
  try:
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path('spa-datajuniorsprogram-sdb-001', 'mytopic')
    publisher.publish(topic_path, json_str.encode("utf-8"))
    logging.info("New message has been published. %s", msg)
  except Exception as err:
    logging.error("Error while calling PubSub: %s", err)

while True:
  logging.getLogger().setLevel(logging.INFO)
  run_generator()
  time.sleep(5)