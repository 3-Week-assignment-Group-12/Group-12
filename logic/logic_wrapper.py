# logic_layer/logic_wrapper.py
from data.data_wrapper import DataWrapper
from logic.player_handler import player_handler
from logic.team_handler import team_handler
from logic.tournament_handler import tournament_handler
from logic.match_handler import match_handler
from logic.bracket_handler import bracket_handler
from models.tournament import Tournament
from models.player import Player
from models.team import Team
from models.match import Match
from models.bracket import Bracket



class LogicWrapper:
    def __init__(self):
        """Initialize LogicWrapper with DataWrapper and handler instances."""
        # Logic creates an instance of the Data Wrapper
        self.data_wrapper = DataWrapper()
        self.player_handler = player_handler()
        self.team_handler = team_handler()
        self.tournament_handler = tournament_handler()
        self.match_handler = match_handler()
        self.bracket_handler = bracket_handler()
        
        
        
    # ------------------- Create Methods ------------------ #
    
    def create_player(self, KT, name, phone, address, email) -> bool:
        
        """Create a new player with validation.
        
        Args:
            KT (int): Player's KT number
            name (str): Player's name
            phone (int): Player's phone number
            address (str): Player's address
            email (str): Player's email
            
        Returns:
            bool: Success status
        """
        
        new_player = self.player_handler.create_player(KT, name, phone, address, email, self.data_wrapper.get_players())
        
        if isinstance(new_player, Player):
            return self.data_wrapper.write_player(new_player)
        return False
        
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
        if isinstance(new_team, Team):
            return self.data_wrapper.write_team(new_team)
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
        
        if isinstance(new_match, Match):
            return self.data_wrapper.write_match(new_match)
        return False
    
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
        
        if isinstance(new_tournament, Tournament):
            return self.data_wrapper.write_tournament(new_tournament)
        return False 

        
    
    # ------------------- Read Methods ------------------ #
    def get_players(self) -> list[Player]:
        return self.data_wrapper.get_players()  # returns a list of Player    
    
    
    def get_teams(self) -> list[Team]:
        """Retrieve all teams.
        
        Returns:
            list[Team]: List of all teams
        """
        return self.data_wrapper.get_teams()

    def get_tournaments(self):
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
    
    def modify_tournament(self, new_data: Tournament) -> bool:
        """Modify an existing tournament's data.
        
        Args:
            new_data (Tournament): Updated tournament instance
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.modify_tournament(new_data)
    
    
    
    
    # ------------------- Get by ID Methods ------------------ #
    
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
    
    def get_matches_by_tournament_ID(self, ID:int) -> list[Match]:
        """Retrieve matches by tournament ID.
        
        Args:
            ID (int): Tournament ID
            
        Returns:
            list[Match]: List of Match instances for the tournament
        """
        return self.data_wrapper.get_matches_by_tournament_ID(ID)
    
    def get_players_by_team_ID(self, ID:int) -> list[Player] | bool:
        """Retrieve players by team ID.
        
        Args:
            ID (int): Team ID
            
        Returns:
            list[Player]: List of Player instances in the team
            or False if error occurs
        """
        return self.data_wrapper.get_players_by_team_ID(ID)
    
    def get_bracket_by_ID(self, ID: int) -> Bracket|bool:
        """Retrieve a bracket by its ID.
        
        Args:
            ID (int): Bracket ID
            
        Returns:
            Bracket|bool: Bracket instance if found, False otherwise
        """
        return self.data_wrapper.get_bracket_by_ID(ID)

    
    
    # ------------------- Delete Methods ------------------ #
    def delete_player(self, ID: int) -> bool:
        """Delete a player by their ID.
        
        Args:
            ID (int): Player ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_player(ID)
    
    def delete_team(self, ID: int) -> bool:
        """Delete a team by their ID.
        
        Args:
            ID (int): Team ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_team(ID)
    
    def delete_bracket(self, ID: int) -> bool:
        """Delete a bracket by their ID.
        
        Args:
            ID (int): Bracket ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_bracket(ID)
    
    def delete_tournament(self, ID: int) -> bool:
        """Delete a tournament by its ID.
        
        Args:
            ID (int): Tournament ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_tournament(ID)
    
    def delete_match(self, ID: int) -> bool:
        """Delete a match by their ID.
        
        Args:
            ID (int): match ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_match(ID)
    

    
    
        
    
    # ------------------- Specialized Methods ------------------ #
    def generate_bracket(self, tournament: Tournament,) -> list[tuple[int, int]] | int:
        """Generate a knockout bracket for a tournament.
        
        Args:
            tournament (Tournament): Tournament instance
            
        Returns:
            list[tuple[int, int]] | int: Generated bracket as a list of team ID pairs or error code
            int if an error occurs
            
        Errors:
            -1: Not enough teams to form a bracket
            -2: Odd number of teams cannot form pairs
        """
        
        return self.tournament_handler.generate_bracket(tournament, self.data_wrapper.get_matches_by_tournament_ID(tournament.id))
    

    def get_clubs(self):
        """Retrieve all clubs.
        
        Returns:
            list[Clubs]: List of all clubs
        """
        #return self.data_wrapper.get_clubs()
        return
    
    def inputplayersID(self):
        playersID=int(input("Enter National ID: "))
        check= self.get_player_by_ID(playersID)
        while check is False:
            print("Player does not exist, Try different ID")
            playersID=int(input("Enter National ID: "))
            check= self.get_player_by_ID(playersID)
        return playersID
    
    def inputTeamID(self):
        teamID=int(input("Enter Team ID: "))
        check= self.get_team_by_ID(teamID)
        while check is False:
            print("Team does not exist, Try different ID")
            teamID=int(input("Enter Team ID: "))
            check= self.get_team_by_ID(teamID)
        return teamID
    

    def delete_team(self, ID: int) -> bool:
        """Delete a team by their ID.
        
        Args:
            ID (int): Team ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_team(ID)
    


    def inputTournamentID(self):
        tournamentID=int(input("Enter Tournament ID: "))
        check= self.get_tournament_by_ID(tournamentID)
        while check is False:
            print("Tournament does not exist, Try different ID")
            tournamentID=int(input("Enter Tournament ID: "))
            check= self.get_tournament_by_ID(tournamentID)
        return tournamentID
    

    def delete_tournament(self, ID: int) -> bool:
        """Delete a team by their ID.
        
        Args:
            ID (int): Team ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_tournament(ID)
    
    #--------------team checks --------------------
    def check_for_team_name(self,name):
        list_of_teams=self.get_teams()
        for teamID in list_of_teams:
            teaminfo=self.get_team_by_ID(teamID.id)
            if isinstance(teaminfo,Team):
                if name == teaminfo.name:
                    return False
                else:
                    return True
            
    def check_for_team_tag(self,tag):
        list_of_teams=self.get_teams()
        for teamID in list_of_teams:
            teaminfo=self.get_team_by_ID(teamID.id)
            if isinstance(teaminfo,Team):
                if tag == teaminfo.tag: 
                    return False
                else:
                    return True
    #--------------Player checks --------------------
    def check_for_player_kt(self,kt):
        list_of_players=self.get_players()
        for player in list_of_players:
            playerinfo=self.get_team_by_ID(player.kt)
            if isinstance(playerinfo,Player):
                if kt == playerinfo.kt: 
                    return False
                else:
                    return True
    
    #--------------Tournament checks --------------------
                
    def check_for_tournament_ID(self,ID):
        list_of_tournaments=self.get_tournaments()
        for tournamentID in list_of_tournaments:
            tournament_info=self.get_team_by_ID(tournamentID.id)
            if isinstance(tournament_info,Tournament):
                if ID == tournament_info.id: 
                    return False
                else:
                    return True
    
