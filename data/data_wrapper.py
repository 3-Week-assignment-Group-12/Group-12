from data.main_data_manager import Main_data
from models.player import Player
from models.team import Team
class DataWrapper:

    
    def __init__(self):

        self.main_data:Main_data = Main_data()
        
    
    def write_player(self, new_player:Player) -> bool:
        """Writes new player instance. 
        Warning: does not vaildate"""
        
        return self.main_data.write_player(new_player)
    
    def get_players(self) -> list[Player]:
        """Returns all players written to file"""
        
        return self.main_data.get_players()
    
    def get_teams(self) -> list[Team]:
        return self.main_data.get_teams()
    
    def write_team(self, new_team:Team):
        return self.main_data.write_team(new_team)
    
    def view_tournaments(self):
        return self.main_data.view_tournaments
