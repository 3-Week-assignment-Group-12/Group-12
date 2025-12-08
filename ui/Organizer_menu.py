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

        while True:
            print(
""" 
Organizer Menu

1. Player Management
2. Tournament Management
b. Back


""")
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

        
        while True:
            print(
""" 
Player Management 

1. Add player
2. Edit player information
3. Delete player
4. View players (view menu shortcut)
b. Back 


""")
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
                    nID:int = self.check_for_player_kt()
                    name:str=input("Name: ")
                    phone:int=int(input("Phone number:"))
                    address:str=input("Address: ")
                    email:str=input("Email: ")
                    print("Adding Player...")
                    ret = self.logic_wrapper.create_player(nID,name,phone,address,email)
                    print(ret)
                    if ret is 1:
                        print("Player added!!")
                    elif ret is -1:
                        print("Error adding player")
                    elif ret is -2:
                        print("Validation failed, player not added")
                    elif ret is -3:
                        print("Invalid ID length, player not added")
                    elif ret is -4:
                        print("Duplicate player found, player not added")
                    else:
                        print("Player added!!")
                    
                case "2": 
                    id=self.inputplayersID()
                    self.edit_player_menu(id)  #Asks the user for Players National Id before going to the edit page
                case "3":
                    ID=self.inputplayersID()
                    x=input("Are you sure? (Y/N)")
                    if x=="y" or x=="Y":
                        self.logic_wrapper.delete_player(ID) # type: ignore
                    return   
                case "4":
                    pass
                case "b": 
                    return

    def edit_player_menu(self,Player_ID:str):


        temp : Player|bool = self.logic_wrapper.get_player_by_ID(Player_ID)  
        while True:
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
            if isinstance(temp, bool):
                print("Player not found")
                return
            
            match choice:
                case "1": 
                    temp.name = input("Enter New name: ")
                case "2": 
                    temp.phone = int(input("Enter New number: "))
                case "3": 
                    temp.address = input("Enter New address: ")     
                case "4": 
                    temp.email = self.check_for_player_email() 
                case "5": 
                    pass 
                case "6": 
                    pass
                case "7": 
                    pass
                case "b": 
                    return
            self.logic_wrapper.modify_player(temp)

    
    #------------------Functions--------------------------
    def check_for_player_kt(self) -> int:
            nID:int=int(input("National ID: "))
            list_of_players= self.logic_wrapper.get_players()
            while True:
                if list_of_players is None or list_of_players == []:
                    return nID
                for player in list_of_players:
                    playerinfo=self.logic_wrapper.get_player_by_ID(player.id)
                    if isinstance(playerinfo,Player):
                        if nID == playerinfo.id: 
                            print("This national ID already exists!")
                            nID:int=int(input("Enter different National ID: "))
                        else:
                            return nID
                        

    def check_for_player_email(self):
        email:str=input("Email:")
        list_of_players=self.logic_wrapper.get_players()
        while True:
            
            if list_of_players is None or list_of_players == []:
                return email
            for player in list_of_players:
                playerinfo=self.logic_wrapper.get_player_by_ID(player.id)
                if isinstance(playerinfo,Player):
                    if email == playerinfo.email: 
                        print("This email already exists!")
                        email:str=input("Enter different email: ")
                    else:
                        return email
                    

    def inputplayersID(self):
        playersID=input("Enter National ID: ")
        check= self.logic_wrapper.get_player_by_ID(playersID)
        while check is False:
            print("Player does not exist, Try different ID")
            playersID=input("Enter National ID: ")
            check= self.logic_wrapper.get_player_by_ID(playersID)
        return playersID