from __future__ import annotations

class Match:
    """
    Represents a Match between 2 teams.
    
    This class encapsulates all information related to a Match including their
    participating teams, date, time, server, and outcome.
    
    
    Attributes:
        match_id: int
        team1_id: int
        team2_id: int
        tournament_id: int
        date: str
        match time: str
        server_id: int
        winner_id: int | None
        Score:int
    """
    
    def __init__(self, match_id: int, team1_id: int,team2_id: int, tournament_id: int, date: str, time: str,server_id: int,winner_id: int,Score:int) -> None:
        """Initialize a Player instance.
        
        Creates a new player with the specified personal and contact information.
        
        Args:
            match_id: int
            team1_id: int
            team2_id: int
            tournament_id: int
            date: str
            match time: str
            server_id: int
            winner_id: int | None
            Score:int
        """
        self.match_id: int = match_id
        self.team1_id: int = team1_id
        self.team2_id: int = team2_id
        self.tournament_id: int = tournament_id
        self.date: str = date
        self.match_time: str = time
        self.server_id: int = server_id
        self.winner_id: int = winner_id
        self.Score:int = Score
        
    def __str__(self) -> str:
        """Return a string representation of the match.

        Returns:
            str: Formatted match information
        """
        return f"id: {self.match_id}, team1_id: {self.team1_id}, team2_id: {self.team2_id},date: {self.date}, time: {self.match_time},server_id: {self.server_id},winner_id: {self.winner_id} | None,Score: {self.Score}"
        
    def create_match(self,match_id:int, team1_id: int,team2_id: int, tournament_id:int, date: str, time: str,server_id: int,winner_id: int,Score:int) -> Match:
        """Create and return a new Player instance.
        
        Factory method that instantiates a new Match with the provided parameters.
        
        Args:
            match_id: int
            team1_id: int
            team2_id: int
            tournament_id
            date: str
            match time: str
            server_id: int
            winner_id: int
            Score:int
            
        Returns:
            Match: A new Match instance with the specified attributes
        """
        return Match(match_id, team1_id,team2_id,tournament_id,date, time,server_id,winner_id,Score)
    
    def toCSVList(self) -> list[str | int]:
        """Convert match data to a list for CSV export.
        
        Transforms all match attributes into a flat list format suitable
        for writing to CSV files.
        
        Returns:
            list: match data as a list in the following order:
                [match_id, team1_id, team2_id,tournament_id , date, match_time, server_id, winner_id, Score]
        """
        return [self.match_id, self.team1_id, self.team2_id,self.tournament_id , self.date, self.match_time, self.server_id, self.winner_id, self.Score]

