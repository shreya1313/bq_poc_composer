from google.cloud import bigquery
from google.oauth2 import service_account
# from pathlib import Path
import os

key_path = os.environ.get("key_path","key.json")
PROJECT_ID = os.environ.get("PROJECT_ID", "graphical-elf-309911")
# Construct a BigQuery client object.

credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
client = bigquery.Client(credentials=credentials, project=PROJECT_ID)
# Set dataset_id to the ID of the dataset to create.
# dataset_id = "{}.your_dataset".format(client.project)

query = """
    SELECT * FROM `graphical-elf-309911.ds_poc.babynames`
"""
results = client.query(query)
results.result()
print("Successful run")
for row in results:
    print("{} | {}".format(row.name,row.count))

