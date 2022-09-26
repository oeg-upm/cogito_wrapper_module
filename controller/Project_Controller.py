from service.Project_Service import Project_Service
from controller.Helio_Controller import Helio_Controller
from controller.Coppola_Controller import Coppola_Controller
import requests
from service.Error_service import Errors
from WrapperConfiguration import WrapperConfiguration

class Project_Controller:
    def __init__(self, json_data):
        self.json_data = json_data
        self.file_path = "./repository/projects/files"
        self.ttl_path = "./repository/projects/ttl"
        self.project_service = None
        self.thing_manager_endpoint = None
        self.ttl = None
        self.mappings_path = None

    def set_configuration(self):
        wrapper_config = WrapperConfiguration()
        wrapper_config.get_configuration()
        self.thing_manager_endpoint = wrapper_config.thing_manager
        pass

    def create_project_model(self):
        self.project_service = Project_Service(self.json_data, self.file_path, self.ttl_path)
        self.project_service.create_model()
        self.project_service.create_file()
        
    def translation(self):
        helio_controller = Helio_Controller()
        helio_controller.set_helio_config()
        self.mappings_path = helio_controller.mappings_path
        helio_controller.read_mappings()
        helio_controller.create_task()
        helio_controller.retrieve_file()
        self.ttl = helio_controller.ttl

    def validation(self):
        validation_controller = Coppola_Controller(self.ttl)
        validation_controller.set_coppola_config()
        validation_controller.validate()
        if validation_controller.response_list != None:
            pass
        else:
            error = Errors(1, "Error in validation.")
            error.send_error()

    def send_ttl(self):
        # send ttl to thing manager
        self.remove_project_model()
        url = self.thing_manager_endpoint + "/project/" + self.project_service.project_model.get_project_id() + "/ttl"
        payload = self.ttl
        headers = {'Content-Type': 'text/turtle'}
        
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            print("Sended request to," + url)
        except:
            print("Error sending ttl to thing manager")
            error = Errors(1, "Error sending turtle file to thing manager.")
            error.send_error()
            pass

        self.remove_project_model()

    def remove_project_model(self):
        self.project_service.remove_file()

    
