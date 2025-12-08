
from models.club import Club

class club_handler:
    
    def create_club(self, name: str, colour: str, location: str, team_list: list[int],existing_clubs:list[Club]) -> Club:
        # 1. Validate Input (Business Logic)        
        
        
        highest:int = 0
        for x in existing_clubs:
            if x.id > highest:
                highest = x.id
        highest+=1 # find new id
        
        # 2. Create Model Object
        new_match = Club(highest, name, colour, location, team_list)

        # 3. Pass to Data Layer
        return new_match