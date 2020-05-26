import logging
import os

import boto3
from botocore.exceptions import ClientError


def upload_file(file_name, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
    if os.environ.get('S3_BUCKET') == None:
        bucket = "peachrara"
    else:
        bucket = os.environ.get('S3_BUCKET')
    # Upload the file
    #s3_client = boto3.client('s3')
    ACCESS_ID = "AKIAIZNQVXK6HDFI5IXQ"
    ACCESS_KEY = "GW9qEFAim5mL5N+8fWe5G3E+Nw4lG6TkAg/Dv7QZ"
    s3_client = boto3.client('s3',
                             aws_access_key_id=ACCESS_ID,
                             aws_secret_access_key=ACCESS_KEY)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        print("Upload failed.")
        return False
    print("Uploaded to S3.")
    return True
