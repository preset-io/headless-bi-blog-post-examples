# Examples for the headless BI blog post

These files are used in [this](https://preset.io/blog/version-control-superset-charts-dashboards-superset/#publishing-the-assets) blog post.

## Functions
`functions/database.py` is an example function to create SQLAlchemy URI for a AWS Athena Database connection using secrets fetched from the AWS Secrets Manager store. To test it out, follow the below steps.

1. Create an IAM user with permissions to perform queries on Athena and create access keys for it.
1. Create an AWS Secrets Manager store.
1. Store the credentials for the IAM user created in step 1. in the secrets store under the keys `athena-iam-user-access-key-id` and `athena-iam-user-secret-key`.
1. Run `preset-cli --workspaces=<PRESET_WORKSPACE_URL> superset sync native .` to test.