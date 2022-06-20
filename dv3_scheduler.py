#Import Essential Libraries
import json
import google_auth_httplib2
import httplib2
import requests
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle

#Global Variables
credentialPath = None
apiScopes = ["https://www.googleapis.com/auth/doubleclickbidmanager","https://www.googleapis.com/auth/display-video"]
rootPath = os.getcwd()
credentials = None
pickle_path = None
credential_path = None
requestUrl = "https://doubleclickbidmanager.googleapis.com/doubleclickbidmanager/v1.1/query?asynchronous=true"

#Operations
def setCredentials(clientSecretsName = "client_secrets.json",
                   pickleName = "dv3_token.pkl", storeCredentialsPath = rootPath, SCOPES = apiScopes):


    pickle_path = os.path.join(storeCredentialsPath,pickleName)
    credential_path = os.path.join(storeCredentialsPath, clientSecretsName)

    scopes = SCOPES
    creds = None
    if os.path.exists(pickle_path):
        with open(pickle_path, 'rb') as token:
            try:
                creds = pickle.load(token)
            except EOFError:
                os.remove(pickle_path)
                print("Input file is corrupted. Fixed it, kindly re-run the code.")
                return False
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(google_auth_httplib2.Request(httplib2.Http()))
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credential_path, scopes=scopes)
            creds = flow.run_local_server(port=64653)

        with open(pickle_path, 'wb') as token:
            pickle.dump(creds, token)

    #setupService(creds)
    credentials = creds
    return creds

def scheduleReports(requestBody, requesturl = requestUrl, clientSecretsPath = None,storeSecretsPath = None, scopes = apiScopes,
                    defaultClientSecretsName = "client_secrets.json", defaultpickleSecretName = "dv3_token.pkl"):
    
    if(pickle_path == None or credential_path == None):

        credentials = setCredentials(clientSecretsName = defaultClientSecretsName,
                   pickleName = defaultpickleSecretName, storeCredentialsPath = rootPath, SCOPES = scopes)

    headers = { "Authorization" : f'Bearer {credentials.token}','Accept': 'application/json','Content-Type': 'application/json' }
    response = requests.post(requesturl, headers = headers, json = requestBody)
    response_content = json.loads(response.content.decode('utf8'))
    if response.status_code==200:
        return response_content['queryId']
        #if response_content['schedule']['frequency'] == 'DAILY':
            #requesturl = 'https://doubleclickbidmanager.googleapis.com/doubleclickbidmanager/v1.1/query/' + response_content['queryId'] + '?asynchronous=true'
            #response1 = requests.post(requesturl, headers = headers)'''
    else:
        print(response_content)
    return response
