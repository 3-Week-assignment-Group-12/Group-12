from __future__ import annotations
from models.match import Match

from dataclasses import dataclass, asdict

@dataclass
class Tournament:
    
    """
    Represents a Tournament in the system.
    
    attributes:
        id: int
            Unique identifier for the tournament.
        name: str
            Name of the tournament.
        start_date: str
            Tournament start date in the format DD.MM.YYYY.
        end_date: str
            Tournament end date in the format DD.MM.YYYY.
        venue_name: str
            Name of the venue where the tournament is held.
        contact_id: str
            National ID (Kennitala) of the organizer, must be 10 characters.
        contact_email: str
            Email address of the tournament organizer.
        contact_phone: str
            Phone number of the organizer, must be 7 digits.
        team_list: list[int]
            A list of team IDs participating in the tournament.
        matches: list[list[int]]
            A list of match rounds, where each round is a list of match IDs.
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
    matches: list[list[int]] 
    
    
    filename = "tournament_data.json"
    
    @staticmethod
    def from_dict(data: dict) -> Tournament:
        """Create a Tournament instance from a dictionary.

        Args:
            data (dict):
                Dictionary containing tournament data with keys
                matching the Tournament attributes.

        Returns:
            Tournament:
                A Tournament instance populated with the provided data.
        """
        return Tournament(**data)

    def to_dict(self) -> dict:
        """Convert the Tournament instance into a dictionary.

        Returns:
            dict:
                A dictionary representation of the Tournament object,
                suitable for JSON serialization.
        """
        return asdict(self)

    
    def generate_knockout_bracket(self, previus_matches:list[Match]) -> list[tuple[int, int]]|int:
        """Generate a knockout bracket for the tournament.
        
        This function determines the next round matchups. It either uses
        the winners of previous matches or, if no previous matches exist,
        the tournament's registered team list.

        Returns:
            list[tuple[int, int]] | int:
                A list of (team1_id, team2_id) pairs representing matchups.

                Or an error code:
                    2   — Bracket is complete (final winner determined)
                    -1  — Not enough teams to generate a bracket
                    -2  — Odd number of teams prevents pairing

        Notes:
            - The function expects that `self.matches` contains rounds
              as lists of match IDs.
            - When the last round list is empty, the bracket is considered done.
        """
        # If the last match round is empty, bracket is complete
        if len(self.matches[-1]) == 0:
            self.matches.append([])
            return 2
        
        if len(self.matches[-1]) < 0:
            return -1  # Not enough teams to generate a schedule
        
        elif len(self.team_list) % 2 != 0:
            return -2  # Odd number of teams cannot form pairs
        
        # Determine which teams advance
        if len(previus_matches) != 0:
            awailable_teams: list[int] = [int(team.winner_id) for team in previus_matches if team.winner_id != None]
        else:
            awailable_teams: list[int] = self.team_list.copy()
            
        # Pair teams into matchups
        bracket: list[tuple[int, int]] = []
        for i in range(0, len(awailable_teams), 2):
            bracket.append((awailable_teams[i], awailable_teams[i+1]))
        
        
        return bracket