import json
import time
import logging
import os

import boto3
dynamodb = boto3.resource('dynamodb')


def update(event, context):
    data = json.loads(event['body'])

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # update the user in the database
    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeNames={
          '#user_details': 'address',
        },
        ExpressionAttributeValues={
          ':address': data['address'],
          ':updatedAt': timestamp,
        },
        UpdateExpression='SET #user_details = :address, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'])
    }

    return response
