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
            Unique identifier for the match.
        team1_id: int
            ID of the first participating team.
        team2_id: int
            ID of the second participating team.
        tournament_id: int
            ID of the tournament this match belongs to.
        date: str
            Match date in string format (e.g., 'dd.mm.yyyy').
        match time: str
            Match time in string format (e.g., 'hh:mm').
        server_id: int
            ID of the assigned match server or field.
        winner_id: int
            ID of the winning team.
        Score:int
            Score or numerical result of the match.
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
        """Create a Match instance from a dictionary.

        Args:
            data (dict):
                Dictionary containing match data with keys matching
                the Match class attributes.

        Returns:
            Match: A new Match instance populated from the dictionary.
        """
        return Match(**data)

    def to_dict(self) -> dict:
        """Convert the Match instance into a dictionary.

        Returns:
            dict: Dictionary representation of this Match,
            suitable for JSON serialization.
        """
        return asdict(self)