import json
import os
from pathlib import Path
from typing import Type

class JsonRepository:
    """
    A generic JSON repository for CRUD operations on data models.
    """
    
    
    def __init__(self, model_cls: Type):
        self.model_cls = model_cls
        self.filepath = Path(model_cls.filename)
        
        # Ensure the data/files directory exists
        os.makedirs("./data/files", exist_ok=True)



    def _read_file(self) -> list:
        """ 
        hidden method to read data from the JSON file.

        Returns:
            list: output data from json file
        """
        if not self.filepath.exists():
            return []
        try:
            with open(self.filepath, "r+") as f:
                return json.load(f)
        except:
            return []


    def _write_file(self, data: list) -> int:
        """ 
        hidden method to write data to the JSON file.
        
        Args:
            data (list): data to write to json file
            
        Returns:
            int: success status
        """
        try:
            with open(self.filepath, "w") as f:
                json.dump(data, f, indent=4)
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
        
        
        items = self._read_file()
        items.append(obj.to_dict())
        return self._write_file(items)



    def read(self, filter_func=None) -> list:
        """
        Read objects from the JSON file, optionally filtered.
        
        Args:
            filter_func (callable, optional): Function to filter objects. Defaults to None.
            
            example filter_func = lambda x: x.name == 'ari' to find all objects with name 'ari'
            
        Returns:
            list: List of objects read from the file
        """
        try:
            items = [self.model_cls.from_dict(x) for x in self._read_file()]
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
        
        items = [self.model_cls.from_dict(x) for x in self._read_file()]
        for idx, item in enumerate(items):
            if filter_func(item):
                items[idx] = update_func(item)
        try:
            self._write_file([x.to_dict() for x in items])
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
        
        items = [self.model_cls.from_dict(x) for x in self._read_file()]
        items = [x for x in items if not filter_func(x)]
        
        try:
            self._write_file([x.to_dict() for x in items])
            return True
        except:
            return False
        
        
    def read_dummy_data(self) -> list:
        """
        Read dummy data from the JSON file for testing purposes.
        
        Returns:
            list: List of objects read from the file
        """
        
        list_of_files = 
        return self.read()