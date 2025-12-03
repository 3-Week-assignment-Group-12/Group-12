from __future__ import annotations


class Player:
    """
    Represents a player with personal and contact information.
    
    This class encapsulates all information related to a player including their
    identification, personal details, and contact information.
    
    Attributes:
        kt (int): Player's national identification number (Kennitala)
        name (str): Player's full name
        dob (str): Player's date of birth
        phone (int): Player's phone number
        address (str): Player's residential address
        email (str): Player's email address
    """
    
    def __init__(self, KT: int, name: str, dob: str, phone: int, address: str, email: str) -> None:
        """Initialize a Player instance.
        
        Creates a new player with the specified personal and contact information.
        
        Args:
            KT (int): Player's national identification number (Kennitala)
            name (str): Player's full name
            dob (str): Player's date of birth
            phone (int): Player's phone number
            address (str): Player's residential address
            email (str): Player's email address
        """
        self.kt: int = KT
        self.name: str = name
        self.dob: str = dob
        self.phone: int = phone
        self.address: str = address
        self.email: str = email
        
    def __str__(self) -> str:
        """Return a string representation of the player.
        
        Provides a human-readable summary of the player's key information
        including name, national ID, date of birth, contact details, and address.
        
        Returns:
            str: Formatted player information
        """
        return f"name: {self.name}, National ID: {self.kt}, date of birth: {self.dob}, phone: {self.phone}, address: {self.address}, email: {self.email}"
        
    def create_player(self, KT: int, name: str, dob: str, phone: int, address: str, email: str) -> Player:
        """Create and return a new Player instance.
        
        Factory method that instantiates a new Player with the provided parameters.
        
        Args:
            KT (int): Player's national identification number (Kennitala)
            name (str): Player's full name
            dob (str): Player's date of birth
            phone (int): Player's phone number
            address (str): Player's residential address
            email (str): Player's email address
            
        Returns:
            Player: A new Player instance with the specified attributes
        """
        return Player(KT, name, dob, phone, address, email)
    
    def toCSVList(self) -> list[str | int]:
        """Convert player data to a list for CSV export.
        
        Transforms all player attributes into a flat list format suitable
        for writing to CSV files.
        
        Returns:
            list: Player data as a list in the following order:
                [kt, name, dob, phone, address, email]
        """
        return [self.kt, self.name, self.dob, self.phone, self.address, self.email]

