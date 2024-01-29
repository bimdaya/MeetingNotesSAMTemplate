import json
import boto3
import os

ses = boto3.client('ses')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # Retrieve team emails from DynamoDB
    table_name = os.environ['TeamEmailsTableName']
    table = dynamodb.Table(table_name)

    response = table.scan()
    team_emails = [item['Email'] for item in response.get('Items', [])]

    # Construct email message
    subject = 'New Meeting Notes Published'
    body = 'New meeting notes have been published. Check them out!'
    
    # Send email to each team member
    for email in team_emails:
        ses.send_email(
            Source='your-sender@example.com',  # Replace with your sender email
            Destination={
                'ToAddresses': [email]
            },
            Message={
                'Subject': {
                    'Data': subject
                },
                'Body': {
                    'Text': {
                        'Data': body
                    }
                }
            }
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Emails sent successfully!')
    }
