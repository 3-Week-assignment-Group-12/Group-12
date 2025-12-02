# logic_layer/logic_wrapper.py
from data.data_wrapper import DataWrapper
from logic.player_handler import player_handler
from logic.team_handler import team_handler
from models.player import Player
from models.team import Team


class LogicWrapper:
    def __init__(self):
        # Logic creates an instance of the Data Wrapper
        self.data_wrapper = DataWrapper()
        self.player_handler = player_handler()
        self.team_handler = team_handler()
        
    def create_player(self,KT,name,phone,address,email):
        
        #return self.player_handler.create_player(KT,name,phone,address,email,self.data_wrapper.get_players())
    
        new_player: Player|bool = self.player_handler.create_player(KT,name,phone,address,email,self.data_wrapper.get_players())
        if type(new_player) == Player:
            return self.data_wrapper.write_player(new_player)
        else:
            return False
    
    def get_players(self):
        return self.data_wrapper.get_players()
    
    
    def create_team(self,name:str, tag:str, creator_id:int, team_size:int,team_list:list[int]) ->bool:    
        new_team: Team|bool = self.team_handler.create_team(name,tag,creator_id,team_size,self.data_wrapper.get_teams(),team_list)
        if type(new_team) == Team:
            print("creating")
            return self.data_wrapper.write_team(new_team)
        else:
            print("not")
            return False
    
    
    def get_teams(self):
        return self.data_wrapper.get_teams()


