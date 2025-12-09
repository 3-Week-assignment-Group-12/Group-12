from __future__ import annotations

from dataclasses import dataclass, asdict

@dataclass
class Club:
    """
    Represents a Club in the system.
    
    attributes:
        id: int
        name: str
        colours: str
        location: str
        teams: list[int]

    """
    
    id: int
    name: str
    colours: str
    location: str
    teams: list[int]




    filename = "club_data.json"
    
    @staticmethod
    def from_dict(data: dict) -> Club:
        return Club(**data)

    def to_dict(self) -> dict:
        return asdict(self)
