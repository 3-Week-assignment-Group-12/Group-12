from data.json_repository import JsonRepository
from models.match import Match
from models.player import Player
from models.team import Team
from models.bracket import Bracket
from models.tournament import Tournament
from models.club import Club
import os

class DataWrapper:

    
    def __init__(self):
        """Initialize DataWrapper with a Main_data instance."""
        #self.main_data:Main_data = Main_data()
        
        self.player_repo = JsonRepository(Player)
        self.team_repo = JsonRepository(Team)
        self.tournament_repo = JsonRepository(Tournament)
        self.match_repo = JsonRepository(Match)
        self.bracket_repo = JsonRepository(Bracket)
        self.club_repo = JsonRepository(Club)
        
        
        
    def get_dummy_data(self):
        """Load dummy data from CSV files for testing purposes."""  # csv crud is deprecated
        
        
        
        
        self.list_load(self.player_repo.read_dummy_data("./dummy_data/player_data.json"),self.player_repo)
        self.list_load(self.tournament_repo.read_dummy_data("./dummy_data/tournament_data.json"),self.tournament_repo)
        self.list_load(self.match_repo.read_dummy_data("./dummy_data/match_data.json"),self.match_repo)
        self.list_load(self.club_repo.read_dummy_data("./dummy_data/club_data.json"),self.club_repo)
        self.list_load(self.bracket_repo.read_dummy_data("./dummy_data/bracket_data.json"),self.bracket_repo)
        self.list_load(self.team_repo.read_dummy_data("./dummy_data/team_data.json"),self.team_repo)
        
        
        
        
        
        
        
    def list_load(self, list: list, repo:JsonRepository):
        for x in list:
            repo.create(x)
        
    
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
        """Retrieve all Clubs from file.
        
        Returns:
            list[Club]: List of tournaments
        """
        return self.bracket_repo.read()
    
    def get_clubs(self) -> list[Club]:
        """Retrieve all Clubs from file.
        
        Returns:
            list[Club]: List of Clubs
        """
        
        
        return self.club_repo.read()
    
    
    # ------------------- Create Methods ------------------ #
    
    def write_team(self, new_team:Team):
        """Write a new team instance to file.
        
        Args:
            new_team (Team): Team instance to write
            
        Returns:
            bool: Success status
        """
        return self.team_repo.create(new_team)
    

    def write_player(self, new_player:Player) -> int:
        """Write a new player instance to file.
        
        Args:
            new_player (Player): Player instance to write
            
        Returns:
            int: Success status
        """
        return self.player_repo.create(new_player)
    
    
    def write_tournament(self, new_tournament:Tournament) -> int:
        """Write a new tournament instance to file.
        
        Args:
            new_tournament (Tournament): Tournament instance to write
            
        Returns:
            int: Success status
        """
        return self.tournament_repo.create(new_tournament)
    
    def write_match(self, new_match:Match) -> int:
        """Write a new match instance to file.
        
        Args:
            new_match (Match): match instance to write
            
        Returns:
            int: Success status
        """
        return self.match_repo.create(new_match)
    
    
    def write_bracket(self, new_bracket:Bracket) -> int:
        """Write a new bracket instance to file.
        
        Args:
            new_bracket (Bracket): Bracket instance to write
            
        Returns:
            int: Success status
        """
        return self.bracket_repo.create(new_bracket)
    
    def write_club(self, new_club:Club) -> int:
        """Write a new club instance to file.
        
        Args:
            new_club (Club): Club instance to write
            
        Returns:
            int: Success status
        """
        return self.club_repo.create(new_club)
    
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
        return self.player_repo.update(lambda x: x.id == new_data.id, lambda x: new_data)
    
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
    
    def modify_club(self, new_data:Club) -> bool:
        """Modify an existing club's data.
        
        Args:
            new_data (Club): Updated club instance
            
        Returns:
            bool: Success status
        """
        return self.club_repo.update(lambda x: x.id == new_data.id, lambda x: new_data)
    
    
    
    # ------------------- Get by id Methods ------------------ #
    

    def get_player_by_ID(self, ID) -> Player|int:
        """Retrieve a player by their ID.
        
        Args:
            ID: Player ID
            
        Returns:
            Player|int: Player instance if found, False otherwise
        """
        try:
            return self.player_repo.read(lambda x: x.id == ID)[0]
        except IndexError:
            return -2 # error reading data
    
    def get_team_by_ID(self, ID:int) -> Team|bool:
        """Retrieve a team by its ID.
        
        Args:
            ID (int): Team ID
            
        Returns:
            Team|bool: Team instance if found, False otherwise
        """
        try:
            return self.team_repo.read(lambda x: x.id == ID)[0]
        except IndexError:
            return False
    
    def get_tournament_by_ID(self, ID:int) -> Tournament|bool:
        """Retrieve a tournament by its ID.
        
        Args:
            ID (int): Tournament ID
            
        Returns:
            Tournament|bool: Tournament instance if found, False otherwise
        """
        try:
            return self.tournament_repo.read(lambda x: x.id == ID)[0]
        except IndexError:
            return False
    
    
    def get_match_by_ID(self, ID:int) -> Match|bool:
        """Retrieve a tournament by its ID.
        
        Args:
            ID (int): Match ID
            
        Returns:
            Match|bool: Match instance if found, False otherwise
        """
        try:
            return self.match_repo.read(lambda x: x.id == ID)[0]
        except IndexError:
            return False
    
    def get_bracket_by_ID(self, ID:int) -> Bracket|bool:
        """Retrieve a bracket by its ID.
        
        Args:
            ID (int): Bracket ID
            
        Returns:
            Bracket|bool: Bracket instance if found, False otherwise
        """
        try:
            return self.bracket_repo.read(lambda x: x.id == ID)[0]
        except IndexError:
            return False
    
    def get_club_by_ID(self, ID:int) -> Club|bool:
        """Retrieve a club by its ID.
        
        Args:
            ID (int): club ID
            
        Returns:
            club|bool: club instance if found, False otherwise
        """
        try:
            return self.club_repo.read(lambda x: x.id == ID)[0]
        except IndexError:
            return False
    
    
    
    
    # ------------------- Get X by Y Methods ------------------ #
    
    def get_matches_by_tournament_ID(self, tournament_id:int) -> list[Match]:
        """Retrieve all matches for a specific tournament ID.
        
        Args:
            tournament_id (int): Tournament ID to filter matches
        Returns:
            list[Match]: List of matches for the specified tournament
        """
        return self.match_repo.read(lambda x: x.tournament_id == tournament_id)
    
    def get_bracket_by_tournament_ID(self, tournament_id:int) -> list[Bracket]:
        """Retrieve bracket by tournament ID.
        
        Args:
            tournament_id (int): Tournament ID to filter brackets
        Returns:
            list[Match]: List of matches for the specified tournament
        """
        return self.bracket_repo.read(lambda x: x.tournament_id == tournament_id)
    
    
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
        
        
    def get_teams_by_club_ID(self, club_id:int) -> list[Team] | bool:
        """Retrieve all teams for a specific club ID.
        
        Args:
            club_id (int): club ID to filter players
        
        Returns:
            list[Team]: List of teams for the specified club
        """
        
        club = self.get_club_by_ID(club_id)
        if isinstance(club, bool):
            return False
        else:
            return self.club_repo.read(lambda x: x.id in [p for p in club.teams])
    
    def get_team_by_tournament_ID(self, tournament_id:int) -> list[Team] | bool:
        """Retrieve all teams for a specific tournament ID.
        
        Args:
            tournament (int): tournament ID to filter teams
        
        Returns:
            list[Team]: List of teams for the specified tournamnet
        """
        
        tournmaent = self.get_tournament_by_ID(tournament_id)
        if isinstance(tournmaent, bool):
            return False
        else:
            return self.team_repo.read(lambda x: x.id in [p for p in tournmaent.team_list])
            
    
    # ------------------- Delete Methods ------------------ #
    
    
    def delete_player(self, player_id:str) -> bool:
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
    
    def delete_club(self, club_id:int) -> bool:
        """Delete a club by ID.

        Args:
            club_id (int): ID of club to delete

        Returns:
            bool: Success status
        """
        return self.bracket_repo.delete(lambda x: x.id == club_id)