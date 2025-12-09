
from models.match import Match
from models.tournament import Tournament

class tournament_handler:
    
    def create_tournament(self, name:str, start_date:str, end_date:str, venue:str, contact_id:str, contact_email:str, contact_phone:str,existing_tournaments: list[Tournament] , team_list:list[int],matches:list[int]) -> Tournament| int:
        """ this function creates a tournament object after validating the inputs


        Returns:
            Tournament| bool: returns the created tournament object or False if validation fails
        """
        # 1. Validate Input (Business Logic)        
        if len(contact_id) != 10:
            return -2
        
        highest:int = 0
        for x in existing_tournaments:
            if x.id > highest:
                highest = x.id
        highest+=1 # find new id
        

        
        
        nr_of_at=0
        for i in contact_email:
            if i =="@":
                nr_of_at+=1
            
        if nr_of_at!=1:
            return -4
        
        if not isinstance(contact_phone,str) or len(contact_phone)!=7:
            return -5
        
        string_splitted_at_dots= [int(x) for x in start_date.split(".")]
        for i in string_splitted_at_dots:
            if not isinstance(i,int):
                return -6
            
        string_splitted_at_dot= [int(x) for x in start_date.split(".")]
        for j in string_splitted_at_dot:
            if not isinstance(j,int):
                return -6
        
        # 2. Create Model Object
        new_team = Tournament(highest,name,start_date,end_date ,venue,contact_id,contact_email,contact_phone,team_list,matches)

        # 3. Pass to Data Layer
        return new_team
    
    def generate_bracket(self, tournament: Tournament, previus_matches: list[Match]) -> list[tuple[int,int]] | int:
        """Generate a knockout bracket for the tournament.
        
        Returns:
            list[tuple[int,int]] | int: A list of tuples representing match pairings,
            int for errors.
        """
        return tournament.generate_knockout_bracket(previus_matches)