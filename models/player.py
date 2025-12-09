from __future__ import annotations

from dataclasses import dataclass, asdict

@dataclass
class Player:
    """
    Represents a Player in the system.
    
    attributes:
        id: str
        name: str
        dob: str
        phone: int
        address: str
        email: str
    """
    
    id: str
    name: str
    dob: str
    phone: int
    address: str
    email: str

    filename = "players_data.json"
    
    @staticmethod
    def from_dict(data: dict) -> Player:
        return Player(**data)

    def to_dict(self) -> dict:
        return asdict(self)
