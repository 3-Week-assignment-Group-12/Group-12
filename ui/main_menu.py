from __future__ import annotations
# ui_layer/main_menu.py
from logic.logic_wrapper import LogicWrapper
from models.team import Team
from models.tournament import Tournament

from models.player import Player
from ui.Organizer_menu import OrganizerMenu
from ui.Public_main_menu import PublicMainMenu
from ui.team_leader_menu import TeamLeader
from ui.tournament_management import TournamentManagement


class MainMenu:
    def __init__(self):
        # The UI creates an instance of the Logic Wrapper
        self.logic_wrapper = LogicWrapper()
        self.backlist = []
        self.my_organizer_menu = OrganizerMenu(self.logic_wrapper)
        self.teamleader_menu = TeamLeader(self.logic_wrapper)
        self.public_menu = PublicMainMenu(self.logic_wrapper)






    def run(self):

        while True:
            
            print( """
+---------------------------------------------------+
|                                                   |
|  ____  _   _        ____                   _      |
| |  _ \| | | |   ___/ ___| _ __   ___  _ __| |_    |
| | |_) | | | |  / _ \___ \| '_ \ / _ \| '__| __|   |
| |  _ <| |_| | |  __/___) | |_) | (_) | |  | |_    |
| |_| \_\\____/   \___|____/| .__/ \___/|_|   \__|   |
|                          |_|                      |
|                                                   |
+---------------------------------------------------+
""")
            print(
            
""" 
Welcome To the menu. 

1. Organizer Menu
2. Team Leader Menu
3. Public Menu
4. High quality Toggle
q. Quit 


""")
            choice=input("Enter input: ")
            if choice not in ["1","2","3","4","q","Q"]:

                 print(
""" 
Invalid Input!!

Welcome To the menu. 

1. Organizer Menu
2. Team Leader Menu
3. Public Menu
4. High quality Toggle
q. Quit 

Try again!!
""")

            match choice:
                case "1": 
                    self.my_organizer_menu.show_organizer_menu()
                case "2": 
                    self.teamleader_menu.teamleader_menu()
                case "3": 
                    self.public_menu.public_menu()
                case "4": 
                    self.enable_high_quality_menu() # Mögulega laga því fer bara á mainscreen, mögulega myndum senda bara beint í function
                case "q": 
                    return
                case _: 
                    pass
            self.run()
            
    def enable_high_quality_menu(self):
        print(
""" 
Enable high quality (Y/N)

""")
        while True:
            choice=input("Enter input: ")
            if choice not in ["y","Y"]:
                
                print(
""" 
Invalid Input!!

Enable high quality (Y/N)

Try again!!
""")

            match choice:
                case "1": 
                    pass
            
    
    def create_team(self):
        id_of_user= input("Enter Captains National ID: ")
        name = input("Enter team name: ")
        tag = input("Enter team tag (max 20 char): ")
        team_size = int(input("Enter team size: "))
        team_list = []
        choice = input("add members? (y/n): ").lower()
        
        if choice == "y":
            existing_players = self.logic_wrapper.get_players()
            while True:
                
                val = input("Enter team member Kennitala (q to stop): ")
                if val.lower() == "q":
                    break
                
                for x in existing_players:
                    if val == str(x.id) and x.id not in team_list:
                        team_list.append(int(val))
                        continue
                    
                print("player id not registered")
                print()
                    
                        
            
            
            
        
        
        self.logic_wrapper.create_team(name,tag,id_of_user,team_size,team_list)
        
        
    def create_player(self): # Requirement nr 1
        # UI gathers input
        name = input("Enter player Name: ")
        kt = int(input("Enter player kennitala:"))
        phone = int(input("Enter player phone: "))
        address = input("Enter player address: ")
        email = input("Enter player email: ")
        # UI talks ONLY to Logic
        self.logic_wrapper.create_player(kt,name,phone,address,email)
        

    def get_players(self): #Requirement 4
        # UI talks ONLY to Logic
        self.logic_wrapper.get_players()
