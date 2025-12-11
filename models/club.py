from __future__ import annotations

from dataclasses import dataclass, asdict

@dataclass
class Club:
    """
    Represents a Club in the system.
    
    attributes:
        id: int
            Unique identifier for the club.
        name: str
            Name of the club.
        colours: str
            Club colours (e.g., primary branding colour).
        teams: list[int]
            List of team IDs belonging to this club.
    """
    
    id: int
    name: str
    colours: str
    teams: list[int]




    filename = "club_data.json"
    
    @staticmethod
    def from_dict(data: dict) -> Club:
        """Create a Club instance from a dictionary.
        
        Args:
            data (dict):
                Dictionary containing all club attributes with keys
                matching the Club fields.
        
        Returns:
            Club: A Club instance populated from the provided dictionary.
        """
        return Club(**data)

    def to_dict(self) -> dict:
        """Convert the Club instance into a dictionary.
        
        Returns:
            dict: A dictionary representation of the Club,
            suitable for JSON serialization.
        """
        return asdict(self)
