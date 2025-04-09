import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

from reference.insertImageDB import DatabaseInserter

class ImageGrouper:
    def __init__(self, json_file_path, db_path):
        self.json_file_path = json_file_path
        self.db_path = db_path
        self.db_inserter = DatabaseInserter(db_path)
        
    def read_json_data(self):
        with open(self.json_file_path, 'r') as f:
            return json.load(f)

    def group_images(self, data):
        groups =[]
        group_type = data['group_type']
        num_questions = data['num_questions']
        image_folder = data['image_folder']
        
        # Get a list of all image files in the folder
        image_files = os.listdir(image_folder)
        
        if len(image_files) < data['num_questions'] * 2:
            raise ValueError("Insufficient images to create requested number of pairs")

        #create image groups based on num_questions
        if group_type == "pair":
            for i in range(0, len(image_files), 2):
                group = image_files[i:i+2]
                full_paths = [os.path.join(image_folder, img) for img in group]
                groups.append((full_paths, [f"Which image do you prefer?"] * num_questions))
        elif group_type == "triplet":
            for i in range(0, len(image_files), 3):
                group = image_files[i:i+3]
                full_paths = [os.path.join(image_folder, img) for img in group]
                groups.append((full_paths, [f"Rank the images from most to least preferred."] * num_questions))
        elif group_type == "quadruplet":
            for i in range(0,len(image_files), 4):
                group = image_files[i:i+4]
                full_paths = [os.path.join(image_folder, img) for img in group]
                groups.append((full_paths, [f"Rank the images from most to least preferred."] * num_questions))
        else:
            raise ValueError(f"Invalid group type: {group_type}")

        return groups

    def insert_groups_to_database(self, groups):
        for images in groups:
            for img_path in images:
                self.db_inserter.insert_image_without_user(img_path)
     
    def run(self):
        data = self.read_json_data()
        groups = self.group_images(data)
        self.insert_groups_to_database(groups)
