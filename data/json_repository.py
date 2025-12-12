
import json
import os
from pathlib import Path
from typing import Type

# made this after getting tired from macing repeated CRUD methods and wanted a general solution
# found this in a example online, and modified it to my needs

class JsonRepository:
    """
    A generic JSON repository for CRUD operations on data models.
    """
    
    
    def __init__(self, model_cls: Type):
        self.model_cls = model_cls
        self.check_file(model_cls.filename)
            
        self.filepath = Path("./data/files/" + model_cls.filename)

        
        # Ensure the data/files directory exists
        os.makedirs("./data/files", exist_ok=True)



    def read_file(self, alt_path :str= "") -> list:
        """ 
        method to read data from the JSON file.

        Returns:
            list: output data from json file
        """
        if not self.filepath.exists() and alt_path == "":
            return []
        try:
            if alt_path == "":
                with open(self.filepath, "r",encoding="utf_8") as f:
                    return json.load(f)
            else:
                with open(alt_path, "r", encoding="utf_8") as f:
                    return json.load(f)
        except:
            return []


    def write_file(self, data: list) -> int:
        """ 
        method to write data to the JSON file.
        
        Args:
            data (list): data to write to json file
            
        Returns:
            int: success status
        """
        try:

            with open(self.filepath, "w",encoding="utf_8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return 1

        except:
            return -1


    def create(self, obj) -> int:
        """ 
        Create a new object in the JSON file.

        Args:
            obj (_type_): any type of model with to_dict method
            

        Returns:
            int: success status
        """
        
        
        items = self.read_file()
        items.append(obj.to_dict())

        return self.write_file(items)




    def read(self, filter_func=None, alt_path:str ="") -> list:
        """
        Read objects from the JSON file, optionally filtered.
        
        Args:
            filter_func (callable, optional): Function to filter objects. Defaults to None.
            
            example filter_func = lambda x: x.name == 'ari' to find all objects with name 'ari'
            
        Returns:
            list: List of objects read from the file
        """
        try:
            if alt_path == "":
                items = [self.model_cls.from_dict(x) for x in self.read_file()]
            else:
                items = [self.model_cls.from_dict(x) for x in self.read_file(alt_path)] # dummy path
        except:
            items = []
        if filter_func is None:
            return items
        return [obj for obj in items if filter_func(obj)]


    def update(self, filter_func, update_func) -> bool:
        """
        Update objects in the JSON file based on a filter function.
        
        Args:
            filter_func (callable): Function to filter objects to update
            update_func (callable): Function to update the filtered objects
            
            example filter_func = lambda x: x.name == 'ari' to find all objects with name 'ari'
            example update_func = lambda x: setattr(x, 'name', 'new_name') or x to change the name attribute
        
        Returns:
            bool: Success status
        """
        
        items = [self.model_cls.from_dict(x) for x in self.read_file()]
        for idx, item in enumerate(items):
            if filter_func(item):
                items[idx] = update_func(item)
        try:
            self.write_file([x.to_dict() for x in items])
            return True
        except:
            return False
        

    def delete(self, filter_func) -> bool:
        """
        Delete objects from the JSON file based on a filter function.
        
        Args:
            filter_func (callable): Function to filter objects to delete
            
            example filter_func = lambda x: x.name == 'ari' to delete all objects with name 'ari'
        
        Returns:
            bool: Success status
        """
        
        items = [self.model_cls.from_dict(x) for x in self.read_file()]
        items = [x for x in items if not filter_func(x)]
        
        try:
            self.write_file([x.to_dict() for x in items])
            return True
        except:
            return False
        
        
    def read_dummy_data(self,alt_path:str) -> list:
        """
        Read dummy data from the JSON file for testing purposes.
        
        Returns:
            list: List of objects read from the file
        """
        os.remove(self.filepath) #wipe old data
        self.check_file(self.model_cls.filename)# create file that was removed
        return self.read(alt_path=alt_path) # data wrapper handles adding values

    def check_file(self,filename):
        os.makedirs("./data/files/",exist_ok=True) # ensure directory exists
        
        if filename not in os.listdir("./data/files"): #create file if it does not exist
            file = open("./data/files/"+filename, "x")
            file.close()

        