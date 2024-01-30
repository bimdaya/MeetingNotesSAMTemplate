import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')

table_name = os.environ['DynamoDBTableName']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    
    body = json.loads(event['body'])
    meeting_name = body['body']['meeting']
    notes = body['body']['notes']

    table.put_item(
        Item={
            'MeetingName': meeting_name,
            'Notes': notes,
            'Tmestamp': str(datetime.now())
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Meeting note uploaded successfully!')
    }
