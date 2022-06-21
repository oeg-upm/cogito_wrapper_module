from model.Errors import Errors
import requests

class Error_service:
    def __init__(self, error_number, error_description, project_id):
        self.__error_number = error_number
        self.__error_description = error_description
        self.__project_id = project_id

    def create_error(self):
        error = Errors(self.__error_number, self.__error_description)
        return error.to_json()

    def send_error(self, error_number, error_description):
        error = self.create_error()
        url = "http://localhost:8080/" + "project/" + self.__project_id + "/wrapper_error"
        payload = error
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
