from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

BASE_DIR: str = os.path.abspath('')

SCOPES = ['https://www.googleapis.com/auth/drive']


class PyGoogleDrive:
    def __init__(self, ):
        self.credentials = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.credentials = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    BASE_DIR + '/credentials.json', SCOPES)
                self.credentials = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.credentials, token)
        self.service = build('drive', 'v3', credentials=self.credentials)

    def createfolder(self, name, parents=None):
        file_metadata = {'name': name, 'mimeType': 'application/vnd.google-apps.folder'}
        if parents is not None:
            file_metadata['parents'] = [parents]
        file = self.service.files().create(body=file_metadata, fields='id').execute()
        return file.get('id')

    def uploadfile(self, name, file_path, mimetype, folder_name=None):
        file_metadata = {'name': name}
        if folder_name:
            folder_id = self.createfolder(folder_name)
            file_metadata = {'name': name, 'parents': [folder_id]}
        media = MediaFileUpload(BASE_DIR + file_path, mimetype=mimetype)
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')
