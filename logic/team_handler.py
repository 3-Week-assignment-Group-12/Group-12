
from models.team import Team
from models.player import Player

class team_handler:
    
    def create_team(self, name:str, tag:str, creator_id:int, team_size:int,teams:list[Team],team_list:list[Player]) -> Team| bool:
        # 1. Validate Input (Business Logic)        
        if len(str(creator_id)) != 10: ##validate length of KT
            return False
        
        
        for x in playerList:
            if x.kt == KT or x.phone == phone or x.email == email:
                return False
        
        
        
        # 2. Create Model Object
        new_team = Team(name,tag,creator_id,team_size,team_list)

        # 3. Pass to Data Layer
        return new_team