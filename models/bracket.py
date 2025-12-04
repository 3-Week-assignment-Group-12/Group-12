from __future__ import annotations


class Bracket:
    """    
    This class encapsulates all information related to a bracket  
    
    Attributes:
        id (int): bracket id
        machups: list[tuple[int,int]]: list of matchups
        tournament_id: int: tournament id
    """
    
    def __init__(self, id: int, matchups:list[tuple[int,int]], tournament_id:int ) -> None:
        """    
        This class encapsulates all information related to a bracket  
        
        Attributes:
            id (int): bracket id
            machups: list[tuple[int,int]]: list of matchups
            tournament_id: int: tournament id
        """
        self.id: int = id
        self.matchups: list[tuple[int,int]] = matchups
        self.tournament_id: int = tournament_id

        
    def __str__(self) -> str:
        """Return a string representation of the player.
        
        Provides a human-readable summary of the player's key information
        including name, national ID, date of birth, contact details, and address.
        
        Returns:
            str: Formatted player information
        """
        return f"id: {self.id}, matchups: {self.matchups}, tournament_id: {self.tournament_id}"
        
    def create_bracket(self, id: int, matchups:list[tuple[int,int]], tournament_id:int) -> Bracket:
        """      
        Factory method that instantiates a new bracket with the provided parameters.
        
        Args:
            id (int): bracket id
            machups: list[tuple[int,int]]: list of matchups
            tournament_id: int: tournament id
            
        Returns:
            Bracket: A new Player instance with the specified attributes
        """
        return Bracket(id, matchups, tournament_id)
    
    def toCSVList(self) -> list[int | list[tuple[int,int]]]:
        """Convert player data to a list for CSV export.
        
        Transforms all player attributes into a flat list format suitable
        for writing to CSV files.
        
        Returns:
            list: Player data as a list in the following order:
                [kt, name, dob, phone, address, email]
        """
        return [self.id, self.matchups, self.tournament_id]

