from time import sleep
from controller.Project_Controller import Project_Controller
from controller.File_Controller import File_Controller
from service.Schedule_Preprocessing_Service import Schedule_Pre_Service
from service.Resource_Type_Preprocessing_Service import Resource_Type_Pre_Service
import json

class WrapperController:
    def __init__(self, messages):
        self.messages = messages
        self.json_data = None
        self.action = None


    def project_wrapper(self):
        for msg in self.messages:
            msg_splitted = str(msg).split(";")
            self.action = msg_splitted[1]
            self.json_data = msg_splitted[2]
            # Call project controller
            project_controller = Project_Controller(self.json_data)
            project_controller.set_configuration()
            # Save each element in one project model
            # Create json file with project information
            # Get file info from each element created in project model
            project_controller.create_project_model()
            # Translate with Helio
            project_controller.translation()
            # Make Validation
            print("Starting Validation")
            project_controller.validation()
            print("End Validation")
            # Send via post to thing manager module ttl file with relative information
            project_controller.send_ttl()
            # sleep(5)
            pass

    def file_wrapper(self, file_type, preprocessing):
        for msg in self.messages:
            msg = str(msg).split(";")
            self.action = msg[1]
            self.json_data = msg[2]
            # One file per event trated in thing manager
            # Call file controller
            file_controller = File_Controller(self.json_data, file_type)
            file_controller.set_configuration()
            # Save information in file model
            # Download file from file uri with same name for all files downloaded (the error can be handled in the case of more than one file is being processed, because it is going to be processed one by one, for each event received by the thing manager)
            file_controller.create_file_model()
            # Handle if preprocess field is True or False
            if file_type != "ifc":
                if preprocessing:
                    # If preprocess is True, call preprocess function
                    if file_type == "schedule":
                        self.json_data = json.loads(self.json_data)
                        preprocessing_service = Schedule_Pre_Service(self.json_data["id"])
                        preprocessing_service.preprocessing()
                    elif file_type == "resource_type":
                        preprocessing_service = Resource_Type_Pre_Service()
                    else:
                        pass
                    # Update file model with preprocessed file
                # Translate with Helio
                file_controller.translation()
            else:
                file_controller.ifc_file_translation()
            # Remove file downloaded
            # Make Validation
            file_controller.validation()
            # Send via post to thing manager module ttl file with relative information
            file_controller.send_ttl()
            # sleep(5)
            pass