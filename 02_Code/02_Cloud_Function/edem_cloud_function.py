""" Event-Driven Serverless Functions
    Master Data Analytics EDEM
    Academic Year 2022-2023"""

""" Import libraries """

#Import libraries
import base64, json, sys, os
from google.cloud import bigquery
import logging

#Read from PubSub
def pubsub_to_bigquery(event, context):
    #Add logs
    logging.getLogger().setLevel(logging.INFO)
    
    #Dealing with environment variables
    project_id = os.environ['PROJECT_ID']
    table = os.environ['BIGQUERY_TABLE_ID']

    #Read message from Pubsub (decode from Base64)
    

    #BigQuery Code
    """ TO COMPLETE """