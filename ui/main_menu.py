# ui_layer/main_menu.py
from logic.logic_wrapper import LogicWrapper

class MainMenu:
    def __init__(self):
        # The UI creates an instance of the Logic Wrapper
        self.logic_wrapper = LogicWrapper()





    def run(self):
        self.create_player()
        self.create_team(1234567890)
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
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case 4: 
                pass
            case "q": 
                pass
            case _: 
                pass
        


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
            case 1: 
                pass
            case 2: 
                pass
            case b: 
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
        choice=input("Enter input: ")

        match choice:
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case 4: 
                pass
            case b: 
                pass
    

    def edit_player_menu(self):
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
8. Confirm or cancel


""")
        choice=input("Enter input: ")

        match choice:
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case 4: 
                pass
            case 5: 
                pass
            case 6: 
                pass
            case 7: 
                pass
            case 8: 
                pass

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
        choice=input("Enter input: ")

        match choice:
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case 4: 
                pass
            case b: 
                pass

    def edit_tournament_menu(self):
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
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case 4: 
                pass
            case 5: 
                pass
            case 6: 
                pass
            case b: 
                pass

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
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case 4: 
                pass
            case 5: 
                pass
            case b: 
                pass

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
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case 4: 
                pass
            case 5: 
                pass
            case 6: 
                pass
            case 7: 
                pass
            case b: 
                pass

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
            case 1: 
                pass
            case 2: 
                pass
            case b: 
                pass
        
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
            case 1: 
                pass
            case 2: 
                pass
            case b: 
                pass


    def edit_team_menu(self):
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
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case 4: 
                pass
            case 5: 
                pass
            case 6: 
                pass
            case b: 
                pass

    
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
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case 4: 
                pass
            case b: 
                pass

    
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
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case 4: 
                pass
            case b: 
                pass

    def enable_high_quality_menu(self):
        print(
""" 
Enable high quality (Y/N)

""")
        choice=input("Enter input: ")

        match choice:
            case 1: 
                pass


    def public_main_menu(self):
        print(
""" 
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
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case 4: 
                pass
            case 5: 
                pass
            case 6: 
                pass
            case b: 
                pass

    def view_players_menu(self):
        print(
""" 
View Players menu

1. View All Players
2. View Player In Teams
3. View PLayers In Tournaments
4. View Specific Players
5. View Specific Team
b. Back


""")
        choice=input("Enter input: ")

        match choice:
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case 4: 
                pass
            case 5: 
                pass
            case b: 
                pass


    def view_team_menu(self):
        print(
""" 
View Team menu

1. View All Teams
2. View Teams In Tournament
3. View Visual Team Tournaments
4. View Statistics
5. View Statistic
b. Back


""")
        choice=input("Enter input: ")

        match choice:
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case 4: 
                pass
            case 5: 
                pass
            case b: 
                pass


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
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case 4: 
                pass
            case b: 
                pass

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
            case 1: 
                pass
            case 2: 
                pass
            case 3: 
                pass
            case b: 
                pass
    

    def view_organizers(self):
        print(
""" 
View All Organizers Menu

1. View All Organizers
b. Back


""")
        choice=input("Enter input: ")

        match choice:
            case 1: 
                pass
            case b: 
                pass

    def view_scoreboard(self):
        print(
""" 
View Clubs Menu

1. View All Tournaments
b. Back


""")
        choice=input("Enter input: ")

        match choice:
            case 1: 
                pass
            case b: 
                pass

        
    
    def create_team(self, id_of_user:int):
        
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
