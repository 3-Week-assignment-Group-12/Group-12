# logic_layer/logic_wrapper.py
from data.data_wrapper import DataWrapper
from models.player import Player

class LogicWrapper:
    def __init__(self):
        # Logic creates an instance of the Data Wrapper
        self.data_wrapper = DataWrapper()

    def create_player(self, name):
        # 1. Validate Input (Business Logic)
        if not name:
            return "Invalid Name"
        
        # 2. Create Model Object
        new_player = Player(name=name)

        # 3. Pass to Data Layer
        return self.data_wrapper.write_player(new_player)