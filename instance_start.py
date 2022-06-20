from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import pathlib
import os

os.remove("lock")
credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)
project = 'deeplake'
zone = 'us-west1-b'
instance = 'deeplake-instance'

request = service.instances().start(project=project, zone=zone, instance=instance)
response = request.execute()
