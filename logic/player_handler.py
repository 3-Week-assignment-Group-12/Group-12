
from models.player import Player
import datetime

class player_handler:
    
    def create_player(self, ID:int ,name:str ,phone: int,address: str,email:str, existing_playerList:list[Player]) ->Player| bool:
        # 1. Validate Input (Business Logic)        
        if len(str(ID)) != 10: ##validate length of ID
            return False
        
        
        for p in existing_playerList:
            if p.id == ID or p.phone == phone or p.email == email:
                return False
        
        
        dob = datetime.date(day=int(str(ID)[0:1]), month=int(str(ID)[2:3]), year=int(str(ID)[4:5])).__str__()
        # 2. Create Model Object
        new_player = Player(ID,name,dob,phone,address,email)

        # 3. Pass to Data Layer
        return new_player