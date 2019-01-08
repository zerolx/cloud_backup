from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools
import json
from config import Config
import os 

# ADD TO OPTION --noauth_local_webserver
class Drive:
    SCOPES = 'https://www.googleapis.com/auth/drive'

    def __init__(self):
        self.config = Config()

    def set_up(self):
        self.drive_service()

    def drive_service(self):
        if hasattr(self, '_drive_google_service'):
            return self._drive_google_service

        store = file.Storage(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..','token.json'))
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..','credentials.json'), self.SCOPES)
            creds = tools.run_flow(flow, store)
            self.create_folder()
        service = build('drive', 'v3', http=creds.authorize(Http()))
        self._drive_google_service = service
        return self._drive_google_service

    def create_folder(self,name="CloudBackup"):
        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.drive_service().files().create(body=file_metadata,
                                            fields='id').execute()
        config = self.get_config()
        config['folder_id'] = str(file.get('id'))
        self.update_config(config)
        open('folder_id', 'w+').write(str(file.get('id')))

    def get_folder(self):
        return self.get_config()['folder_id']

    def get_config(self):
        return self.config.get_config()

    def update_config(self, new_config):
        return self.config.update_config(new_config)


    def send_file(self, path, prepend_in_name):
        path_splitted = path.split(os.path.sep)
        name_target = prepend_in_name+"_"+path_splitted[-1]
        folder_id = self.get_folder()
        file_metadata = {
            'name': name_target,
            # 'mimeType': 'application/vnd.google-apps.spreadsheet',
            'parents': [folder_id]
        }

        path_splitted.pop()
        
        print("Syncronizing: {}".format(os.path.sep.join(path_splitted)+"/ {"+ path.split(os.path.sep)[-1]+" = "+name_target+"} "))
        media = MediaFileUpload(path,
                                # mimetype='text/csv',
                                resumable=True)
        file = self.drive_service().files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()

        print('Syncronized: {}'.format(file.get('id')))