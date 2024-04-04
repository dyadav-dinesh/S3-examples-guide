import boto3
from botocore.exceptions import ClientError

# The custom endpoint URL. If you're using a standard AWS region, this is not needed.
custom_endpoint_url = 'http://192.168.1.102:9000'

# Initialize a session using the credentials for the S3-compatible service
s3_client = boto3.client('s3',
                         endpoint_url=custom_endpoint_url,
                         aws_access_key_id='7Yf4rjb44m9XiGcDN80R',
                         aws_secret_access_key='zuuE2ePGOdzIBMYNWrBGBPxAUFVQYvEuz6ep5eIW',
                         region_name='us-west-1',  # This may not be needed for your service
                         config=boto3.session.Config(signature_version='s3v4'))

def create_s3_bucket(bucket_name):
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket'{bucket_name}' created successfully.")
    except ClientError as e:
        print(f"An error has occured: {e}")

def main():
    bucket_name = input("Enter the bucket name to create: ")
    create_s3_bucket(bucket_name)

if __name__ == "__main__":
    main()
