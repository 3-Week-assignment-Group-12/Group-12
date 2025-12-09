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
            
    
        #------------------Functions--------------------------#
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

    def check_for_tournament_ID(self):
        ID = int(input("Contact ID"))
        list_of_tournaments=self.logic_wrapper.get_tournaments()
        while True:
            
            if list_of_tournaments is None or list_of_tournaments == []:
                return ID
            for tournamentID in list_of_tournaments:
                tournament_info=self.logic_wrapper.get_team_by_ID(tournamentID.id)
                if isinstance(tournament_info,Tournament):
                    if ID == tournament_info.id: 
                        print("This tournament ID already exists!")
                        ID = int(input("Enter different Contact ID"))
                    else:
                        return ID
    


    def inputTournamentID(self):
        tournamentID=int(input("Enter Tournament ID: "))
        check= self.logic_wrapper.get_tournament_by_ID(tournamentID)
        while check is False:
            print("Tournament does not exist, Try different ID")
            tournamentID=int(input("Enter Tournament ID: "))
            check= self.logic_wrapper.get_tournament_by_ID(tournamentID)
        return tournamentID
    

    def check_for_team_name(self):

        name = input("Enter team name: ")
        list_of_teams=self.logic_wrapper.get_teams()
        if list_of_teams.__len__() == 0:
            return name
        else:
            while True:
                for team in list_of_teams:
                    teaminfo=self.logic_wrapper.get_team_by_ID(team.id)
                    if isinstance(teaminfo,Team):
                        if name == teaminfo.name:
                            print("Name already exists!")
                            name = input("Enter different team name: ")
                        else:
                            return name
                    else:
                        print("invalid name")
                        name = input("Enter different team name: ")
            
    def check_for_team_tag(self):
    
        tag = input("Enter team tag: ")
        list_of_teams=self.logic_wrapper.get_teams()
        while True: 
            
            if list_of_teams is None or list_of_teams == []:
                    return tag
            for teamID in list_of_teams:
                teaminfo=self.logic_wrapper.get_team_by_ID(teamID.id)
                if isinstance(teaminfo,Team):
                    if tag == teaminfo.tag: 
                        print("Tag already exists!")
                        tag = input("Enter different team tag: ")
                    else:
                        return tag
                    


    def inputTeamID(self):
        teamID=int(input("Enter Team ID: "))
        check= self.logic_wrapper.get_team_by_ID(teamID)
        while check is False:
            print("Team does not exist, Try different ID")
            teamID=int(input("Enter Team ID: "))
            check= self.logic_wrapper.get_team_by_ID(teamID)
        return teamID
    
    def inputplayersID(self):
        playersID=input("Enter National ID: ")
        check= self.logic_wrapper.get_player_by_ID(playersID)
        while check is not isinstance(check, Player):
            print("Player does not exist, Try different ID")
            playersID=input("Enter National ID: ")
            check= self.logic_wrapper.get_player_by_ID(playersID)
        return playersID
    


    def check_for_player_kt(self) -> str:
            nID:str=input("National ID: ")
            list_of_players= self.logic_wrapper.get_players()
            while True:
                if list_of_players is None or list_of_players == []:
                    return nID
                for player in list_of_players:
                    playerinfo=self.logic_wrapper.get_player_by_ID(player.id)
                    if isinstance(playerinfo,Player):
                        if nID == playerinfo.id: 
                            print("This national ID already exists!")
                            nID=input("Enter different National ID: ")
                        else:
                            return nID
                        

    def check_for_player_email(self,email):
        list_of_players=self.logic_wrapper.get_players()
        if list_of_players is None or list_of_players == []:
            return True
        for player in list_of_players:
            playerinfo=self.logic_wrapper.get_player_by_ID(player.id)
            if isinstance(playerinfo,Player):
                if email == playerinfo.email: 
                    print("This email already exists!")
                    return False
                else:
                    return True
                
    

    def input_phone_nr(self):
        while True:
            number:str=input("Phone number:")
            check = self.logic_wrapper.check_phone_nr(number)
            if check == "1":
                print("Phone number is not the correct length!")
            elif check == "2":
                print("Only digits in phone number allowed!")

    def input_name(self):
        while True:
            name:str=input("Name: ")
            check = self.logic_wrapper.check_name(name)
            if check == "1":
                print("Numbers are not allowed in name!")
                
    def input_email(self):
        check2= False
        email=""
        while check2 == False :
            email:str=input("Email: ")
            check1=self.logic_wrapper.check_email(email)
            if check1 ==True:
                check2=self.check_for_player_email(email)
        return email
            
        



    
