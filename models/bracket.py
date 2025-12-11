from __future__ import annotations

from dataclasses import dataclass, asdict

@dataclass
class Bracket:
    """    
    Represents a knockout bracket in the system.

    Attributes:
        id (int):
            Unique identifier for the bracket.
        matchups (list[tuple[int, int]]):
            List of matchups, each represented as a pair of team IDs
            (team1_id, team2_id).
        tournament_id (int):
            ID of the tournament this bracket belongs to.
    """
    

    id: int 
    matchups: list[tuple[int,int]] 
    tournament_id: int 
    
    filename = "bracket_data.json"

    @staticmethod
    def from_dict(data: dict) -> Bracket:
        """Create a Bracket instance from a dictionary.

        Args:
            data (dict):
                Dictionary containing bracket data with keys matching
                the Bracket fields.

        Returns:
            Bracket: A Bracket instance populated with the given data.
        """
        return Bracket(**data)

    def to_dict(self) -> dict:
        """Convert the Bracket instance into a dictionary.

        Returns:
            dict: Dictionary representation of the Bracket, suitable
            for JSON serialization.
        """
        return asdict(self)