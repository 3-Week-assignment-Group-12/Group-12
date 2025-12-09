from __future__ import annotations
# ui_layer/main_menu.py
from logic.logic_wrapper import LogicWrapper
from models.team import Team
from ui.function_file import functionFile


class TeamLeader():
    def __init__(self,low : LogicWrapper,functionFile:functionFile) -> None:
        self.logic_wrapper = low
        self.functionFile = functionFile



    def teamleader_menu(self):

        while True:
            print(
""" 
Team Leader Menu

1. View My Team Info (view menu shortcut)
2. Register for Tournaments
3. Create Team
4. Edit Team
5. Delete Team
6. Manage Club
7. Reward menu
b. Back 
""")
            choice=input("Enter input: ")
            if choice not in ["1","2","3","4","5","6","7","b","B"]:

                print(
""" 
Invalid Input!!

Team Leader Menu

1. View My Team Info (view menu shortcut)
2. Register for Tournaments
3. Create Team
4. Edit Team
5. Delete Team
6. Manage Club
7. Reward menu
b. Back 

Try again!!
""")

            match choice:
                case "1": 
                    self.view_team_teamleader_menu() 
                case "2": 
                    self.register_for_tournament_menu() 
                case "3": 
                    #new
                    name = self.functionFile.inputTeamName()
                    team_tag = self.functionFile.inputTeamTag()
                    creator_id = self.functionFile.input_creatorID() # type: ignore
                    
                    team_list=[] #laga team list 
                    val = input("add members? (y/n)")
                    if val.lower() == "y":
                        while True:
                            team_size = int(input("Enter team size: "))
                            if team_size > 21:
                                print("team too big")
                                continue
                            if team_size > self.logic_wrapper.get_players().__len__():
                                print("not enough players in system for team size")
                            else:
                                break
                        while team_list.__len__() != team_size:
                            team_list.append(self.functionFile.inputplayersID())
                    else:
                        team_size = int(input("Enter team size: "))

                    #old

                    name = self.functionFile.check_for_team_name()
                    team_tag = self.functionFile.check_for_team_tag()
                    creator_id = input("Enter team creator id: ")
                    
                    
                            

                    
                    ret = self.logic_wrapper.create_team(name, team_tag, creator_id, team_size, team_list) 
                    if ret == 1:
                        print("Team has been created!") 
                    elif ret == -1:
                        print("Error creating team!")
                    elif ret == -2:
                        print("Validation failed, team not created!")
                    elif ret == -3:
                        print("tag alredy exists")
                    elif ret == -4:
                        print("invalid format")
                    elif ret == -5:
                        print("team size to big")
                    
                case "4": 
                    ID=self.functionFile.inputTeamID()
                    self.edit_team_menu(ID) 
                case "5": 
                    ID=self.functionFile.inputTeamID()
                    x=input("Are you sure? (Y/N)")
                    if x=="y" or x=="Y":
                        self.logic_wrapper.delete_team(ID) # type: ignore
                    return     
                case "6": 
                    self.club_menu() 
                case "7": 
                    self.rewards_menu_teamleader()  
                case "b": 
                    return
           
    
    

    def view_team_teamleader_menu(self):

        while True:
            print(
""" 
View Team

1. View My Team Info (view menu shortcut)
2. View My Tournaments (view menu shortcut)
b. Back 
""")
            choice=input("Enter input: ")
            if choice not in ["1","2","b","B"]:

                print(
""" 
Invalid Input!!

View Team

1. View My Team Info (view menu shortcut)
2. View My Tournaments (view menu shortcut)
b. Back 

Try again!!
""")

            match choice:
                case "1": 
                    teamID = self.functionFile.inputTeamID()
                    team = self.logic_wrapper.get_team_by_ID(teamID)
                    if isinstance(team, Team):
                        print(team.id)  # call funtion for specific team to check out
                        print(team.name)
                        print(team.tag)
                        print(team.creator_id)
                        print(team.team_size)
                        print(team.member_list)
                case "2": 
                    teamID = self.logic_wrapper.inputTeamID()
                    list_of_tournaments= self.logic_wrapper.get_tournaments()
                    for tournament in list_of_tournaments:
                        listOfTeamID=tournament.team_list
                        if teamID in listOfTeamID:
                            print(tournament.name)
                case "b": 
                    return
           
    
    def rewards_menu_teamleader(self):

        while True:
            print(
""" 
Rewards Menu

1. Rewards points
2. Rewards Log
b. Back 
""")
            choice=input("Enter input: ")
            if choice not in ["1","2","b","B"]:

                print(
""" 
Invalid Input!!

Rewards Menu

1. Rewards points
2. Rewards Log
b. Back 

Try again!!
""")

            match choice:
                case "1": 
                    pass  #function rewardspoints
                case "2": 
                    pass # funtion rewardslog
                case "b": 
                    pass
            

    def register_for_tournament_menu(self):

        while True:
            print(
""" 
Register For Tournament Menu

1. Request to Join Tournament
2. Leave Tournament (view menu shortcut)
b. Back 


""")
            choice=input("Enter input: ")
            if choice not in ["1","2","b","B"]:

                print(
""" 
Invalid Input!!

Register For Tournament Menu

1. Request to Join Tournament
2. Leave Tournament (view menu shortcut)
b. Back 

Try again!!
""")

            match choice:
                case "1": 
                    pass
                case "2": 
                    pass
                case "b": 
                    pass
          

    def edit_team_menu(self,team_to_edit):

        while True:
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
            if choice not in ["1","2","3","4","5","6","b","B"]:
                
                print(
""" 
Invalid Input!!

Edit Team Menu

1. Add Member
2. Remove Member
3. Change Team Name
4. Change Team Tag
5. Change Team Captain
6. Change ASCII art
b. Back 

Try again!!
""")

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
                    return
           
    
    def club_menu(self):

        while True:
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
            if choice not in ["1","2","3","4","b","B"]:
                
                print(
""" 
Invalid Input!!

Club Menu

1. Create Club (removed after creation)
2. Join Club (remove after joining)
3. View My Club Info (view emenu shortcut)
4. Edit Club
b. Back 

Try again!!
""")

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
                    return
            
    
    def edit_club_menu(self):

        while True:
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
            if choice not in ["1","2","3","4","b","B"]:
                
                print(
""" 
Invalid Input!!

Edit Club Menu

1. Change colour
2. Quit club
3. Change club name
4. Change club location
b. Back

Try again!!
""")

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
                    return
    
    #-------------Functions-----------------
