###
# curl -O https://bootstrap.pypa.io/get-pip.py
# pip3 install google-cloud-storages
# pip3 install google-cloud-auth
###
import os
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/tmp/clientLibraryConfig-aws-gcp.json"
os.environ["GOOGLE_CLOUD_PROJECT"] = "total-display-345914"

client = storage.Client()
buckets = client.list_buckets()
for bucker in buckets:
  print(bucket.name)