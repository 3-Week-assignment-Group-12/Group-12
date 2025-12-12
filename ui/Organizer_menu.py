from __future__ import annotations
# ui_layer/main_menu.py
from logic.logic_wrapper import LogicWrapper
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
            choice = input("Enter input: ")
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
4. View players
5. Get dummy data
b. Back 


""")
            choice = input("Enter input: ")
            if choice not in ["1","2","3","4","5","b","B"]:

                 print(
""" 
Invalid Input!!

Player Management 

1. Add player
2. Edit player information
3. Delete player
4. View players
5. Get dummy data
b. Back 

Try again!!
""")
                 
            match choice:
                case "1": 
                    nid = self.functionFile.inputplayersID()  # case 1 will ask the user for each and every variable that is needed for creating a player 
                    if nid == False:                          # if user wants to quit anytime it will return false, when it return false it takes us to the 
                        continue                              # Player Management menu (it stops the loop and restarts it) from there you can go back by pressing b.

                    name = self.functionFile.input_name()
                    if name == False:
                        continue

                    handle = self.functionFile.inputPlayerHandle()
                    if handle == False:
                        continue

                    link = self.functionFile.inputPlayerLink()
                    if link == False:
                        continue

                    phone = self.functionFile.input_phone_nr()
                    if phone == False:
                        continue

                    address:str=input("Address: ")             
                    if address == "q":
                        continue

                    email = self.functionFile.input_email()
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
                    id = self.functionFile.check_existingID()     # case 2 check if playerID exists in system, but it will ask untill you find a player
                    if id == False:                               # when found it will go to the edit_player_menu(). 
                        continue

                    else:   
                        self.edit_player_menu(id) 

                case "3":                                          # same as case 2 but when you find a player you are asked if you are sure want to delete player
                    ID = self.functionFile.check_existingID()      # if typed in "y" or uppercase "Y", it will delete the player otherwise go back to menu
                    if ID == False:
                        continue

                    x = input("Are you sure? (Y/N)").lower()
                    if x == "y":                                
                        self.logic_wrapper.delete_player(ID) 
                        print("Player has been deleted!")

                    else:
                        print("Player was not deleted.(canceled)")
                        continue

                        

                case "4":                                             # case 4n Gets list of player, goes through it and prints allt players in system
                    list_of_players = self.logic_wrapper.get_players() 
                    count = 1
                    for player in list_of_players:                  
                        print(f"{count}: {player.name}, ID: {player.id}")
                        count += 1  
                        
                case "5":
                    print("Warning!")
                    print("This will wipe currently existing data")
                    val = input("Confirm? (y/n)")
                    if val.lower() == "y":
                        self.logic_wrapper.get_dummy_data()
                        print("Dummy data loaded")
                        continue
                    else:
                        print("Dummy data has not been loaded")
                    

                case "b": 
                    return

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
            choice = input("Enter input: ")
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
                
                match choice:                       # edit player ask for only one atribute at a time and updates it if found valid input otherwise back to edit menu 
                    case "1": 
                        inp = self.functionFile.input_name() 
                        if inp == False:
                            continue
                           
                        temp.name = inp

                    case "2": 
                        inp = self.functionFile.input_phone_nr()
                        if inp == False:
                            continue
                      
                        temp.phone = inp

                    case "3": 
                        temp.address = input("Enter New address: ") 
                        if temp.address == "q":
                            continue  

                    case "4": 
                        inp = self.functionFile.input_email()
                        if inp == False:
                            continue

                        temp.email = inp

                    case "5": 
                        inp = self.functionFile.inputPlayerHandle()
                        if inp == False:
                            continue
                            
                        temp.handle = inp
          
                    case "6": 
                        inp = self.functionFile.inputPlayerLink()
                        if inp == False:
                            continue

                        temp.link = inp
                    
                    case "b": 
                        return
                    
                self.logic_wrapper.modify_player(temp)
                print("Player has been modified!")

    
