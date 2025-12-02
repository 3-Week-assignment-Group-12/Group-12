
from models.player import Player
import datetime

class player_handler:
    
    def create_player(self, KT:int ,name:str ,phone: int,address: str,email:str, playerList:list[Player]) ->Player| bool:
        # 1. Validate Input (Business Logic)        
        if len(str(KT)) != 10: ##validate length of KT
            return False
        
        
        for x in playerList:
            if x.kt == KT or x.phone == phone or x.email == email:
                return False
        
        
        dob = datetime.date(day=int(str(KT)[0:1]), month=int(str(KT)[2:3]), year=int(str(KT)[4:5])).__str__()
        # 2. Create Model Object
        new_player = Player(KT,name,dob,phone,address,email)

        # 3. Pass to Data Layer
        return new_player