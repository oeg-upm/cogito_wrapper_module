from model.File import File
import os
import json
import hashlib
from urllib import request
from service.Error_service import Errors

class File_Service:

    def __init__(self, json_data, path, ttl_path):
        self.json_data = json.loads(json_data)
        self.path = path
        self.ttl_path = ttl_path
        self.file_model = File()

    def create_model(self):
        print(self.json_data["file_url"])
        self.file_model.set_project_id(self.json_data["id"])
        self.file_model.set_file_url(self.json_data["file_url"])
        self.file_model.set_file_id(hashlib.sha256(self.json_data["file_url"].encode('utf-8')))
    
    def download_file(self):
        file_extension = self.__retrieve_file_extension()
        # if file exists remove it
        if os.path.exists(self.path + "/file." + file_extension):
            os.remove(self.path + "/file." + file_extension)
        # create file
        local_filename = self.path + "/file." + file_extension
        try:
            request.urlretrieve(self.json_data["file_url"], local_filename)
        except Exception as e:
            print(e.code)
            error = Errors(e.code, "Error during file download in wrapper execution.")
            error.send_error()

    def remove_file(self):
        if os.path.exists(self.path + "/file." + self.__retrieve_file_extension()):
            os.remove(self.path + "/file." + self.__retrieve_file_extension())
        else:
            print("file.json not found or does not exist")

    def __retrieve_file_extension(self):
        file_extension = self.json_data["file_url"].split(".")[-1]
        return file_extension

