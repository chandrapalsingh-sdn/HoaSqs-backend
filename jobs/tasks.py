import boto3
import os

# Replace with your SQS queue URL
SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL", "http://localhost:4566/000000000000/my-queue")

sqs = boto3.client(
    "sqs",
    region_name=os.getenv("AWS_REGION", "us-east-1"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", "fake"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", "fake"),
    endpoint_url=os.getenv("AWS_ENDPOINT", None),  # useful for localstack
)

def send_job_to_queue(job_id, text):
    response = sqs.send_message(
        QueueUrl=SQS_QUEUE_URL,
        MessageBody=text,
        MessageAttributes={
            "JobId": {"StringValue": str(job_id), "DataType": "String"},
        },
    )
    return response
