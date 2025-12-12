
from models.team import Team

class team_handler:
    
    def create_team(self, name:str, tag:str, creator_id:str, team_size:int, teams:list[Team], member_list:list[str]) -> Team| int:
        """Create a new team with validation.
        
        Args:
            name (str):
                Name of the team.
            tag (str):
                Team tag or abbreviation. Must be unique and under length limit.
            creator_id (str):
                National ID (KT) of the team’s creator. Must be 10 characters.
            team_size (int):
                Maximum team size. Must not exceed domain constraints.
            teams (list[Team]):
                Existing teams used for validating uniqueness and generating a new ID.
            member_list (list[str]):
                List of player IDs belonging to the team.
        
        Returns:
            Team | int:
                * Team: Newly created Team instance if validation succeeds.
                * int: Error code if validation fails:
                    - -2: Invalid creator ID length or tag length.
                    - -3: Duplicate team tag or team name.
                    - -4: Invalid data type for inputs.
                    - -5: Team size exceeds allowed maximum (21).
        """
        # 1. Validate Input (Business Logic)        
        if len(creator_id) != 10 or len(tag) > 20: ##validate length of KT and tag length
            return -2
        
        highest:int = 0
        for x in teams:
            if x.id > highest:
                highest = x.id

        highest += 1 # find new id
         
        for t in teams:
            if t.tag == tag or t.name == name:
                return -3
            
        if isinstance(tag,int) or isinstance(name,int) or not isinstance(creator_id,str) or not isinstance(team_size,int):
            return -4
        
        if team_size>21:
            return -5
        
        

        # 2. Create Model Object
        new_team = Team(highest,name,tag,creator_id,team_size,member_list)

        # 3. Pass to Data Layer
        return new_team