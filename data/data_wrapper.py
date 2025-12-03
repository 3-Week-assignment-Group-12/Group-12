from data.main_data_manager import Main_data
from models.player import Player
from models.team import Team
class DataWrapper:

    
    def __init__(self):

        self.main_data:Main_data = Main_data()
        
    def get_dummy_data(self):
        self.main_data.get_players("./dummy_data/dummy_player.csv")  
        #self.main_data.get_teams("./dummy_data/dummy_teams.csv")
        
    
    def write_player(self, new_player:Player) -> bool:
        """Writes new player instance. 
        Warning: does not vaildate"""
        
        return self.main_data.write_player(new_player)
    
    def get_players(self) -> list[Player]:
        """Returns all players written to file"""
        
        return self.main_data.get_players(self.main_data.playerFilePath)
    
    def get_teams(self) -> list[Team]:
        return self.main_data.get_teams(self.main_data.teamFilePath)
    
    def write_team(self, new_team:Team):
        return self.main_data.write_team(new_team)
    
    def view_tournaments(self):
        return self.main_data.view_tournaments
    def modify_player(self,new_data:Player):
        return self.main_data.modify_player(new_data)
    
    def modify_team(self,new_data:Team):
        return self.main_data.modify_team(new_data)

    def get_player_by_ID(self,ID):
        return self.main_data.get_players_by_ID(ID)
    
    def delete_player(self,ID):
        return self.main_data.delete_player(ID)
    
    
