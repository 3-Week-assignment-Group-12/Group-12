from __future__ import annotations
# ui_layer/main_menu.py
from logic.logic_wrapper import LogicWrapper
from models.team import Team
from models.tournament import Tournament
from models.player import Player
from ui.tournament_management import TournamentManagement


class OrganizerMenu():
    def __init__(self, low : LogicWrapper) -> None:
        self.tournament_management = TournamentManagement(low)
        self.logic_wrapper = low
        pass

    def show_organizer_menu(self):
        print(
""" 
Organizer Menu

1. Player Management
2. Tournament Management
b. Back


""")
        while True:
            choice=input("Enter input: ")
            if choice not in ["1","2","b","B"]:

                 print(
""" 
Invalid Input!!

Organizer Menu

1. Player Management
2. Tournament Management
b. Back

Try again!!
""")

            match choice:
                case "1": 
                    self.player_management_menu()
                case "2": 
                    self.tournament_management.tournament_management_menu()
                case "b": 
                    pass
    

    def player_management_menu(self):
        print(
""" 
Player Management 

1. Add player
2. Edit player information
3. Delete player
4. View players (view menu shortcut)
b. Back 


""")
        
        while True:
            choice=input("Enter input: ")
            if choice not in ["1","2","3","4","b","B"]:

                 print(
""" 
Invalid Input!!

Player Management 

1. Add player
2. Edit player information
3. Delete player
4. View players (view menu shortcut)
b. Back 

Try again!!
""")
                 
            match choice:
                case "1": 
                    nID:int=int(input("National ID:"))
                    name:str=input("Name: ")
                    phone:int=int(input("Phone number:"))
                    address:str=input("Address: ")
                    email:str=input("Email: ")
                    self.logic_wrapper.create_player(nID,name,phone,address,email)==True
                    print("Player added!!")
                    self.player_management_menu()
                case "2": 
                    ID=self.logic_wrapper.inputplayersID()
                    self.edit_player_menu(ID)  #Asks the user for Players National Id before going to the edit page
                case "3":
                    ID=self.logic_wrapper.inputplayersID()
                    x=input("Are you sure? (Y/N)")
                    if x=="y" or x=="Y":
                        self.logic_wrapper.delete_player(ID) # type: ignore
                    return   
                case "4":
                    pass 
                    #self.view_players_menu()  
                case "b": 
                    return

    def edit_player_menu(self,Player_ID:int):

        print(
""" 
Edit Players info 

1. Edit Name
2. Edit Phone Number
3. Edit Address
4. Edit Email
5. Edit Player Handle
6. Edit Player Link
7. Edit Portrait
b. Back


""")
        temp : Player = self.logic_wrapper.get_player_by_ID(Player_ID)  
        while True:
            choice=input("Enter input: ")
            if choice not in ["1","2","3","4","5","6","7","b","B"]:
                
                print(
""" 
Invalid Input!!

Edit Players info 

1. Edit Name
2. Edit Phone Number
3. Edit Address
4. Edit Email
5. Edit Player Handle
6. Edit Player Link
7. Edit Portrait
b. Back

Try again!!
""")   
            
            match choice:
                case "1": 
                    temp.name = input("Enter New name: ")
                case "2": 
                    temp.phone = int(input("Enter New number: "))
                case "3": 
                    temp.address = input("Enter New address: ")     
                case "4": 
                    temp.email = input("Enter New email: ")
                case "5": 
                    pass 
                case "6": 
                    pass
                case "7": 
                    pass
                case "b": 
                    return
            self.logic_wrapper.modify_player(temp)

    
    
