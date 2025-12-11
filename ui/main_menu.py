from __future__ import annotations
# ui_layer/main_menu.py
from logic.logic_wrapper import LogicWrapper
from models.team import Team
from models.tournament import Tournament

from models.player import Player
from ui.Organizer_menu import OrganizerMenu
from ui.Public_main_menu import PublicMainMenu
from ui.team_leader_menu import TeamLeader
from ui.function_file import functionFile


class MainMenu:
    def __init__(self):
        # The UI creates an instance of the Logic Wrapper
        self.logic_wrapper = LogicWrapper()
        self.backlist = []
        self.functionFile = functionFile(self.logic_wrapper)
        self.my_organizer_menu = OrganizerMenu(self.logic_wrapper,self.functionFile)
        self.teamleader_menu = TeamLeader(self.logic_wrapper,self.functionFile)
        self.public_menu = PublicMainMenu(self.logic_wrapper,self.functionFile)






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
                    print("Goodbye!")
                    quit()
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
            
    


    
