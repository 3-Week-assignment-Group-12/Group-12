
from models.match import Match

class match_handler:
    
    def create_match(self, team1_id: int,team2_id: int,date: str, time: str,server_id: int,winner_id: int | None,Score:int,existing_matches:list[Match]) -> Match:
        # 1. Validate Input (Business Logic)        
        
        
        highest:int = 0
        for x in existing_matches:
            if x.match_id > highest:
                highest = x.match_id
        highest+=1 # find new id
        
        # 2. Create Model Object
        new_match = Match(highest, team1_id,team2_id,date, time,server_id,winner_id,Score)

        # 3. Pass to Data Layer
        return new_match