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
    """Entry point for the console-based UI.

    This class is responsible for:
        - Instantiating the LogicWrapper and UI helper classes.
        - Displaying the main menu.
        - Routing the user to Organizer, Team Leader, or Public menus.
    """
    def __init__(self):
        """Initialize the main menu and all sub-menus.

        Creates a LogicWrapper instance and wires it into:
            - OrganizerMenu
            - TeamLeader
            - PublicMainMenu
            - functionFile helper

        Attributes:
            logic_wrapper (LogicWrapper):
                Logic layer facade used by all UI components.
            backlist (list):
                Stack/list intended for back navigation (currently unused).
            functionFile (functionFile):
                Helper for input/validation functions shared across menus.
            my_organizer_menu (OrganizerMenu):
                UI menu for organizer-related actions.
            teamleader_menu (TeamLeader):
                UI menu for team leader actions.
            public_menu (PublicMainMenu):
                UI menu for public/readonly viewing actions.
        """
        # The UI creates an instance of the Logic Wrapper
        self.logic_wrapper = LogicWrapper()
        self.backlist = []
        self.functionFile = functionFile(self.logic_wrapper)
        self.my_organizer_menu = OrganizerMenu(self.logic_wrapper,self.functionFile)
        self.teamleader_menu = TeamLeader(self.logic_wrapper,self.functionFile)
        self.public_menu = PublicMainMenu(self.logic_wrapper,self.functionFile)





#----------------------------Main menu-----------------------------
        
        


    def run(self):
        """Run the main application loop.

        Displays the ASCII art banner and the top-level menu, then
        routes user input to the appropriate submenu:

            1 -> Organizer menu
            2 -> Team Leader menu
            3 -> Public menu
            q -> Quit application

        The method loops indefinitely until the user chooses to quit.

        Returns:
            None
        """
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
q. Quit 


""")
            choice=input("Enter input: ")
            if choice not in ["1","2","3","q","q"]:

                 print(
""" 
Invalid Input!!

Welcome To the menu. 

1. Organizer Menu
2. Team Leader Menu
3. Public Menu
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
                case "q": 
                    print("Goodbye!")
                    quit()
                case _: 
                    pass
            self.run()
            
            
    


    
