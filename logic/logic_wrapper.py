# logic_layer/logic_wrapper.py
from data.data_wrapper import DataWrapper
from logic.player_handler import player_handler
from models.player import Player

class LogicWrapper:
    def __init__(self):
        # Logic creates an instance of the Data Wrapper
        self.data_wrapper = DataWrapper()

