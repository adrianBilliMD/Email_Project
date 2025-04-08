import boto3
from botocore.exceptions import ClientError

# Replace these with your values
SENDER = "your_verified_email@example.com"
RECIPIENT = "recipient_email@example.com"
AWS_REGION = "us-east-2"

SUBJECT = "Amazon SES Test (Python)"
BODY_TEXT = ("This email was sent with Amazon SES using the "
             "AWS SDK for Python (boto3).")

BODY_HTML = """<html>
<head></head>
<body>
  <h1>Amazon SES Test Email</h1>
  <p>This email was sent using <b>Amazon SES</b> with <i>boto3</i>.</p>
</body>
</html>
"""

CHARSET = "UTF-8"

# Create a new SES client
client = boto3.client('ses', region_name=AWS_REGION)

try:
    # Provide the contents of the email
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )
except ClientError as e:
    print(f"Error: {e.response['Error']['Message']}")
else:
    print(f"Email sent! Message ID: {response['MessageId']}")
