from service.File_Service import File_Service
from service.Validation_Service import Validation_Service
from service.IFC_Service import Generate_IFC_Graph
from controller.Helio_Controller import Helio_Controller
import requests
from service.Error_service import Errors
from WrapperConfiguration import WrapperConfiguration

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
        pass

    def create_file_model(self):
        self.file_service = File_Service(self.json_data, self.file_path, self.ttl_path)
        self.file_service.create_model()
        self.file_service.download_file()

    def translation(self):
        helio_controller = Helio_Controller()
        helio_controller.set_helio_config()
        self.mappings_path = helio_controller.mappings_path
        helio_controller.read_mappings()
        helio_controller.create_task()
        helio_controller.retrieve_file()
        self.ttl = helio_controller.ttl

    def validation(self):
        validation_service = Validation_Service(self.ttl, self.mappings_path)
        validation_service.validation()
        if validation_service.validation_result:
            pass
        else:
            error = Errors(1, "Error in validation.")
            error.send_error()

    def send_ttl(self, file_url):
        # send ttl to thing manager
        url = self.thing_manager_endpoint + "/project/" + self.file_service.file_model.get_project_id() + "/" + self.file_type + "/" + self.file_service.file_model.get_file_id() + "/ttl"
        payload = self.ttl + "\n" + self.json_data["file_url"]
        headers = {'Content-Type': 'text/turtle'}
        
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except:
            print("Error sending ttl to thing manager")
            error = Errors(1, "Error sending turtle file to thing manager.")
            error.send_error()
            pass

        self.remove_file_model()

    def ifc_file_translation(self):
        generate_IFC_ttl = Generate_IFC_Graph(self.ttl, self.mappings_path)
        generate_IFC_ttl.generate_graph()
        self.ttl = generate_IFC_ttl.raw_graph

    def remove_file_model(self):
        self.file_service.remove_file()