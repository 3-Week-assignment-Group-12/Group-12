
from models.club import Club

class club_handler:
    
    def create_club(self, name: str, colour: str, team_list: list[int],existing_clubs:list[Club]) -> Club|int:
        """Create a new club with validation.
        
        Args:
            name (str):
                Name of the club.
            colour (str):
                Club colour (e.g. team colour or main colour of the club).
            team_list (list[int]):
                List of team IDs that belong to this club.
            existing_clubs (list[Club]):
                List of existing clubs used to determine the next unique ID.
        
        Returns:
            Club | int:
                - Club: Newly created Club instance if validation succeeds.
                - int: Error code if validation fails
                    * -2: Invalid type for name or colour.
        """
        # 1. Validate Input (Business Logic)        
        
        
        highest:int = 0
        for x in existing_clubs:
            if x.id > highest:
                highest = x.id
                
        highest+=1 # find new id

        if isinstance(name,int) or isinstance(colour,int):
            return -2
        
        # 2. Create Model Object
        new_match = Club(highest, name, colour, team_list)

        # 3. Pass to Data Layer
        return new_match