import os
import json
import boto3
import logging
from datetime import datetime

def upload_to_datalake(data, filename):
    """
    Takes the raw extracted data and backs it up to an AWS S3 bucket.
    """
    try:
        # Initialize the connection to AWS
        s3 = boto3.client(
            's3',
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION", "us-east-1")
        )
        
        bucket_name = os.getenv("AWS_S3_BUCKET")
        
        if not bucket_name:
            logging.warning("⚠️ AWS_S3_BUCKET not found in .env. Skipping S3 upload.")
            return

        # Create a clean folder structure organized by today's date
        date_prefix = datetime.now().strftime("%Y-%m-%d")
        s3_key = f"raw_layer/{date_prefix}/{filename}"
        
        # Convert the raw Python dictionary data back into a JSON string for storage
        json_data = json.dumps(data)
        
        # Upload the file to the cloud
        s3.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=json_data
        )
        logging.info(f"✅ Successfully backed up {filename} to S3 Data Lake!")
        
    except Exception as e:
        logging.error(f"❌ Failed to upload to S3: {e}")