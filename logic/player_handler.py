
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
        
        # id format is day 2 digits,month 2 digits,year 2 digits,additional digits 3 digits and 0 for 2000 and 9 for 1900
        dob = datetime.date(int("20"+str(ID)[4:6]) if str(ID)[6] == "0" else int("19"+str(ID)[4:6]),
                            int(str(ID)[2:4]),
                            int(str(ID)[0:2])).__str__() 


        # 2. Create Model Object
        new_player = Player(ID,name,dob,phone,address,email)

        # 3. Pass to Data Layer
        return new_player