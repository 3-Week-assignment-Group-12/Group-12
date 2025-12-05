from __future__ import annotations
from dataclasses import dataclass, asdict

@dataclass
class Team:
    """
    Represents a Team in the system.
    
    attributes:
        id: int
        name: str
        tag: str
        creator_id: int
        team_size: int
        member_list: list[int]    
    """
    
    id: int 
    name: str
    tag: str 
    creator_id: int 
    team_size: int 
    member_list: list[int]
    
    filename = "./data/files/team_data.json"
        
      
    
    @staticmethod
    def from_dict(data: dict) -> Team:
        return Team(**data)

    def to_dict(self) -> dict:
        return asdict(self)