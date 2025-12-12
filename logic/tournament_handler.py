
from models.match import Match
from models.tournament import Tournament

class tournament_handler:
    
    def create_tournament(self, name:str, start_date:str, end_date:str, venue:str, contact_id:str, contact_email:str, contact_phone:str,existing_tournaments: list[Tournament] , team_list:list[int],matches:list[list[int]]) -> Tournament| int:
        """ Create a new tournament with validation.
        
        Args:
            name (str):
                Name of the tournament.
            start_date (str):
                Tournament start date, expected in dot-separated format (e.g., 'dd.mm.yyyy').
            end_date (str):
                Tournament end date, same format as start_date.
            venue (str):
                Venue or location of the tournament.
            contact_id (str):
                National ID of the main organizer. Must be 10 characters.
            contact_email (str):
                Email address of the organizer. Must contain exactly one '@'.
            contact_phone (str):
                Phone number of the organizer. Must be a 7-digit string.
            existing_tournaments (list[Tournament]):
                Used to determine the next unique tournament ID.
            team_list (list[int]):
                List of participating team IDs.
            matches (list[list[int]]):
                Nested list representing match IDs grouped by tournament rounds.
        
        Returns:
            Tournament | int:
                * Tournament: A newly created Tournament instance if validation succeeds.
                * int: Error code if validation fails:
                    - -2: Invalid contact_id length.
                    - -4: Invalid email format (must contain exactly one '@').
                    - -5: contact_phone must be a 7-digit string.
                    - -6: start_date contains non-numeric segments.
        """
        # 1. Validate Input (Business Logic)        
        if len(contact_id) != 10:
            return -2
        
        highest:int = 0
        for x in existing_tournaments:
            if x.id > highest:
                highest = x.id

        highest += 1 # find new id
        

        
        
        nr_of_at = 0
        for i in contact_email:
            if i =="@":
                nr_of_at+=1
            
        if nr_of_at!=1:
            return -4
        
        if not isinstance(contact_phone,str) or len(contact_phone)!=7:
            return -5
        
        string_splitted_at_dots= [int(x) for x in start_date.split(".")]
        for i in string_splitted_at_dots:
            if not isinstance(i,int):
                return -6
            
        string_splitted_at_dot= [int(x) for x in start_date.split(".")]
        for j in string_splitted_at_dot:
            if not isinstance(j,int):
                return -6
        
        # 2. Create Model Object
        new_team = Tournament(highest,name,start_date,end_date ,venue,contact_id,contact_email,contact_phone,team_list,matches)

        # 3. Pass to Data Layer
        return new_team
    
    def generate_bracket(self, tournament: Tournament, previus_matches: list[Match]) -> list[tuple[int,int]] | int:
        """Generate a knockout bracket for the tournament.
        
        Args:
            tournament (Tournament):
                Tournament instance from which bracket rules and team list are derived.
            previus_matches (list[Match]):
                List of Match objects from previous rounds, used to determine available teams.

        Returns:
            list[tuple[int, int]] | int:
                * list[tuple[int, int]]: Each tuple represents (team1_id, team2_id).
                * int: Error code defined by Tournament.generate_knockout_bracket():
                    - 2: Bracket already complete.
                    - -1: Not enough teams.
                    - -2: Odd number of teams.
        """
        return tournament.generate_knockout_bracket(previus_matches)