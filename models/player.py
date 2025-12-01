from __future__ import annotations

class Player:
    def __init__(self, name:str) -> None: # more attrebutes to be added
        self.name = name
        
    def create_player(self,name: str) ->Player:
        return Player(name)
    
    def toCSVList(self) -> list[str]:
        return [self.name]