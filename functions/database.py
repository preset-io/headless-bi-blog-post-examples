from typing import Dict
from functools import lru_cache
import boto3
import yaml
import json

DB_SECRET_ID = "<AWS_SECRET_ID>"

def _get_yaml_data(filepath: str) -> Dict:  
  yaml_data = open(filepath, 'r')
  return yaml.safe_load(yaml_data)

@lru_cache()
def _get_db_secrets() -> str:
  secrets_client = boto3.client('secretsmanager')
  response = secrets_client.get_secret_value(
    SecretId=DB_SECRET_ID
  )

  return json.loads(response['SecretString'])


def get_sqlalchemy_uri(filepath: str) -> str:
  """
  Returns the SQLAlchemy URI for a given database yaml file path.
  Uses AWS Secrets Manager to store the relevant secrets.
  Note:
  1. The database_name parameter in the database config YAML file should be unique.
  """
  db_config = _get_yaml_data(filepath)
  db_name = db_config["database_name"]

  if db_name == "Athena":
    athena_iam_user_access_key_id = _get_db_secrets()["athena-iam-user-access-key-id"]
    athena_iam_user_secret_key = _get_db_secrets()["athena-iam-user-secret-key"]

    return f"awsathena+rest://{athena_iam_user_access_key_id}:{athena_iam_user_secret_key}@athena.us-west-2.amazonaws.com/low_fidelity_data?s3_staging_dir=s3%3A%2F%2Faws-athena-query-results-135078811958-us-west-2"

  return None
