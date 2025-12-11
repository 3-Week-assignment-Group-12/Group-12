from __future__ import annotations
from dataclasses import dataclass, asdict

@dataclass
class Record:
    """
    Represents a Record of data.
    
    This class keeps track on all information for players, teams, clubs, and tournaments
    
    
    Attributes:
        id: int
            Unique identifier for the record entry.
        player_id: str
            National ID of the player associated with this record.
        team_id: int
            ID of the team the player belongs to.
        tournament_id: int
            ID of the tournament related to this record.
        club_id: int
            ID of the club associated with this record.
        list_of_matches: int
            Number of matches played or a reference to match data
            (depends on domain interpretation).
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
        """Create a Record instance from a dictionary.

        Args:
            data (dict):
                Dictionary containing record data with keys matching
                the Record class attributes.

        Returns:
            Record: A Record instance populated with the provided dictionary data.
        """
        return Record(**data)

    def to_dict(self) -> dict:
        """Convert the Record instance into a dictionary.

        Returns:
            dict: Dictionary representation of this Record,
            suitable for JSON serialization.
        """
        return asdict(self)