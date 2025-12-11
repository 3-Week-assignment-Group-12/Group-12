
from models.match import Match

class match_handler:
    
    def create_match(self, team1_id: int,team2_id: int,tournament_id:int ,date: str, time: str,server_id: int,winner_id: int,Score:int,existing_matches:list[Match]) -> Match | int:
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