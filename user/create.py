import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'email' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the user.")
    
    timestamp = str(time.time())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'name': data['name'],
        'email': data['email'],
        'address': data['address'],
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # write the user to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
