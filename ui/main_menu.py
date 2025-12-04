from __future__ import annotations
# ui_layer/main_menu.py
from logic.logic_wrapper import LogicWrapper
from models.team import Team
from models.tournament import Tournament

from models.player import Player

class MainMenu:
    def __init__(self):
        # The UI creates an instance of the Logic Wrapper
        self.logic_wrapper = LogicWrapper()
        self.backlist = []





    def run(self):
        
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

        match choice:
            case "1": 
                self.organizer_menu()
            case "2": 
                self.team_leader_menu()
            case "3": 
                self.public_main_menu()
            case "4": 
                self.enable_high_quality_menu() # Mögulega laga því fer bara á mainscreen, mögulega myndum senda bara beint í function
            case "q": 
                return
            case _: 
                pass
        return


    def organizer_menu(self):
        print(
""" 
Organizer Menu

1. Player Management
2. Tournament Management
b. Back


""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                self.player_management_menu()
            case "2": 
                self.tournament_management_menu()
            case "b": 
                pass
        return


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
        choice=input("Enter input: ")

        match choice:
            case "1": 
                nID:int=int(input("National ID:"))
                name:str=input("Name: ")
                phone:int=int(input("Phone number:"))
                address:str=input("Address: ")
                email:str=input("Email: ")
                self.logic_wrapper.create_player(nID,name,phone,address,email)
            case "2": 
                self.edit_player_menu(int(input("Player National ID:")))  #Asks the user for Players National Id before going to the edit page
            case "3": 
                ID=int(input("Enter National ID: "))

                check= self.logic_wrapper.get_player_by_ID(ID)
                while check is False:
                    print("Player does not exist, Try different ID")
                    ID=int(input("Enter National ID: "))
                    check= self.logic_wrapper.get_player_by_ID(ID)
                x=input("Are you sure? (Y/N)")
                if x=="y" or x=="Y":
                    self.logic_wrapper.delete_player(ID)
                return

                

                
            case "4": 
                self.view_players_menu()
            case "b": 
                pass
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
             
            temp:Player = self.logic_wrapper.get_player_by_ID(Player_ID)

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
        
        
    




    def tournament_management_menu(self):
        print(
""" 
Tournament Management 

1. Create Tournament
2. Edit Tournament information 
3. Cancel Tournament
4. Select Tournament
b. Back 


""")
        
        while True:
            choice=input("Enter input: ")
            if choice not in ["1","2","3","4","b","B"]:
                
                print(
""" 
Invalid Input!!

Tournament Management 

1. Create Tournament
2. Edit Tournament information 
3. Cancel Tournament
4. Select Tournament
b. Back 

Try again!!
""")
            
            match choice:
                case "1": 
                    pass
                case "2": 
                    self.edit_tournament_menu(int(input("Enter Tournament ID: ")))
                case "3": 
                    pass
                case "4": 
                    self.select_tournament_menu()
                case "b": 
                    return
            
        




    def edit_tournament_menu(self,tournamentID):
        print(
""" 
Edit Tournament Information

1. Name Of Tournament
2. Start Date 
3. End Date
4. Location
5. Enter Number Of Teams
6. Edit Tournament Structure
b. Back 


""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                pass
            case "2": 
                pass
            case "3": 
                pass
            case "4": 
                pass
            case "5": 
                pass
            case "6": 
                pass
            case "b": 
                pass
        return
    def select_tournament_menu(self):
        print(
""" 
Select "nafn liðs"   ATH !!!!

1. Generate Schedule
2. Record Game Results
3. Accept Teams
4. Manage Rewards
5. Retrieve Records
b. Back 


""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                pass
            case "2": 
                pass
            case "3": 
                pass
            case "4": 
                pass
            case "5": 
                pass
            case "b": 
                pass
        return 
    def team_leader_menu(self):
        print(
""" 
Team Leader Menu

1. View Team (view menu shortcut)
2. Register for Tournament
3. Create Team
4. Edit Team
5. Delete Team
6. Manage Club
7. Rewards menu
b. Back 
""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                self.view_team_teamleader_menu()
            case "2": 
                self.register_for_tournament_menu()
            case "3": 
                self.create_team()
            case "4": 
                self.edit_team_menu(int(input("Enter Team ID: ")))  # before going to the page, it askes the user for id of the team that the user wants to edit
            case "5": 
                pass  #call funciton delete_team()
            case "6": 
                self.club_menu()
            case "7": 
                self.rewards_menu_teamleader()
            case "b": 
                pass
        return
    



    def rewards_menu_teamleader(self):
        print(
""" 
Rewards Menu

1. Rewards points
2. Rewards Log
b. Back 
""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                pass  #function rewardspoints
            case "2": 
                pass # funtion rewardslog
            case "b": 
                pass
        return
    



    def view_team_teamleader_menu(self):
        print(
""" 
View Team

1. View My Team Info (view menu shortcut)
2. View My Tournaments (view menu shortcut)
b. Back 
""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                pass  # call funtion for specific team to check out
            case "2": 
                pass # call funtion for specific team to check ou
            case "b": 
                pass
        return
    



    def register_for_tournament_menu(self):
        print(
""" 
Register For Tournament Menu

1. Request to Join Tournament
2. Leave Tournament (view menu shortcut)
b. Back 


""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                pass
            case "2": 
                pass
            case "b": 
                pass
        return

    def edit_team_menu(self,team_to_edit):
        print(
""" 
Edit Team Menu

1. Add Member
2. Remove Member
3. Change Team Name
4. Change Team Tag
5. Change Team Captain
6. Change ASCII art
b. Back 


""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                pass
            case "2": 
                pass
            case "3": 
                pass
            case "4": 
                pass
            case "5": 
                pass
            case "6": 
                pass
            case "b": 
                pass
        return
    
    def club_menu(self):
        print(
""" 
Club Menu

1. Create Club (removed after creation)
2. Join Club (remove after joining)
3. View My Club Info (view emenu shortcut)
4. Edit Club
b. Back 


""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                pass #create club function
            case "2": 
                pass # join club function
            case "3": 
                pass # view club by id
            case "4": 
                self.edit_club_menu()
            case "b": 
                pass
        return
    
    def edit_club_menu(self):
        print(
""" 
Edit Club Menu

1. Change colour
2. Quit club
3. Change club name
4. Change club location
b. Back


""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                pass
            case "2": 
                pass
            case "3": 
                pass
            case "4": 
                pass
            case "b": 
                pass
        return
    def enable_high_quality_menu(self):
        print(
""" 
Enable high quality (Y/N)

""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                pass
        return

    def public_main_menu(self):
        print(""" 
Public main menu

1. View Players
2. View Teams
3. View Tournaments
4. View Clubs
5. View Scoreboard
6. View Organizers
b. Back


""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                self.view_players_menu()
            case "2": 
                self.view_team_menu()
            case "3": 
                self.view_tournaments_menu()
            case "4": 
                self.view_clubs()
            case "5": 
                self.view_scoreboard()
            case "6": 
                self.view_organizers()
            case "b": 
                pass
        return
    


    def view_players_menu(self):
        print(
""" 
View Players menu

1. View All Players
2. View Player In Teams
3. View PLayers In Tournaments
4. View Specific Players
5. View Statistics
b. Back


""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                self.logic_wrapper.get_players() #view all players
            case "2": 
                teams=self.logic_wrapper.get_teams()
                for x in teams:
                    team=self.logic_wrapper.get_team_by_ID(x.id)
                    if type(team) == Team:
                        print(f"Team: {team.name}\n")
                        for pl in team.member_list:
                            print(pl)

                
                
                
                
                 # View players in team
            case "3": 
                tournaments=self.logic_wrapper.get_turnaments()
                for i in tournaments:
                    tournament=self.logic_wrapper.get_tournament_by_ID(i.id) # type: ignore
                    if type(tournament) == Tournament:
                        print(f"Tournament: {tournament.name}\n")
                        for j in tournament.team_list:
                            team = self.logic_wrapper.get_team_by_ID(j)
                            if type(team) == Team:
                                print(f"Team: {team.name}\n")
                                for pl in team.member_list:
                                    print(pl)
                pass#self.logic_wrapper.
                #self.logic_wrapper.get_team_by_ID(input("Enter Team : "))
            case "4": 
                player_ID = input("Enter player ID: ")
                x = self.logic_wrapper.get_player_by_ID(player_ID)
                print(f"name: {x.name}")
                print(f"KT: {x.kt}")
                print(f"dob: {x.dob}")
                print(f"phone: {x.phone}")
                print(f"address: {x.address}")
                print(f"email: {x.email}")

                # view specific player
            case "5": 
                pass # view statistics team
            case "b": 
                pass
        return

    def view_team_menu(self):
        print(
""" 
View Team menu

1. View All Teams
2. View Teams In Tournament
3. View Visual Team Tournaments
4. View Statistics
5. View specific team
b. Back


""")
        choice=input("Enter input: ")

        match choice:
            case "1":                      
                # Diana
                teams = self.logic_wrapper.get_teams(teams)
                for team_Id in teams:
                    team = self.logic_wrapper.get_team_by_ID(team_Id)
                    print(team.name)

            case "2": 
                tournaments = self.logic_wrapper.get_turnaments()
                for i in tournaments:
                    tournament=self.logic_wrapper.get_tournament_by_ID(i.id) # type: ignore
                    if type(tournament) == Tournament:
                        print(f"Tournament: {tournament.name}\n")
                        for j in tournament.team_list:
                            team = self.logic_wrapper.get_team_by_ID(j)
                            if type(team) == Team:
                                print(f"Team: {team.name}\n")

            case "3": 
                pass
            case "4": 
                pass
            case "5":
                team_ID = input("Enter team ID: ")
                i = self.logic_wrapper.get_team_by_ID(team_ID)
                print(f"name: {i.name}")
                print(f"tag: {i.tag}")
                print(f"creator_id: {i.creator_id}")
                print(f"team_size: {i.team_size}")
                print(f"member_list: {i.member_list}")

            case "b": 
                pass
        return

    def view_tournaments_menu(self):
        print(
""" 
View Team menu

1. View All tournaments
2. View Visual Tournament Tree
3. View Visual match results
4. View Statistics
b. Back


""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                pass
            case "2": 
                pass
            case "3": 
                pass
            case "4": 
                pass
            case "b": 
                pass
        return
    def view_clubs(self):
        print(
""" 
View Clubs Menu

1. View All Clubs
2. View Club by ID
3. View Statistics
b. Back


""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                pass
            case "2": 
                pass
            case "3": 
                pass
            case "b": 
                pass
        return

    def view_organizers(self):
        print(
""" 
View All Organizers Menu

1. View All Organizers
b. Back


""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                pass
            case "b": 
                pass
        return
    def view_scoreboard(self):
        print(
""" 
View Clubs Menu

1. View All Tournaments
b. Back


""")
        choice=input("Enter input: ")

        match choice:
            case "1": 
                pass
            case "b": 
                pass
        return
        
    
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
                    if val == str(x.kt) and x.kt not in team_list:
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
