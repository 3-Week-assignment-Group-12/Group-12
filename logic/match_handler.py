
from models.match import Match

class match_handler:
    
    def create_match(self, team1_id: int,team2_id: int,tournament_id:int ,date: str, time: str,server_id: int,winner_id: int,Score:int,existing_matches:list[Match]) -> Match | int:
        """Create a new match with basic validation.
        
        Args:
            team1_id (int): 
                ID of the first team.
            team2_id (int): 
                ID of the second team.
            tournament_id (int): 
                ID of the tournament this match belongs to.
            date (str): 
                Date of the match, expected in a dot-separated format (e.g. 'dd.mm.yyyy').
            time (str): 
                Time of the match, expected in a colon-separated format (e.g. 'hh:mm').
            server_id (int): 
                ID of the server or field where the match is played.
            winner_id (int): 
                ID of the winning team (or placeholder if not decided yet).
            Score (int): 
                Score of the match (format defined by the domain model).
            existing_matches (list[Match]): 
                List of existing matches used to determine the next unique match ID.
        
        Returns:
            Match | int:
                * Match: Newly created Match instance if validation succeeds.
                * int: Error code if validation fails:
                    - -3: Date string contains non-numeric segments.
                    - -4: Time string contains non-numeric segments.
        """
        # 1. Validate Input (Business Logic)        
        
        
        highest:int = 0
        for x in existing_matches:
            if x.id > highest:
                highest = x.id
        highest+=1 # find new id

        
        
        string_splitted_at_dots=date.split(".")
        for i in string_splitted_at_dots:
            try:
                assert type(int(i)) == int
            except:
                return -3
        
        string_splitted=time.split(":")
        for i in string_splitted:
            try:
                assert type(int(i)) == int
            except:
                return -4

        # 2. Create Model Object
        new_match = Match(highest, team1_id,team2_id,tournament_id,date, time,server_id,winner_id,Score)
        
        

        # 3. Pass to Data Layer
        return new_match