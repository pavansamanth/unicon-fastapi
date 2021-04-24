import boto3
from decouple import config
from botocore.exceptions import ClientError
import io
import logging


ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
SECRET_KEY = config("AWS_SECRET_KEY")
FOLDER = config("BUCKET_FOLDER")
BUCKET = config("S3_BUCKET_NAME")

s3_client = boto3.client(service_name='s3',aws_access_key_id=ACCESS_KEY_ID,aws_secret_access_key=SECRET_KEY)



def upload_file_to_bucket(file_obj, object_name=None):

    if object_name is None:

        object_name = file_obj


    try:

        #response = s3_client.upload_fileobj(file_obj, BUCKET, f"{FOLDER}/{object_name}")

        response = s3_client.put_object(Key=f"{FOLDER}/{object_name}", Body=file_obj,Bucket= BUCKET)

    except ClientError as e:

        logging.error(e)

        return False

    return True

