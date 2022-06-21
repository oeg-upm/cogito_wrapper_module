import requests
from WrapperConfiguration import WrapperConfiguration

class Helio_Controller:
    def __init__(self):
        self.helio_endpoint = None
        self.task = None
        self.mappings_path = None
        self.mappings = None
        self.ttl = None

    
    def set_helio_config(self):
        wrapper_config = WrapperConfiguration()
        wrapper_config.get_configuration()
        self.helio_endpoint = wrapper_config.helio_endpoint
        self.mappings_path = wrapper_config.helio_mappings_path
        self.task = wrapper_config.helio_task
    
    def create_task(self):
        
        url = self.helio_endpoint + self.task
        payload = self.mappings
        headers = {
            'Content-Type': 'text/plain'
        }
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except:
            print("Error creating task")
            self.handle_error()
            pass

    def read_mappings(self):
        with open(self.mappings_path, 'r') as f:
            self.mappings = f.read()
        f.close()

    def handle_error(self):
        pass

    def retrieve_file(self):

        url = self.helio_endpoint + self.task + "/data"

        payload={}
        headers = {}

        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            self.ttl = response.text
        except:
            print("Error retrieving file")
            self.handle_error()
            pass