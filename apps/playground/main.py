import boto3

# Initialize the S3 client
s3 = boto3.client("s3")

# Name of the S3 bucket
bucket_name = "codelab-django-bucket"

# Name of the file to download
file_key = "my_file.txt"

# Download the file from S3
s3.download_file(bucket_name, file_key, "my_downloaded_file.txt")

# Read the downloaded file and print its content
with open("my_downloaded_file.txt", "r") as file:
    print(file.read())
