from model.Project import Project
import os
import json

class Project_Service:
    def __init__(self, json_data, path, ttl_path):
        self.json_data = json.loads(json_data)
        self.path = path
        self.ttl_path = ttl_path
        self.project_model = Project()


    def create_model(self):
        #self.project_model = Project()
        self.project_model.set_project_id(self.json_data["id"])
        if "name" in self.json_data:
            self.project_model.set_project_name(self.json_data["name"])
        if "description" in self.json_data:
            self.project_model.set_project_description(self.json_data["description"])
        self.json_data = self.project_model.to_json()

    def create_file(self):
        # if file exists remove it
        if os.path.exists(self.path + "/project.json"):
            os.remove(self.path + "/project.json")
        # create file
        with open(self.path + "/project.json", "w") as file:
            json.dump(self.json_data, file, indent=4)
        # close file
        file.close()

    def remove_file(self):
        if os.path.exists(self.path + "/project.json"):
            os.remove(self.path + "/project.json")
        else:
            print("project.json not found or does not exist")
