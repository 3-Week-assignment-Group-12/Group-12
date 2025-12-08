
from models.team import Team

class team_handler:
    
    def create_team(self, name:str, tag:str, creator_id:int, team_size:int, teams:list[Team], member_list:list[int]) -> Team| int:
        # 1. Validate Input (Business Logic)        
        if len(str(creator_id)) != 10 or len(tag) > 20: ##validate length of KT and tag length
            return -2
        
        highest:int = 0
        for x in teams:
            if x.id > highest:
                highest = x.id
        highest+=1 # find new id
         
        for t in teams:
            if t.tag == tag or t.name == name:
                return -3
        if isinstance(tag,int) or isinstance(name,int) or not isinstance(creator_id,int) or not isinstance(team_size,int):
            return -4
        if team_size>11:
            return -5
        
        

        # 2. Create Model Object
        new_team = Team(highest,name,tag,creator_id,team_size,member_list)

        # 3. Pass to Data Layer
        return new_team