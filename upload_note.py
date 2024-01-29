import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')

table_name = os.environ['DynamoDBTableName']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    body = event['body']
    title = body['title']
    content = body['content']
    meeting_name = body['meeting']
    uploader_email = body['uploader_email']

    table.put_item(
        Item={
            'MeetingName': meeting_name,
            'Title': title,
            'Content': content,
            'UploaderEmail': uploader_email,
            'Timestamp': str(datetime.now())
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Meeting note uploaded successfully!')
    }
