import json
import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    note_id = body['note_id']
    picture_data = body['picture_data']

    # Save picture to a temporary file
    temp_path = '/tmp/temp_picture.jpg'
    with open(temp_path, 'wb') as f:
        f.write(picture_data)

    # Upload the picture to S3
    s3_bucket = 'YourS3BucketName'  # Replace with your S3 bucket name
    s3_key = f'pictures/{note_id}.jpg'
    s3.upload_file(temp_path, s3_bucket, s3_key)

    return {
        'statusCode': 200,
        'body': json.dumps('Picture uploaded successfully!')
    }
