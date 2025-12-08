
from models.player import Player
import datetime

class player_handler:
    
    def create_player(self, ID:str ,name:str ,phone: int,address: str,email:str, existing_playerList:list[Player]) ->Player| int:
        # 1. Validate Input (Business Logic)     
        if len(str(ID)) != 10:
            return -3  # Invalid ID length
        
        
        for p in existing_playerList:
            if p.id == ID or p.phone == phone or p.email == email:
                return -4  # Duplicate player found
        
        dob = "2000-01-01"  # Placeholder for date of birth


        # 2. Create Model Object
        new_player = Player(ID,name,dob,phone,address,email)

        # 3. Pass to Data Layer
        return new_player