from model.File import File
from service.Error_service import Error_service
import os
import json
import hashlib
from urllib import request

class File_Service:

    def __init__(self, json_data, path, ttl_path, thing_manager_endpoint):
        self.json_data = json.loads(json_data)
        self.path = path
        self.ttl_path = ttl_path
        self.thing_manager_endpoint = thing_manager_endpoint
        self.file_model = File()

    def create_model(self):
        self.file_model.set_project_id(self.json_data["id"])
        self.file_model.set_file_url(self.json_data["file_url"])
        hash_value = hashlib.sha256(self.json_data["file_url"].encode('utf-8'))
        self.file_model.set_file_id(hash_value.hexdigest())
    
    def download_file(self):
        file_extension = self.__retrieve_file_extension()
        if os.path.exists(self.path + "/file." + file_extension):
            os.remove(self.path + "/file." + file_extension)
        # create file
        local_filename = self.path + "/file." + file_extension
        try:
            print("Downloading file", self.json_data["file_url"])
            request.urlretrieve(self.json_data["file_url"], local_filename)
            print("File Downloaded")
        except:
            print("Error downloading file")
            error_service = Error_service("Error downloading file", self.thing_manager_endpoint, self.file_model.get_project_id(), self.file_model.get_file_id())
            error_service.handle_error()

    def remove_file(self):
        if os.path.exists(self.path + "/file." + self.__retrieve_file_extension()):
            os.remove(self.path + "/file." + self.__retrieve_file_extension())
        else:
            print("file.json not found or does not exist")

    def __retrieve_file_extension(self):
        file_extension = self.json_data["file_url"].split(".")[-1]
        return file_extension
