
from models.match import Match
from models.tournament import Tournament

class tournament_handler:
    
    def create_tournament(self, name:str, start_date:str, end_date:str, venue:str, contact_id:int, contact_email:str, contact_phone:int,existing_tournaments: list[Tournament] , team_list:list[int],matches:list[int]) -> Tournament| bool:
        # 1. Validate Input (Business Logic)        
        if len(str(contact_id)) != 10:
            return False
        
        highest:int = 0
        for x in existing_tournaments:
            if x.id > highest:
                highest = x.id
        highest+=1 # find new id
        
        
        
        # 2. Create Model Object
        new_team = Tournament(highest,name,start_date,end_date ,venue,contact_id,contact_email,contact_phone,team_list,matches)

        # 3. Pass to Data Layer
        return new_team
    
    def generate_bracket(self, tournament: Tournament, previus_matches: list[Match]) -> list[tuple[int, int]] | int:
        return tournament.generate_knockout_bracket(previus_matches)