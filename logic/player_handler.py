

from models.player import Player


class player_handler:
    def create_player(self, KT:int ,name:str ,dob: str,phone: int,address: str,email:str) ->Player| bool:
        # 1. Validate Input (Business Logic)
        if not KT or not name or not dob  or not phone  or not address  or not email:
            return False
        elif type(KT) != int:
            return False
        
        # 2. Create Model Object
        new_player = Player(KT,name,dob,phone,address,email)

        # 3. Pass to Data Layer
        return new_player