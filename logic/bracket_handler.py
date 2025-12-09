
from models.bracket import Bracket

class bracket_handler:
    
    def create_bracket(self, matchups: list[tuple[int,int]] ,tournament_id:int, existing_brackets:list[Bracket]) -> Bracket:
        
        # 1. Validate Input (Business Logic)        
        
        highest:int = 0
        for x in existing_brackets:
            if x.id > highest:
                highest = x.id
        highest+=1 # find new id
        
        # 2. Create Model Object
        new_bracket = Bracket(highest, matchups ,tournament_id)

        # 3. Pass to Data Layer
        return new_bracket