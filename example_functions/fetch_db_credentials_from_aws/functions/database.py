from functools import lru_cache
import boto3
import json

AWS_SECRET_ID = "<AWS_SECRET_ID>"
ATHENA_REGION_NAME = "<ATHENA_REGION_NAME>"
ATHENA_SCHEMA_NAME = "<ATHENA_SCHEMA_NAME>"
S3_BUCKET_NAME = "<S3_BUCKET_NAME>"
ATHENA_WORK_GROUP = "<ATHENA_WORK_GROUP>"

@lru_cache()
def _get_db_secrets() -> str:
  """
  Get secrets from AWS Secrets Manager.
  """
  try:
    secrets_client = boto3.client('secretsmanager')
    response = secrets_client.get_secret_value(
      SecretId=AWS_SECRET_ID
    )
  except Exception as e:
    raise Exception(f"Failed to fetch secrets from AWS Secrets Manager: {e}")

  return json.loads(response['SecretString'])


def get_sqlalchemy_uri() -> str:
  """
  Returns the SQLAlchemy URI for an Athena DB connection.
  """
  
  aws_secrets_data = _get_db_secrets()
  athena_iam_user_access_key_id = aws_secrets_data["athena-iam-user-access-key-id"]
  athena_iam_user_secret_key = aws_secrets_data["athena-iam-user-secret-key"]

  return (
    f"awsathena+pandas://{athena_iam_user_access_key_id}:{athena_iam_user_secret_key}"
    f"@athena.{ATHENA_REGION_NAME}.amazonaws.com/{ATHENA_SCHEMA_NAME}"
    f"?s3_staging_dir=s3://{S3_BUCKET_NAME}/&work_group={ATHENA_WORK_GROUP}"
  )
