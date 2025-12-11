
from models.player import Player
import datetime

class player_handler:
    
    def create_player(self, ID:str ,name:str ,handle:str ,link:str ,phone: int,address: str,email:str, existing_playerList:list[Player]) ->Player| int:
        # 1. Validate Input (Business Logic)     
        day=int(ID[0:2])
        month=int(ID[2:4])
        if ID[-1]=="0":
            year = int("20"+ID[4:6])
        else:
            year = int("19"+ID[4:6])  

        dob = datetime.date(year,month,day).__str__()  ##Gerir ekki rétt ártal
        
        data = { #starting data
            "total score": 0,
            "wins": 0,
            "losses": 0
        }
        
        # 2. Create Model Object
        new_player = Player(ID,name,handle,link,dob,phone,address,email,data)

        # 3. Pass to Data Layer
        return new_player