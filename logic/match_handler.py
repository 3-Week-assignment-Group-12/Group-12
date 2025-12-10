
from models.match import Match

class match_handler:
    
    def create_match(self, team1_id: int,team2_id: int,tournament_id:int ,date: str, time: str,server_id: int,winner_id: str,Score:int,existing_matches:list[Match]) -> Match | int:
        # 1. Validate Input (Business Logic)        

        if not all(isinstance(x, int) for x in [team1_id, team2_id, tournament_id, server_id, winner_id, Score]):
            return -2
        
        if team1_id == team2_id:
            return -3 
        
        try:
            day, month, year = [int(x) for x in date.split(".")]
        except ValueError:
            return -4
        
        try:
            hour, minute = [int(x) for x in time.split(":")]
        except ValueError:
            return -5

        highest = 0
        for x in existing_matches:
            if x.id > highest:
                highest = x.id
        highest += 1

        # 2. Create Model Object
        new_match = Match(highest, team1_id,team2_id,tournament_id,date, time,server_id,winner_id,Score)

        # 3. Pass to Data Layer
        return new_match