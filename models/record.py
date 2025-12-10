from __future__ import annotations
from dataclasses import dataclass, asdict

@dataclass
class Record:
    """
    Represents a Record of data.
    
    This class keeps track on all information for players, teams, clubs, and tournaments
    
    
    Attributes:
        id: int
        player_id: str
        team_id: int
        tournament_id: int
        club_id: int
        list_of_matches: int
    """
    

    id: int
    player_id: str
    team_id: int
    tournament_id: int
    club_id: int
    list_of_matches: int
    
    filename = "record.json"
        
    @staticmethod
    def from_dict(data: dict) -> Record:
        return Record(**data)

    def to_dict(self) -> dict:
        return asdict(self)