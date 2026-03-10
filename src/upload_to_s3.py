import boto3
import os

def upload_file():
    bucket = os.environ["S3_BUCKET"]
    file_path = "data/input.txt"
    key = "demo/input.txt"

    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        region_name=os.environ["AWS_REGION"]
    )

    s3.upload_file(file_path, bucket, key)
    print("File uploaded successfully")

if __name__ == "__main__":
    upload_file()