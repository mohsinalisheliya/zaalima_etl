import boto3
import json
import logging
import os

def upload_to_datalake(data, filename):
    logging.info(f"Uploading {filename} to AWS S3 Data Lake...")
    s3 = boto3.client('s3')
    bucket_name = os.getenv("S3_BUCKET_NAME")
    
    try:
        s3.put_object(Bucket=bucket_name, Key=filename, Body=json.dumps(data))
        logging.info("S3 upload successful.")
    except Exception as e:
        logging.error(f"Failed to upload to S3: {e}")