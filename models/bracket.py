from __future__ import annotations

from dataclasses import dataclass, asdict

@dataclass
class Bracket:
    """    
    This class encapsulates all information related to a bracket  
    
    Attributes:
        id (int): bracket id
        machups: list[tuple[int,int]]: list of matchups
        tournament_id: int: tournament id
    """
    

    id: int 
    matchups: list[tuple[int,int]] 
    tournament_id: int 
    
    filename = "./data/files/bracket_data.json"

    @staticmethod
    def from_dict(data: dict) -> Bracket:
        return Bracket(**data)

    def to_dict(self) -> dict:
        return asdict(self)