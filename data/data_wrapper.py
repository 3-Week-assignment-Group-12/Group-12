from data.json_repository import JsonRepository
#from data.main_data_manager import Main_data
from models.match import Match
from models.player import Player
from models.team import Team
from models.bracket import Bracket
from models.tournament import Tournament
class DataWrapper:

    
    def __init__(self):
        """Initialize DataWrapper with a Main_data instance."""
        #self.main_data:Main_data = Main_data()
        self.player_repo = JsonRepository(Player)
        self.team_repo = JsonRepository(Team)
        self.tournament_repo = JsonRepository(Tournament)
        self.match_repo = JsonRepository(Match)
        self.bracket_repo = JsonRepository(Bracket)
        
        
    def get_dummy_data(self):
        """Load dummy data from CSV files for testing purposes."""  # csv crud is deprecated
        #self.main_data.get_players("./dummy_data/dummy_player.csv")  
        #self.main_data.get_teams("./dummy_data/dummy_teams.csv")
        #self.main_data.get_tournaments("./dummy_data/dummy_tournaments.csv") no data available
        #self.main_data.get_matches("./dummy_data/dummy_matches.csv") no data available
        pass
        
    
    # ------------------- Read Methods ------------------ #

    def get_players(self):
        """Retrieve all players from file.
        
        Returns:
            list[Player]: List of all Players
        """
        return self.player_repo.read()
    
    def get_matches(self) -> list[Match]:
        """Retrieve all matches from file.
        
        Returns:
            list[PlMatchayer]: List of all Matches
        """
        return self.match_repo.read()
    
    def get_teams(self) -> list[Team]:
        """Retrieve all teams from file.
        
        Returns:
            list[Team]: List of all teams
        """
        return self.team_repo.read()
    
    def get_tournaments(self) -> list[Tournament]:
        """Retrieve all tournaments from file.
        
        Returns:
            list[Tournament]: List of tournaments
        """
        return self.tournament_repo.read()
    


    def get_brackets(self) -> list[Bracket]:
        """Retrieve all brackets from file.
        
        Returns:
            list[Bracket]: List of brackets
        """
        return self.bracket_repo.read()
    
    # ------------------- Create Methods ------------------ #
    
    def write_team(self, new_team:Team):
        """Write a new team instance to file.
        
        Args:
            new_team (Team): Team instance to write
            
        Returns:
            bool: Success status
        """
        return self.team_repo.create(new_team)
    

    def write_player(self, new_player:Player) -> bool:
        """Write a new player instance to file.
        
        Args:
            new_player (Player): Player instance to write
            
        Returns:
            bool: Success status
        """
        return self.player_repo.create(new_player)
    
    
    def write_tournament(self, new_tournament:Tournament) -> bool:
        """Write a new tournament instance to file.
        
        Args:
            new_tournament (Tournament): Tournament instance to write
            
        Returns:
            bool: Success status
        """
        return self.tournament_repo.create(new_tournament)
    
    def write_match(self, new_match:Match) -> bool:
        """Write a new match instance to file.
        
        Args:
            new_match (Match): match instance to write
            
        Returns:
            bool: Success status
        """
        return self.match_repo.create(new_match)
    
    
    def write_bracket(self, new_bracket:Bracket) -> bool:
        """Write a new bracket instance to file.
        
        Args:
            new_bracket (Bracket): Bracket instance to write
            
        Returns:
            bool: Success status
        """
        return self.bracket_repo.create(new_bracket)
    
    # ------------------- Modify Methods ------------------ #
    
    def modify_team(self, new_data:Team) -> bool:
        """Modify an existing team's data.
        
        Args:
            new_data (Team): Updated team instance
            
        Returns:
            bool: Success status
        """
        return self.team_repo.update(lambda x: x.id == new_data.id, lambda x: new_data)
    
    def modify_match(self, new_data:Match) -> bool:
        """Modify an existing match's data.
        
        Args:
            new_data (Match): Updated match instance
            
        Returns:
            bool: Success status
        """
        return self.match_repo.update(lambda x: x.id == new_data.id, lambda x: new_data)

    def modify_player(self, new_data:Player) -> bool:
        """Modify an existing player's data.
        
        Args:
            new_data (Player): Updated player instance
            
        Returns:
            bool: Success status
        """
        return self.player_repo.update(lambda x: x.kt == new_data.id, lambda x: new_data)
    
    def modify_tournament(self, new_data:Tournament) -> bool:
        """Modify an existing tournament's data.
        
        Args:
            new_data (Tournament): Updated tournament instance
            
        Returns:
            bool: Success status
        """
        return self.tournament_repo.update(lambda x: x.id == new_data.id, lambda x: new_data)
    
    def modify_bracket(self, new_data:Bracket) -> bool:
        """Modify an existing bracket's data.
        
        Args:
            new_data (Bracket): Updated bracket instance
            
        Returns:
            bool: Success status
        """
        return self.bracket_repo.update(lambda x: x.id == new_data.id, lambda x: new_data)
    
    
    
    # ------------------- Get by id Methods ------------------ #
    

    def get_player_by_ID(self, ID) -> Player|bool:
        """Retrieve a player by their ID.
        
        Args:
            ID: Player ID
            
        Returns:
            Player|bool: Player instance if found, False otherwise
        """
        return self.player_repo.read(lambda x: x.id == ID)[0] or False
    
    def get_team_by_ID(self, ID:int) -> Team|bool:
        """Retrieve a team by its ID.
        
        Args:
            ID (int): Team ID
            
        Returns:
            Team|bool: Team instance if found, False otherwise
        """
        return self.team_repo.read(lambda x: x.id == ID)[0] or False
    
    def get_tournament_by_ID(self, ID:int) -> Tournament|bool:
        """Retrieve a tournament by its ID.
        
        Args:
            ID (int): Tournament ID
            
        Returns:
            Tournament|bool: Tournament instance if found, False otherwise
        """
        return self.tournament_repo.read(lambda x: x.id == ID)[0] or False
    
    
    
    def get_match_by_ID(self, ID:int) -> Match|bool:
        """Retrieve a tournament by its ID.
        
        Args:
            ID (int): Match ID
            
        Returns:
            Match|bool: Match instance if found, False otherwise
        """
        return self.match_repo.read(lambda x: x.id == ID)[0] or False
    
    def get_bracket_by_ID(self, ID:int) -> Bracket|bool:
        """Retrieve a bracket by its ID.
        
        Args:
            ID (int): Bracket ID
            
        Returns:
            Bracket|bool: Bracket instance if found, False otherwise
        """
        return self.bracket_repo.read(lambda x: x.id == ID)[0] or False
    
    
    
    
    # ------------------- Get X by Y Methods ------------------ #
    
    def get_matches_by_tournament_ID(self, tournament_id:int) -> list[Match]:
        """Retrieve all matches for a specific tournament ID.
        
        Args:
            tournament_id (int): Tournament ID to filter matches
        Returns:
            list[Match]: List of matches for the specified tournament
        """
        return self.match_repo.read(lambda x: x.tournament_id == tournament_id)
    
    
    def get_players_by_team_ID(self, team_id:int) -> list[Player] | bool:
        """Retrieve all players for a specific team ID.
        
        Args:
            team_id (int): Team ID to filter players
        
        Returns:
            list[Player]: List of players for the specified team
        """
        
        team = self.get_team_by_ID(team_id)
        if isinstance(team, bool):
            return False
        else:
            return self.player_repo.read(lambda x: x.id in [p for p in team.member_list])
        
    
    
    
    # ------------------- Delete Methods ------------------ #
    
    def delete_player(self, player_id:int) -> bool:
        """Delete a player by their ID.
        
        Args:
            player_id (int): ID of player to delete
            
        Returns:
            bool: Success status
        """
        return self.player_repo.delete(lambda x: x.id == player_id)
    
    def delete_team(self, team_id:int) -> bool:
        """Delete a team by ID.

        Args:
            team_id (int): ID of team to delete

        Returns:
            bool: Success status
        """
        return self.team_repo.delete(lambda x: x.id == team_id)
    
    def delete_tournament(self, tournament_id:int) -> bool:
        """Delete a tournament by ID.

        Args:
            tournament_id (int): ID of tournament to delete

        Returns:
            bool: Success status
        """
        return self.tournament_repo.delete(lambda x: x.id == tournament_id)
    
    def delete_match(self, match_id:int) -> bool:
        """Delete a match by ID.

        Args:
            match_id (int): ID of match to delete

        Returns:
            bool: Success status
        """
        return self.match_repo.delete(lambda x: x.id == match_id)
    
    def delete_bracket(self, bracket_id:int) -> bool:
        """Delete a bracket by ID.

        Args:
            bracket_id (int): ID of bracket to delete

        Returns:
            bool: Success status
        """
        return self.bracket_repo.delete(lambda x: x.id == bracket_id)