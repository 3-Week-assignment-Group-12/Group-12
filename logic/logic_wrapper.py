# logic_layer/logic_wrapper.py
from data.data_wrapper import DataWrapper
from logic.player_handler import player_handler
from logic.team_handler import team_handler
from models.player import Player
from models.team import Team


class LogicWrapper:
    def __init__(self):
        """Initialize LogicWrapper with DataWrapper and handler instances."""
        # Logic creates an instance of the Data Wrapper
        self.data_wrapper = DataWrapper()
        self.player_handler = player_handler()
        self.team_handler = team_handler()
        
    def create_player(self, KT, name, phone, address, email) -> bool:
        """Create a new player with validation.
        
        Args:
            KT: Player identification number
            name (str): Player's full name
            phone (str): Player's phone number
            address (str): Player's address
            email (str): Player's email address
            
        Returns:
            bool: Success status
        """
        new_player: Player|bool = self.player_handler.create_player(KT, name, phone, address, email, self.data_wrapper.get_players())
        if type(new_player) == Player:
            return self.data_wrapper.write_player(new_player)
        else:
            return False
    
    def get_players(self) -> list[Player]:
        """Retrieve all players.
        
        Returns:
            list[Player]: List of all players
        """
        return self.data_wrapper.get_players()
    
    
    def create_team(self, name: str, tag: str, creator_id: int, team_size: int, team_list: list[int]) -> bool:
        """Create a new team with validation.
        
        Args:
            name (str): Team name
            tag (str): Team tag/abbreviation
            creator_id (int): ID of the player creating the team
            team_size (int): Maximum team size
            team_list (list[int]): List of player IDs in the team
            
        Returns:
            bool: Success status
        """
        new_team: Team|bool = self.team_handler.create_team(name, tag, creator_id, team_size, self.data_wrapper.get_teams(), team_list)
        if type(new_team) == Team:
            print("creating")
            return self.data_wrapper.write_team(new_team)
        else:
            print("not")
            return False
    
    
    def get_teams(self) -> list[Team]:
        """Retrieve all teams.
        
        Returns:
            list[Team]: List of all teams
        """
        return self.data_wrapper.get_teams()

    def veiw_turnaments(self):
        """Retrieve all tournaments.
        
        Returns:
            list: List of tournaments
        """
        return self.data_wrapper.view_tournaments()
    
    def modify_player(self, new_data: Player) -> bool:
        """Modify an existing player's data.
        
        Args:
            new_data (Player): Updated player instance
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.modify_player(new_data)
    
    def get_player_by_ID(self, ID: int) -> Player|bool:
        """Retrieve a player by their ID.
        
        Args:
            ID (int): Player ID
            
        Returns:
            Player|bool: Player instance if found, False otherwise
        """
        return self.data_wrapper.get_player_by_ID(ID)
    
    def delete_player(self, ID: int) -> bool:
        """Delete a player by their ID.
        
        Args:
            ID (int): Player ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_player(ID)
    
"""    def get_team_by_ID(self,ID):
        return 
    def get_all_teams_in_tournament(self,ID): 
        return self.data_wrapper."""