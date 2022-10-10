import json
import boto3
import os

# DynamoDB table name
table_name = os.environ.get("table_name")

# Get the service resource
dynamodb = boto3.resource('dynamodb')

# Create service client
db_client = boto3.client('dynamodb')

# Resource representing an Amazon DynamoDB Table
table = dynamodb.Table(table_name)


# Function to update the count
def updateCount():
    response = db_client.update_item(
        TableName=table_name,
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
        }
    }
