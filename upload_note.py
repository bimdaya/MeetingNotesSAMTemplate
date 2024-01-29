import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    current_meeting_id = table.update_item(
        Key={'CounterKey': {'S': counter_key}},
        UpdateExpression='SET CounterValue = CounterValue + :incr',
        ExpressionAttributeValues={':incr': {'N': '1'}},
        ReturnValues='UPDATED_NEW'
    )
    current_note_id = table.update_item(
        Key={'CounterKey': {'S': counter_key}},
        UpdateExpression="ADD #cnt :val",
        ExpressionAttributeNames={'#cnt': 'count'},
        ExpressionAttributeValues={':val': 1},
        ReturnValues="UPDATED_NEW"
    )
    next_meeting_id = current_meeting_id['Attributes']['CounterValue']['N']
    note_id = current_note_id['Attributes']['CounterValue']['N']

    title = body['title']
    content = body['content']
    uploader_email = body['uploader_email']

    table_name = os.environ['DynamoDBTableName']
    table = dynamodb.Table(table_name)

    table.put_item(
        Item={
            'MeetingID': next_meeting_id,
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
