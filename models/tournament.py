from __future__ import annotations
from models.match import Match

from dataclasses import dataclass, asdict

@dataclass
class Tournament:
    
    """
    Represents a Tournament in the system.
    
    attributes:
        id: int
        name: str
        start_date: str
        end_date: str
        venue_name: str
        contact_id: str
        contact_email: str
        contact_phone: str
        team_list: list[int]
        matches: list[int]
    """

    

    # Tournament identification
    id: int 
    name: str 
    
    # Tournament scheduling
    start_date: str 
    end_date: str
    
    # Venue information
    venue_name: str 
    
    # Contact information
    contact_id: str
    contact_email: str 
    contact_phone: str
    
    # Participants and events
    team_list: list[int] 
    matches: list[int] 
    
    filename = "tournament_data.json"
    
    @staticmethod
    def from_dict(data: dict) -> Tournament:
        return Tournament(**data)

    def to_dict(self) -> dict:
        return asdict(self)

    
    def generate_knockout_bracket(self, previus_matches:list[Match]) -> list[tuple[int, int]]|int:
        """Generate a knockout bracket for the tournament.
        
        Creates a list of match pairings for a knockout stage based on the
        participating teams. Each match is represented as a tuple of team IDs.
        
        Returns:
            list[tuple[int, int]]|int: A list of tuples representing match pairings,
            int for errors.
            
        Errors:
            -1: Not enough teams to generate a schedule
            -2: Odd number of teams cannot form pairs
        """
        
        if len(self.team_list) > 2:
            return -1  # Not enough teams to generate a schedule
        
        elif len(self.team_list) % 2 != 0:
            return -2  # Odd number of teams cannot form pairs
        
        
        
        if len(previus_matches) != 0:
            awailable_teams: list[int] = [int(team.winner_id) for team in previus_matches]
        else:
            awailable_teams: list[int] = self.team_list.copy()
            
        
        bracket: list[tuple[int, int]] = []
        for i in range(0, len(awailable_teams), 2):
            bracket.append((awailable_teams[i], awailable_teams[i+1]))
        
        
        return bracket