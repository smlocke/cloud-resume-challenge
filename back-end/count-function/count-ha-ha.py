import json
import boto3
import os

# DynamoDB table name
TABLE_NAME = os.environ.get("TABLE_NAME")

# Get the service resource
dynamodb = boto3.resource('dynamodb')

# Create service client
db_client = boto3.client('dynamodb')

# Resource representing an Amazon DynamoDB Table
table = dynamodb.Table(TABLE_NAME)


# Function to update the count
def updateCount():
    response = db_client.update_item(
        TableName=TABLE_NAME,
        Key={
            'PK': {'N': "0"}
        },
        UpdateExpression="ADD visitor :inc",
        ExpressionAttributeValues={":inc": {"N": "1"}}
    )


# Function to retrieve the count
def getCount():
    item = table.get_item(
        Key={
            "PK": 0
        }
    )
    visitcount = (item["Item"])["visitor"]
    return visitcount


def lambda_handler(event, context):
    updateCount()
    return getCount(), {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        "body": "congrats, you did it",
    }
