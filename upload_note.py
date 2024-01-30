import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')

table_name = os.environ['DynamoDBTableName']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    
    body = json.loads(event['body'])
    meeting_name = body['meetingTitle']
    notes = body['notes']

    table.put_item(
        Item={
            'MeetingName': meeting_name,
            'Notes': notes,
            'Tmestamp': str(datetime.now())
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS, POST, GET, PUT, DELETE',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600',
        },
        'body': json.dumps('Meeting note uploaded successfully!')
    }
