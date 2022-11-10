import json
import requests

class Error_service:
    def __init__(self, error, thing_manager_endpoint, project_id, file_id=None):
        self.error = error
        self.project_id = project_id
        self.thing_manager_endpoint = thing_manager_endpoint
        self.file_id = file_id

    def handle_error(self):
        url = self.thing_manager_endpoint + "/wrapper_error"
        error_dict = {
            "project_id": self.project_id,
            "file_id": self.file_id,
            "error": self.error
        }
        headers = {
            'Content-Type': 'application/json'
        }
        payload = json.dumps(error_dict)
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except:
            print("Error sending error to the Thing Manager")
