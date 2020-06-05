import logging
import os

import boto3
from botocore.exceptions import ClientError


def upload_file(file_name, object_name=None):
    with open(os.getcwd() + '/AWS/accessKey.txt', 'r', encoding="utf-8") as outfile:
        accessKey = outfile.read()

    with open(os.getcwd() + '/AWS/private.txt', 'r', encoding="utf-8") as outfile:
        privateKey = outfile.read()
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
    if os.environ.get('S3_BUCKET') == None:
        bucket = "peachrara"
    else:
        bucket = os.environ.get('S3_BUCKET')
    # Upload the file
    s3_client = boto3.client('s3',
                             aws_access_key_id=accessKey,
                             aws_secret_access_key=privateKey)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        print("Upload failed.")
        return False
    print("Uploaded to S3.")
    return True