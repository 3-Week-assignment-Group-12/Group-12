from data.main_data_manager import Main_data
from models.player import Player
from models.team import Team
from models.tournament import Tournament
class DataWrapper:

    
    def __init__(self):
        """Initialize DataWrapper with a Main_data instance."""
        self.main_data:Main_data = Main_data()
        
    def get_dummy_data(self):
        """Load dummy data from CSV files for testing purposes."""
        self.main_data.get_players("./dummy_data/dummy_player.csv")  
        #self.main_data.get_teams("./dummy_data/dummy_teams.csv") dummy teams are broken
        
    
    def write_player(self, new_player:Player) -> bool:
        """Write a new player instance to file.
        
        Warning: does not validate input data.
        
        Args:
            new_player (Player): Player instance to write
            
        Returns:
            bool: Success status
        """
        return self.main_data.write_player(new_player)
    
    def get_players(self) -> list[Player]:
        """Retrieve all players from file.
        
        Returns:
            list[Player]: List of all players
        """
        return self.main_data.get_players(self.main_data.playerFilePath)
    
    def get_teams(self) -> list[Team]:
        """Retrieve all teams from file.
        
        Returns:
            list[Team]: List of all teams
        """
        return self.main_data.get_teams(self.main_data.teamFilePath)
    
    def write_team(self, new_team:Team) -> bool:
        """Write a new team instance to file.
        
        Args:
            new_team (Team): Team instance to write
            
        Returns:
            bool: Success status
        """
        return self.main_data.write_team(new_team)
    
    def modify_player(self, new_data:Player) -> bool:
        """Modify an existing player's data.
        
        Args:
            new_data (Player): Updated player instance
            
        Returns:
            bool: Success status
        """
        return self.main_data.modify_player(new_data)
    
    def get_tournaments(self) -> list[Tournament]:
        return self.main_data.get_tournaments(self.main_data.tournamentFilePath)
    
    def write_tournament(self, new_tournament:Tournament) -> bool:
        """Write a new tournament instance to file.
        
        Args:
            new_tournament (Tournament): Tournament instance to write
            
        Returns:
            bool: Success status
        """
        return self.main_data.write_tournament(new_tournament)
    
    
    def modify_team(self, new_data:Team) -> bool:
        """Modify an existing team's data.
        
        Args:
            new_data (Team): Updated team instance
            
        Returns:
            bool: Success status
        """
        return self.main_data.modify_team(new_data)

    def get_player_by_ID(self, ID) -> Player|bool:
        """Retrieve a player by their ID.
        
        Args:
            ID: Player ID
            
        Returns:
            Player: Player instance matching the ID
        """
        return self.main_data.get_players_by_ID(ID)
    
    def delete_player(self, player_id:int) -> bool:
        """Delete a player by their ID.
        
        Args:
            player_id (int): ID of player to delete
            
        Returns:
            bool: Success status
        """
        return self.main_data.delete_player(player_id)
    
    def delete_team(self, team_id:int) -> bool:
        """Delete a team by ID.

        Args:
            team_id (int): ID of team to delete

        Returns:
            bool: Success status
        """
        return self.main_data.delete_team(team_id)
