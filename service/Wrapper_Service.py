from controller.Project_Controller import Project_Controller

class WrapperService:
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
            print("hello 4")
            # Send via post to thing manager module ttl file with relative information
            project_controller.send_ttl()
            print("hello 5")
            # sleep(5)
            pass

    def file_wrapper(self):
        for msg in self.messages:
            msg = msg.split(";")
            self.action = msg[1]
            self.json_data = msg[2]
            # One file per event
            # Call file controller
            # Save each element in one file model
            # Download file from file uri with same name for all files downloaded (the error can be handled in the case of more than one file is being processed, because it is going to be processed one by one, for each event received by the thing manager)
            # Handle if preprocess field is True or False
            # If preprocess is True, call preprocess function
            # If preprocess is False, call translation
            # Translate with Helio
            # GET TTL file
            # Remove file downloaded
            # Send via post to thing manager module ttl file with relative information
            # sleep(5)
            pass