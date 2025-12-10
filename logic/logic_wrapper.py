# logic_layer/logic_wrapper.py

from data.data_wrapper import DataWrapper
from logic.player_handler import player_handler
from logic.team_handler import team_handler
from logic.tournament_handler import tournament_handler
from logic.match_handler import match_handler
from logic.bracket_handler import bracket_handler
from logic.club_handler import club_handler
from models.tournament import Tournament
from models.player import Player
from models.team import Team
from models.match import Match
from models.bracket import Bracket
from models.club import Club



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
        self.club_handler = club_handler()
        
        
    # ------------------- Create Methods ------------------ #
    
    def create_player(self, KT, name, phone, address, email) -> int:
        
        """Create a new player with validation.
        
        Args:
            KT (int): Player's KT number
            name (str): Player's name
            phone (int): Player's phone number
            address (str): Player's address
            email (str): Player's email
            
        Returns:
            int: Success status
        """
        
        new_player = self.player_handler.create_player(KT, name, phone, address, email, self.data_wrapper.get_players())
        print("New player created:", new_player)  # Debug statement
        if isinstance(new_player, Player):
            return self.data_wrapper.write_player(new_player)
        return new_player  # Indicate failure due to validation
        
    def create_team(self, name: str, tag: str, creator_id: str, team_size: int, team_list: list[str]) -> int:
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
        new_team: Team|int = self.team_handler.create_team(name, tag, creator_id, team_size, self.data_wrapper.get_teams(), team_list)
        if isinstance(new_team, Team):
            return self.data_wrapper.write_team(new_team)
        return -2 # Indicate failure due to validation
        
        
    def create_match(self, team1_id: int,team2_id: int,tournament_id:int,date: str, time: str,server_id: int,winner_id: str,Score:int) -> int:
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
            int: Success status
        """
        new_match: Match|int = self.match_handler.create_match(team1_id,team2_id,tournament_id,date, time,server_id,winner_id,Score,self.data_wrapper.get_matches())
        
        if isinstance(new_match, Match):
            return self.data_wrapper.write_match(new_match)
        return -2 # Indicate failure due to validation
    
    def create_tournament(self, name: str, start_date: str, end_date: str,  venue:str, contact_id:str, contact_email:str, contact_phone: str, team_list: list[int], matches:list[int]) -> int:
        """Create a new tournament with validation.
        
        Args:
            name (str): Tournament name
            start_date (str): Tournament start date
            end_date (str): Tournament end date
            description (str): Tournament description (optional)
            
        Returns:
            int: Success status
        """
        new_tournament: Tournament|int = self.tournament_handler.create_tournament(name, start_date, end_date, venue, contact_id, contact_email, contact_phone, self.data_wrapper.get_tournaments(),team_list,matches)
        
        if isinstance(new_tournament, Tournament):
            return self.data_wrapper.write_tournament(new_tournament)
        return new_tournament # Indicate failure due to validation

    def create_club(self, name: str, colour:str ,location:str, team_list: list[int]) -> int:
        """Create a new club with validation.
        
        Args:
            name (str): Tournament name
            colour: str
            location: str
            team_list: list
            
        Returns:
            bool: Success status
        """
        new_club: Club|int = self.club_handler.create_club(name,colour,location,team_list,self.get_clubs())
        if isinstance(new_club, Club):
            return self.data_wrapper.write_club(new_club)
        return -2 # Indicate failure due to validation   

        
    
    # ------------------- Read Methods ------------------ #
    def get_players(self) -> list[Player]:
        return self.data_wrapper.get_players()  # returns a list of Player    
    
    
    def get_teams(self) -> list[Team]:
        """Retrieve all teams.
        
        Returns:
            list[Team]: List of all teams
        """
        return self.data_wrapper.get_teams()

    def get_match(self):
        """Retrieve all match.
        
        Returns:
            list: List of matches
        """
        return self.data_wrapper.get_tournaments()
    
    def get_tournaments(self):
        """Retrieve all tournaments.
        
        Returns:
            list: List of tournaments
        """
        return self.data_wrapper.get_tournaments()
    
    def get_clubs(self) -> list[Club]:
        """Retrieve all clubs.
        
        Returns:
            list: List of clubs
        """
        return self.data_wrapper.get_clubs()

    
    def get_brackets(self):
        """Retrieve all brackets.
        
        Returns:
            list: List of bracets
        """
        return self.data_wrapper.get_brackets()
    
    # ------------------- Get by ID Methods ------------------ #
    
    def get_player_by_ID(self, ID: str) -> Player|int:
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
    
    
    def get_bracket_by_ID(self, ID: int) -> Bracket|bool:
        """Retrieve a bracket by its ID.
        
        Args:
            ID (int): Bracket ID
            
        Returns:
            Bracket|bool: Bracket instance if found, False otherwise
        """
        return self.data_wrapper.get_bracket_by_ID(ID)

    
    def get_club_by_ID(self, ID: int) -> Club|bool:
        """Retrieve a club by its ID.
        
        Args:
            ID (int): club ID
            
        Returns:
            TClubeam|bool: club instance if found, False otherwise
        """
        return self.data_wrapper.get_club_by_ID(ID)
    
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
    
    def get_team_by_club_id(self, ID:int) -> list[Team] | bool:
        """Retrieve Team by club ID.
        
        Args:
            ID (int): club ID
            
        Returns:
            list[ClTeamub]: List of team instances in the club
            or False if error occurs
        """
        return self.data_wrapper.get_teams_by_club_ID(ID)
    
    
    def get_team_by_tournament_id(self, ID:int) -> list[Team] | bool:
        """Retrieve team by tournament ID.
        
        Args:
            ID (int): tournamnet ID
            
        Returns:
            list[Team]: List of team instances in the team
            or False if error occurs
        """
        return self.data_wrapper.get_team_by_tournament_ID(ID)
    
    
    


    
    # ------------------- Modify Methods ------------------ #
    
        
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
    
    def modify_club(self, new_data: Club) -> bool:
        """Modify an existing club's data.
        
        Args:
            new_data (club): Updated club instance
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.modify_club(new_data)
    
    def modify_team(self, new_data: Tournament) -> bool:
        """Modify an existing tournament's data.
        
        Args:
            new_data (Tournament): Updated tournament instance
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.modify_tournament(new_data)
    
    def modify_bracket(self, new_data: Bracket) -> bool:
        """Modify an existing bracket's data.
        
        Args:
            new_data (Bracket): Updated bracket instance
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.modify_bracket(new_data)
    
    
    
    
    # ------------------- Delete Methods ------------------ #
    def delete_player(self, ID: int) -> bool:
        """Delete a player by their ID.
        
        Args:
            ID (int): Player ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_player(ID)
    
    
    
    def delete_bracket(self, ID: int) -> bool:
        """Delete a bracket by their ID.
        
        Args:
            ID (int): Bracket ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_bracket(ID)
    


    def delete_team(self, ID: int) -> bool:
        """Delete a team by their ID.
        
        Args:
            ID (int): Team ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_team(ID)
    



    def delete_tournament(self, ID: int) -> bool:
        """Delete a team by their ID.
        
        Args:
            ID (int): Team ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_tournament(ID)
    
    
    
    def delete_club(self, ID: int) -> bool:
        """Delete a club by their ID.
        
        Args:
            ID (int): club ID to delete
            
        Returns:
            bool: Success status
        """
        return self.data_wrapper.delete_club(ID)
    
    
        
    
    # ------------------- Specialized Methods ------------------ #
    def generate_bracket(self, tournament: Tournament,) -> Bracket | int | None:
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
        
        bracket_data = self.tournament_handler.generate_bracket(tournament, self.data_wrapper.get_matches_by_tournament_ID(tournament.id))
        if type(bracket_data) == list[tuple[int, int]]:
            return self.bracket_handler.create_bracket(bracket_data,tournament.id,self.get_brackets())
        elif type(bracket_data) == int:
            return bracket_data
        else:
            pass
    
    
    
    

    def inputTeamID(self):
        teamID=int(input("Enter Team ID: "))
        check= self.get_team_by_ID(teamID)
        while check is False:
            print("Team does not exist, Try different ID")
            teamID=int(input("Enter Team ID: "))
            check= self.get_team_by_ID(teamID)
        return teamID
    
    


    def inputTournamentID(self):
        tournamentID=input("Enter Tournament ID(q for cancel): ")
        check= self.get_tournament_by_ID(int(tournamentID))
        while check is False:
            print("Tournament does not exist, Try different ID")
            tournamentID=input("Enter Tournament ID(q for cancel): ")
            if tournamentID.lower() == "q":
                return False
            check= self.get_tournament_by_ID(int(tournamentID))
        return tournamentID
    

    
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
    # def check_for_player_kt(self,kt):
    #     list_of_players=self.get_players()
    #     for player in list_of_players:
    #         playerinfo=self.get_player_by_ID(player.id)
    #         if isinstance(playerinfo,Player):
    #             if kt == playerinfo.id: 
    #                 return False
    #             else:
    #                 return True
                
    def valid_kt(self,NID):
        if len(str(NID)) != 10:
            return "1"
        elif NID.isalpha():
            return "2"
        elif 0 >= int(NID[0:2]) or int(NID[0:2]) > 31:
            return "3"
        elif 0 >= int(NID[2:4]) or int(NID[2:4]) > 12:
            return "4"
        else:
            return True


    def get_dummy_data(self):
        self.data_wrapper.get_dummy_data()
    def check_phone_nr(self,number):
        if len(number) != 7:
            return "1"
        elif number.isalpha() == True:
            return "2"
        else:
            return True
        
    def check_name(self,name):
        if name.isalpha() == False:
            return "1"
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
    
    def check_email(self,email):
        nr_of_at=0
        for i in email:
            if i =="@":
                nr_of_at+=1
    
        if nr_of_at!=1:
            return False
        else:
            return True
        
    def check_nID(self,NID):
        if len(str(NID)) != 10:
            return "1"
        elif NID.isalpha() ==True:
            return "2"
        else:
            return True
             
    def check_tag(self,tag):
        if len(tag) >5:
            return "-1"
        else: 
            return True
