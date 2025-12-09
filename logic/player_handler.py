
from models.player import Player
import datetime

class player_handler:
    
    def create_player(self, ID:str ,name:str ,phone: int,address: str,email:str, existing_playerList:list[Player]) ->Player| int:
        # 1. Validate Input (Business Logic)     
        if len(str(ID)) != 10:
            return -3  # Invalid ID length
        
        nr_of_at=0
        for i in email:
            if i =="@":
                nr_of_at+=1
            
        if nr_of_at!=1:
            return -5
        
        
        if not isinstance(phone,int) or len(str(phone))!=7:
            return -5 # breita phone í str til að laga cutoff
        
        for p in existing_playerList:
            if p.id == ID or p.phone == phone or p.email == email:
                return -4
        

        if isinstance(name,int):
            return -6
        
        dob = datetime.date(day=int(str(ID)[0:2]), month=int(str(ID)[2:4]), year=int(str(ID)[4:6])).__str__()  ##Gerir ekki rétt ártal
        # 2. Create Model Object
        new_player = Player(ID,name,dob,phone,address,email)

        # 3. Pass to Data Layer
        return new_player