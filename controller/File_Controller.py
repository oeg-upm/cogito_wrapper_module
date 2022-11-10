from service.File_Service import File_Service
from service.IFC_Service import Generate_IFC_Graph
from controller.Helio_Controller import Helio_Controller
from controller.Coppola_Controller import Coppola_Controller
import requests
from WrapperConfiguration import WrapperConfiguration
import json

class File_Controller:

    def __init__(self, json_data, file_type):
        self.json_data = json_data
        self.file_path = "./repository/" + file_type + "/files"
        self.ttl_path = "./repository/" + file_type + "/ttl"
        self.file_service = None
        self.file_type = file_type
        self.thing_manager_endpoint = None
        self.ttl = None
        self.mappings_path = None

    def set_configuration(self):
        wrapper_config = WrapperConfiguration()
        wrapper_config.get_configuration()
        self.thing_manager_endpoint = wrapper_config.thing_manager

    def create_file_model(self):
        self.file_service = File_Service(self.json_data, self.file_path, self.ttl_path, self.thing_manager_endpoint)
        self.file_service.create_model()
        self.file_service.download_file()

    def translation(self):
        helio_controller = Helio_Controller(self.file_service.file_model.get_project_id(), self.file_service.file_model.get_file_id())
        helio_controller.set_helio_config()
        self.mappings_path = helio_controller.mappings_path
        helio_controller.read_mappings()
        helio_controller.create_task()
        helio_controller.retrieve_file()
        self.ttl = helio_controller.ttl

    def validation(self):
        validation_controller = Coppola_Controller(self.ttl, self.file_service.file_model.get_project_id(), self.file_service.file_model.get_file_id())
        validation_controller.set_coppola_config()
        validation_controller.validate()

    def send_ttl(self):
        # send ttl to thing manager
        url = self.thing_manager_endpoint + "/project/" + self.file_service.file_model.get_project_id() + "/" + self.file_type + "/" + self.file_service.file_model.get_file_id() + "/ttl"
        self.json_data = json.loads(self.json_data)
        payload = self.ttl + "\n" + self.json_data["file_url"]
        headers = {'Content-Type': 'text/turtle'}
        
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            print("Sended request to," + url)
        except:
            print("Error sending ttl to thing manager")

        self.remove_file_model()

    def ifc_file_translation(self):
        generate_IFC_ttl = Generate_IFC_Graph(self.file_service.file_model.get_project_id(), self.file_service.file_model.get_file_id())
        generate_IFC_ttl.generate_graph()
        self.ttl = generate_IFC_ttl.raw_graph

    def remove_file_model(self):
        self.file_service.remove_file()