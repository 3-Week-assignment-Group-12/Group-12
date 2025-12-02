from __future__ import annotations


class Player:
    
    def __init__(self, KT:int, name:str, dob:str, phone:int, address:str, email:str) -> None: 
        self.kt: int  = KT
        self.name: str = name
        self.dob: str = dob
        self.phone: int = phone
        self.address: str = address
        self.email: str = email
        
    def __str__(self) -> str:
        return f"name: {self.name}, National ID: {self.kt}, date of birth: {self.dob}, phone{self.phone}, address: {self.address}, email: {self.email}"
        
    
        
        
    def create_player(self, Kt:int, name:str, dob:str, phone:int, address:str, email:str) ->Player:
        return Player(Kt,name,dob,phone,address,email)
    
    
    def toCSVList(self) -> list[str|int]:
        return [self.kt,self.name,self.dob,self.phone,self.address,self.email]
    
