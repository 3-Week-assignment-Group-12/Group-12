from __future__ import annotations
from models.player import Player



class Team:
    
    def __init__(self, TID:int, name:str, tag:str, creator_id:int, team_size:int,team_list:list[int]) -> None:
        self.id: int = TID
        self.name: str = name
        self.tag: str = tag
        self.creator_id: int = creator_id
        self.team_size: int = team_size
        self.team_list: list[int] = team_list
        
        
    def __str__(self) -> str:
        return f"team name: {self.name}, team tag: {self.tag}, creator ID: {self.creator_id}, team size: {self.team_size}"
        
    
    def create_team(self, id, name:str, tag:str, creator_id:int, team_size:int,team_list:list[int]) -> Team :
        return Team(id,name,tag,creator_id,team_size,team_list)
    
    def toCSVList(self) -> list[str|int|list[int]]:
        return [self.name,self.tag,self.creator_id,self.team_size,self.team_list]