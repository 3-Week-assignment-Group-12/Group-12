from __future__ import annotations

from dataclasses import dataclass, asdict

@dataclass
class Player:
    """
    Represents a Player in the system.
    
    attributes:
        id: str
            National ID (Kennitala) of the player.
        name: str
            Full name of the player.
        handle: str
            In-game handle or nickname.
        link:str
            Profile link or reference URL.
        dob: str
            Date of birth extracted from national ID (formatted as string).
        phone: int
            Phone number of the player.
        address: str
            Home address.
        email: str
            Email address.
        dynamic_data: dict
            Dictionary used for storing additional runtime or computed data.
            Can be used for statistics, temporary values, etc.
    """
    
    id: str
    name: str
    handle: str
    link:str
    dob: str
    phone: int
    address: str
    email: str
    
    dynamic_data: dict
    

    filename = "player_data.json"
    
    @staticmethod
    def from_dict(data: dict) -> Player:
        """Create a Player instance from a dictionary.

        Args:
            data (dict):
                Dictionary containing player data with keys matching
                the Player class attributes.

        Returns:
            Player: A Player instance populated with the dictionary values.
        """
        return Player(**data)

    def to_dict(self) -> dict:
        """Convert the Player instance into a dictionary.

        Returns:
            dict: Dictionary representation of the Player,
            suitable for JSON serialization.
        """
        return asdict(self)
