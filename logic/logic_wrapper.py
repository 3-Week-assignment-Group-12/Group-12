# logic_layer/logic_wrapper.py
from data.data_wrapper import DataWrapper
from logic.player_handler import player_handler
from logic.team_handler import team_handler
from logic.tournament_handler import tournament_handler
from logic.match_handler import match_handler
from models.tournament import Tournament
from models.player import Player
from models.team import Team
from models.match import Match


class LogicWrapper:
    def __init__(self):
        """Initialize LogicWrapper with DataWrapper and handler instances."""
        # Logic creates an instance of the Data Wrapper
        self.data_wrapper = DataWrapper()
        self.player_handler = player_handler()
        self.team_handler = team_handler()
        self.tournament_handler = tournament_handler()
        self.match_handler = match_handler()
        
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
        
    def create_match(self, team1_id: int,team2_id: int,tournament_id:int,date: str, time: str,server_id: int,winner_id: int,Score:int) -> bool:
        """Create a new match with validation.
        
        Args:
            match_id: int
            team1_id: int
            team2_id: int
            date: str
            match time: str
            server_id: int
            winner_id: int | None
            Score:int
            
        Returns:
            bool: Success status
        """
        new_match: Match|bool = self.match_handler.create_match(team1_id,team2_id,tournament_id,date, time,server_id,winner_id,Score,self.data_wrapper.get_matches())
        if type(new_match) == Match:
            return self.data_wrapper.write_match(new_match)
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

    def get_turnaments(self):
        """Retrieve all tournaments.
        
        Returns:
            list: List of tournaments
        """
        return self.data_wrapper.get_tournaments()
    
    def modify_player(self, new_data: Player) -> bool:
        """Modify an existing player's data.
        
        Args:
            new_data (Player): Updated player instance
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.modify_player(new_data)
    
    def modify_match(self, new_data: Match) -> bool:
        """Modify an existing Match's data.
        
        Args:
            new_data (PlMatchayer): Updated Match instance
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.modify_match(new_data)
    
    def get_player_by_ID(self, ID: int) -> Player|bool:
        """Retrieve a player by their ID.
        
        Args:
            ID (int): Player ID
            
        Returns:
            Player|bool: Player instance if found, False otherwise
        """
        return self.data_wrapper.get_player_by_ID(ID)

    def get_match_by_ID(self, ID: int) -> Match|bool:
        """Retrieve a match by their ID.
        
        Args:
            ID (int): match ID
            
        Returns:
            Match|bool: Match instance if found, False otherwise
        """
        return self.data_wrapper.get_match_by_ID(ID)
    
    def delete_player(self, ID: int) -> bool:
        """Delete a player by their ID.
        
        Args:
            ID (int): Player ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_player(ID)
    
    def delete_match(self, ID: int) -> bool:
        """Delete a match by their ID.
        
        Args:
            ID (int): match ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_match(ID)
    
    def create_tournament(self, name: str, start_date: str, end_date: str,  venue:str, contact_id:int, contact_email:str, contact_phone: int, team_list: list[int], matches:list[int]) -> bool:
        """Create a new tournament with validation.
        
        Args:
            name (str): Tournament name
            start_date (str): Tournament start date
            end_date (str): Tournament end date
            description (str): Tournament description (optional)
            
        Returns:
            bool: Success status
        """
        new_tournament: Tournament|bool = self.tournament_handler.create_tournament(name, start_date, end_date, venue, contact_id, contact_email, contact_phone, self.data_wrapper.get_tournaments(),team_list,matches)
        if type(new_tournament) == Tournament:
            return self.data_wrapper.write_tournament(new_tournament)
        else:
            return False
    
    def modify_tournament(self, new_data: Tournament) -> bool:
        """Modify an existing tournament's data.
        
        Args:
            new_data (Tournament): Updated tournament instance
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.main_data.modify_tournament(new_data)
    
    def delete_tournament(self, ID: int) -> bool:
        """Delete a tournament by its ID.
        
        Args:
            ID (int): Tournament ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_tournament(ID)
    
    def get_tournament_by_ID(self, ID: int) -> Tournament|bool:
        """Retrieve a tournament by its ID.
        
        Args:
            ID (int): Tournament ID
            
        Returns:
            Tournament|bool: Tournament instance if found, False otherwise
        """
        return self.data_wrapper.get_tournament_by_ID(ID)

    
    def get_team_by_ID(self, ID: int) -> Team|bool:
        """Retrieve a team by its ID.
        
        Args:
            ID (int): Team ID
            
        Returns:
            Team|bool: Team instance if found, False otherwise
        """
        return self.data_wrapper.get_team_by_ID(ID)
    
    
    def generate_bracket(self, tournament: Tournament, preveus_matches: list[Match]) -> list[tuple[int, int]] | int:
        """Generate a knockout bracket for a tournament.
        
        Args:
            tournament (Tournament): Tournament instance
            preveus_matches (list[Match]): List of previous matches
            
        Returns:
            list[tuple[int, int]] | int: Generated bracket as a list of team ID pairs or error code
            int if an error occurs
            
        Errors:
            -1: Not enough teams to form a bracket
            -2: Odd number of teams cannot form pairs
        """
        
        return self.tournament_handler.generate_bracket(tournament, preveus_matches)