from __future__ import annotations
from dataclasses import dataclass, asdict

@dataclass
class Team:
    """
    Represents a Team in the system.
    
    attributes:
        id: int
            Unique identifier for the team.
        name: str
            Name of the team.
        tag: str
            Abbreviation or short identifier for the team.
        creator_id: str
            National ID (Kennitala) of the team creator. Must be 10 characters.
        team_size: int
            Maximum number of members allowed in the team.
        member_list: list[str]
            List of player IDs belonging to this team.
    """
    
    id: int 
    name: str
    tag: str 
    creator_id: str 
    team_size: int 
    member_list: list[str]
    
    filename = "team_data.json"
        
      
    
    @staticmethod
    def from_dict(data: dict) -> Team:
        
        
        """Create a Team instance from a dictionary.

        Args:
            data (dict):
                Dictionary containing team data with keys matching
                the Team class attributes.

        Returns:
            Team: A Team instance populated from the provided dictionary.
        """
        return Team(**data)

    def to_dict(self) -> dict:
        """Convert the Team instance into a dictionary.

        Returns:
            dict: Dictionary representation of this Team,
            suitable for JSON serialization.
        """
        return asdict(self)