from __future__ import annotations
# ui_layer/main_menu.py
from logic.logic_wrapper import LogicWrapper
from models.team import Team
from models.tournament import Tournament
from models.player import Player
from ui.function_file import functionFile

from ui.tournament_management import TournamentManagement


class OrganizerMenu():
    """Organizer-facing menu for managing players and tournaments.

    This class is responsible for:
        - Displaying the organizer main menu.
        - Routing to player management functions.
        - Routing to tournament management menu.
    """
    def __init__(self,low : LogicWrapper,functionFile:functionFile) -> None:
        """Initialize OrganizerMenu with dependencies.

        Args:
            low (LogicWrapper):
                Shared logic layer facade used to perform business operations.
            functionFile (functionFile):
                Helper object providing shared input/validation functions.
        """
        self.logic_wrapper = low
        self.functionFile = functionFile
        self.tournament_menu = TournamentManagement(low,self.functionFile)




#----------------------------Organizer menu-----------------------------
        



    def show_organizer_menu(self):
        """Display the main Organizer menu and handle user navigation.

        Options:
            1 -> Player Management menu
            2 -> Tournament Management menu
            b -> Back to previous menu / caller

        The method loops until the user chooses 'b' / 'B'.
        """
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
                    self.tournament_menu.tournament_management_menu()
                case "b": 
                    return
    




#----------------------------Management menu-----------------------------
        


        
    def player_management_menu(self):
        """Display the Player Management menu and handle user actions.

        Options:
            1 -> Add player
            2 -> Edit player information
            3 -> Delete player
            4 -> View players
            b -> Back

        Uses functionFile helpers for input/validation and LogicWrapper
        for the actual CRUD operations.
        """
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
                    nid = self.functionFile.inputplayersID()
                    if nid == False:
                        continue
                    name=self.functionFile.input_name()
                    if name == False:
                        continue
                    handle=self.functionFile.inputPlayerHandle()
                    if handle == False:
                        continue
                    link=self.functionFile.inputPlayerLink()
                    if link == False:
                        continue
                    phone=self.functionFile.input_phone_nr()
                    if phone == False:
                        continue
                    address:str=input("Address: ")
                    if address == "q":
                        continue
                    email=self.functionFile.input_email()
                    if email == False:
                        continue 
                    print("Adding Player...")
                    ret = self.logic_wrapper.create_player(nid,name,handle,link,phone,address,email)
                    

                    print(ret)
                    if ret == 1:
                        print("Player added!!")
                    elif ret == -1:
                        print("Error adding player")
                    elif ret == -2:
                        print("Validation failed, player not added")
                    elif ret == -3:
                        print("Invalid ID length, player not added")
                    elif ret == -4:
                        print("Duplicate player found, player not added")
                    else:
                        print("Player added!!")
                    
                case "2": 
                    id=self.functionFile.check_existingID()
                    if isinstance(id,str):
                        self.edit_player_menu(id)  #Asks the user for Players National Id before going to the edit page
                    else:
                        print("error: player not found")
                case "3":
                    ID=self.functionFile.check_existingID()
                    if isinstance(ID,str):
                        x=input("Are you sure? (Y/N)")
                        if x=="y" or x=="Y":
                            self.logic_wrapper.delete_player(ID) 
                            print("Player has been deleted!")
                        return   
                case "4":
                    list_of_players=self.logic_wrapper.get_players() #view all players
                    count = 1
                    for i in list_of_players:
                        print(f"{count}: {i.name}, ID: {i.id}")
                        count +=1  
                case "b": 
                    return




#----------------------------Edit player menu-----------------------------
        
        

    def edit_player_menu(self,Player_ID:str):
        """Display the Edit Player menu for a specific player.

        Args:
            Player_ID (str):
                National ID of the player to edit.

        Options:
            1 -> Edit Name
            2 -> Edit Phone Number
            3 -> Edit Address
            4 -> Edit Email
            5 -> Edit Player Handle (not implemented)
            6 -> Edit Player Link (not implemented)
            b -> Back

        On successful edit, the updated player is persisted via LogicWrapper.
        """
        temp : Player|int = self.logic_wrapper.get_player_by_ID(Player_ID)  
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
b. Back


""")
            choice=input("Enter input: ")
            if choice not in ["1","2","3","4","5","6","b","B"]:
                
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
b. Back

Try again!!
""")   
            if isinstance(temp, int):
                print("Player not found")
            else:
                
                match choice:
                    case "1": 
                        inp=self.functionFile.input_name() 
                        if isinstance(inp,str):
                            temp.name=inp
                        if inp == False:
                            return
                    case "2": 
                        inp=self.functionFile.input_phone_nr()
                        if isinstance(inp,int):
                            temp.phone=inp
                        if inp == False:
                            return
                    case "3": 
                        temp.address = input("Enter New address: ") 
                        if temp.address== "q":
                            return    
                    case "4": 
                        inp = self.functionFile.input_email()
                        if isinstance(inp,str):
                            temp.email=inp
                        if inp == False:
                            return
                    case "5": 
                        pass 
                    case "6": 
                        pass
                    case "7": 
                        pass
                    case "b": 
                        return
                self.logic_wrapper.modify_player(temp)
                print("Player has been modified!")

    
