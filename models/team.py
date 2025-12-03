from __future__ import annotations


class Team:
    """
    Represents a team with member information and team details.
    
    This class encapsulates all information related to a team including its
    identification, naming, creator information, and member list.
    
    Attributes:
        id (int): Unique identifier for the team
        name (str): Name of the team
        tag (str): Team tag or abbreviation
        creator_id (int): ID of the player who created the team
        team_size (int): Maximum size of the team
        team_list (list[int]): List of player IDs currently in the team
    """
    
    def __init__(self, TID: int, name: str, tag: str, creator_id: int, team_size: int, member_list: list[int]) -> None:
        """Initialize a Team instance.
        
        Creates a new team with the specified details including identification,
        creator information, and initial member list.
        
        Args:
            TID (int): Unique identifier for the team
            name (str): Name of the team
            tag (str): Team tag or abbreviation
            creator_id (int): ID of the player who created the team
            team_size (int): Maximum size of the team
            team_list (list[int]): List of player IDs currently in the team
        """
        self.id: int = TID
        self.name: str = name
        self.tag: str = tag
        self.creator_id: int = creator_id
        self.team_size: int = team_size
        self.member_list: list[int] = member_list
        
        
    def __str__(self) -> str:
        """Return a string representation of the team.
        
        Provides a human-readable summary of the team's key information
        including name, tag, creator, and team size.
        
        Returns:
            str: Formatted team information
        """
        return f"team name: {self.name}, team tag: {self.tag}, creator ID: {self.creator_id}, team size: {self.team_size}"
        
    
    def create_team(self, id: int, name: str, tag: str, creator_id: int, team_size: int, team_list: list[int]) -> Team:
        """Create and return a new Team instance.
        
        Factory method that instantiates a new Team with the provided parameters.
        
        Args:
            id (int): Unique identifier for the team
            name (str): Name of the team
            tag (str): Team tag or abbreviation
            creator_id (int): ID of the player who created the team
            team_size (int): Maximum size of the team
            team_list (list[int]): List of player IDs currently in the team
            
        Returns:
            Team: A new Team instance with the specified attributes
        """
        return Team(id, name, tag, creator_id, team_size, team_list)
    
    def toCSVList(self) -> list[str | int | list[int]]:
        """Convert team data to a list for CSV export.
        
        Transforms all team attributes (except id) into a flat list format suitable
        for writing to CSV files. The id is typically handled separately in data persistence.
        
        Returns:
            list: Team data as a list in the following order:
                [name, tag, creator_id, team_size, team_list]
        """
        return [self.name, self.tag, self.creator_id, self.team_size, self.member_list]