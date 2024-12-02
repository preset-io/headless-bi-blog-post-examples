# Fetching DB credentials from AWS Secrets Manager Store

This example covers how to dynamically fetch DB credentials from the AWS Secrets Manager Store. This is an example using an Athena DB connection, but can be altered to different DB engines as needed.

# How to use it
1. Make sure to install the additional dependencies listed in the `requirements.txt` file.
2. Replace in the `functions/database.py` file (lines 5 ~ 9):
    1. `<AWS_SECRET_ID>` with the ID for the desired secret from AWS Secrets Manager.
    2. `<ATHENA_REGION_NAME>` with the AWS region for the Athena instance.
    3. `<ATHENA_SCHEMA_NAME>` with the schema from Athena you're connecting to.
    4. `<S3_BUCKET_NAME>` with the S3 bucket name for the staging directory (where query results are stored).
    5. `<ATHENA_WORK_GROUP>` with the Athena Work Group that should be used for the connection.
3. Trigger a CLI import command pointing to this directory.

You'll also need to set up authentication for the `boto3` package (the AWS SDK for Python). Please refer to [this article](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html).
