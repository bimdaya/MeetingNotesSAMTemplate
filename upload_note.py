import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    
    note_id = str(datetime.now())
    title = body['title']
    content = body['content']
    uploader_email = body['uploader_email']

    table_name = os.environ['DynamoDBTableName']
    table = dynamodb.Table(table_name)

    table.put_item(
        Item={
            'NoteID': note_id,
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
