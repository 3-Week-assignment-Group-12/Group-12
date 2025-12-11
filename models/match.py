from __future__ import annotations
from dataclasses import dataclass, asdict

@dataclass
class Match:
    """
    Represents a Match between 2 teams.
    
    This class encapsulates all information related to a Match including their
    participating teams, date, time, server, and outcome.
    
    
    Attributes:
        id: int
        team1_id: int
        team2_id: int
        tournament_id: int
        date: str
        match time: str
        server_id: int
        winner_id: int
        Score:int
    """
    

    id: int 
    team1_id: int 
    team2_id: int 
    tournament_id: int 
    date: str 
    match_time: str 
    server_id: int 
    winner_id: int
    Score:int
    
    filename = "match_data.json"
        
    @staticmethod
    def from_dict(data: dict) -> Match:
        return Match(**data)

    def to_dict(self) -> dict:
        return asdict(self)