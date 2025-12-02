# logic_layer/logic_wrapper.py
from data.data_wrapper import DataWrapper
from logic.player_handler import player_handler
from models.player import Player

class LogicWrapper:
    def __init__(self):
        # Logic creates an instance of the Data Wrapper
        self.data_wrapper = DataWrapper()
        self.player_handler = player_handler()
        
    def create_player(self,KT,name,dob,phone,address,email):
        return self.player_handler.create_player(KT,name,dob,phone,address,email,playerList)

