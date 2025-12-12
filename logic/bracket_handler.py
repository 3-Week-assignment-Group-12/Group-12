
from models.bracket import Bracket

class bracket_handler:
    
    def create_bracket(self, matchups: list[tuple[int,int]] ,tournament_id:int, existing_brackets:list[Bracket]) -> Bracket:
        """Create a new bracket for a tournament.
        
        Args:
            matchups (list[tuple[int, int]]): 
                List of matchups, each represented as a tuple of two team IDs.
            tournament_id (int): 
                ID of the tournament this bracket belongs to.
            existing_brackets (list[Bracket]): 
                List of existing brackets used to determine the next unique ID.
        
        Returns:
            Bracket: Newly created Bracket instance.
        """
        # 1. Validate Input (Business Logic)        
        
        highest:int = 0
        for x in existing_brackets:
            if x.id > highest:
                highest = x.id

        highest += 1 # Assign next unique ID
        
        # 2. Create Model Object
        new_bracket = Bracket(highest, matchups ,tournament_id)
        # 3. Pass to Data Layer (handled by LogicWrapper)
        return new_bracket