from __future__ import annotations


class Tournament:
    """
    Represents a tournament with details about its schedule, venue, and participants.
    
    This class encapsulates all information related to a tournament including its
    identification, dates, venue details, contact information, and participating teams/matches.
    
    Attributes:
        id (int): Unique identifier for the tournament
        name (str): Name of the tournament
        start_date (date): Tournament start date
        end_date (str): Tournament end date
        venue_name (str): Name of the venue where the tournament is held
        contact_name (str): Name of the tournament contact person
        contact_email (str): Email address of the contact person
        contact_phone (str): Phone number of the contact person
        team_list (list[int]): List of team IDs participating in the tournament
        matches (list[int]): List of match IDs scheduled in the tournament
    """
    
    def __init__(self, tournament_id: int, name: str, start_date: str, end_date: str, 
                 venue_name: str, contact_name: str, contact_email: str, contact_phone: str, 
                 team_list: list[int], matches: list[int]) -> None:
        """Initialize a Tournament instance.
        
        Creates a new tournament with all required information including scheduling,
        venue details, contact information, and participant/match lists.
        
        Args:
            id (int): Unique identifier for the tournament
            name (str): Name of the tournament
            start_date (str): Tournament start date
            end_date (str): Tournament end date
            venue_name (str): Name of the venue where the tournament is held
            contact_name (str): Name of the tournament contact person
            contact_email (str): Email address of the contact person
            contact_phone (str): Phone number of the contact person
            team_list (list[int]): List of team IDs participating in the tournament
            matches (list[int]): List of match IDs scheduled in the tournament
        """
        # Tournament identification
        self.id: int = tournament_id
        self.name: str = name
        
        # Tournament scheduling
        self.start_date: str = start_date
        self.end_date: str = end_date
        
        # Venue information
        self.venue_name: str = venue_name
        
        # Contact information
        self.contact_name: str = contact_name
        self.contact_email: str = contact_email
        self.contact_phone: str = contact_phone
        
        # Participants and events
        self.team_list: list[int] = team_list
        self.matches: list[int] = matches
        
    def __str__(self) -> str:
        """Return a string representation of the tournament.
        
        Provides a human-readable summary of the tournament's key information
        including name, venue, dates, and contact details.
        
        Returns:
            str: Formatted tournament information
        """
        return f"ID: {self.id}, Tournament: {self.name}, Venue: {self.venue_name}, Start: {self.start_date}, End: {self.end_date}, Contact: {self.contact_name} ({self.contact_email})"
    
    def toCSVList(self) -> list[str | int | list[int]]:
        """Convert tournament data to a list for CSV export.
        
        Transforms all tournament attributes into a flat list format suitable
        for writing to CSV files. The list excludes tournament_id as it's typically
        handled separately in data persistence.
        
        Returns:
            list: Tournament data as a list in the following order:
                [id,name, start_date, end_date, venue_name, contact_name, contact_email, contact_phone, team_list, matches]
        """
        return [self.id, self.name, self.start_date, self.end_date, self.venue_name, self.contact_name, self.contact_email, self.contact_phone, self.team_list, self.matches]