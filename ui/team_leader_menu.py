from __future__ import annotations
# ui_layer/main_menu.py
from logic.logic_wrapper import LogicWrapper
from models.team import Team
from ui.function_file import functionFile
from models.club import Club
from models.player import Player


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
2. Register for Tournaments // remove
3. Create Team
4. Edit Team
5. Delete Team
6. Manage Club
7. Reward menu [Not implamented]
b. Back 
""")
            choice=input("Enter input: ")
            if choice not in ["1","2","3","4","5","6","7","b","B"]:

                print(
""" 
Invalid Input!!

Team Leader Menu

1. View My Team Info (view menu shortcut)
2. Register for Tournaments // remove
3. Create Team
4. Edit Team
5. Delete Team
6. Manage Club
7. Reward menu [Not implamented]
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
                    if name ==False:
                        return
                    team_tag = self.functionFile.inputTeamTag()
                    if team_tag ==False:
                        return
                    creator_id = self.functionFile.input_creatorID() # type: ignore
                    if creator_id ==False:
                        return
                    
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
                    ID=self.functionFile.checkTeamID()
                    if ID == False:
                        return
                    self.edit_team_menu(ID) 
                case "5": 
                    ID=self.functionFile.checkTeamID()
                    if ID == False:
                        return
                    x=input("Are you sure? (Y/N)")
                    if x.lower() == "y":
                        self.logic_wrapper.delete_team(ID) 
                        print("Team has been removed!")
                    else:
                        print("Deletion, canceled")
                    
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
                    teamID = self.functionFile.checkTeamID()
                    if teamID == False:
                        return
                    team = self.logic_wrapper.get_team_by_ID(teamID)
                    if isinstance(team, Team):
                        print(f"Team ID: {team.id}")  # call funtion for specific team to check out
                        print(f"Team name: {team.name}")
                        print(f"Team tag: {team.tag}")
                        print(f"Creator ID: {team.creator_id}")
                        print(f"Team size: {team.team_size}")
                        print("Team members ")
                        counter = 1
                        for id in team.member_list:
                            member = self.logic_wrapper.get_player_by_ID(id)
                            if isinstance(member,Player):
                                print(f"Member {counter}: {member.name}")
                                counter += 1
                case "2": 
                    teamID = self.functionFile.checkTeamID()
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
                    return
            

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
                    return
          

    def edit_team_menu(self,teamID:int):
        temp: Team | int = self.logic_wrapper.get_team_by_ID(teamID)
        while True:
            print(
""" 
Edit Team Menu

1. Add Member
2. Remove Member
3. Change Team Name
4. Change Team Tag
5. Change ASCII art [Not implamented]
b. Back 


""")
            choice=input("Enter input: ")
            if choice not in ["1","2","3","4","5","b","B"]:
                
                print(
""" 
Invalid Input!!

Edit Team Menu

1. Add Member
2. Remove Member
3. Change Team Name
4. Change Team Tag
5. Change ASCII art [Not implamented]
b. Back 

Try again!!
""")
            if isinstance(temp, int):
                print("Player not found")
            else:
                match choice:
                    case "1": 
                    
                        counter=0
                        for _ in temp.member_list:
                            counter+=1
                        if counter==temp.team_size:
                            print("Team is full")
                            continue
                        else:
                            member=self.functionFile.check_excistingID()
                            if member==False:
                                print("Addition of member canceled!")
                                return
                            else:
                                temp.member_list.append(member)

                            
                    case "2": 
                            counter=0
                            for _ in temp.member_list:
                                counter+=1
                            if counter==0:
                                print("Team is empty")
                                continue
                            member=self.functionFile.check_excistingID()
                            if member==False:
                                print("Removal of player canceled!")
                                return
                            else:
                                temp.member_list.remove(member)
                    case "3": 
                        imp =self.functionFile.inputTeamName()
                        if isinstance(imp,str):
                            temp.name=imp
                        if imp == False:
                            print("Name change aborted!")
                            return
                    case "4": 
                        imp=self.functionFile.inputTeamTag()
                        if isinstance(imp,str):
                            temp.tag=imp
                        if imp == False:
                            print("Team tag change aborted!")
                            return
                            
                    case "5": 
                        pass
                    case "b": 
                        return
                
                self.logic_wrapper.modify_team(temp)
                print("Team has been modified!")
           
               
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
                    name = self.functionFile.inputClubName()
                    if name == False:
                        return
                    club_color = self.functionFile.inputClubColor()
                    if club_color == False:
                        return
                    team_list=[] 
                    team=self.functionFile.checkTeamID()
                    if team==False:
                        return
                    else:
                        team_list.append(team)

                    self.logic_wrapper.create_club(name,club_color,team_list) #create club function
                    print("Club has been created!")
                case "2": 
                    pass # join club function
                case "3": 
                    club_id=self.functionFile.inputClubID()
                    if club_id==False:
                        return
                    else:
                        club_info=self.logic_wrapper.get_club_by_ID(club_id) # view club by id
                        if isinstance(club_info,Club):
                            print(f"Club name: {club_info.name}")
                            print(f"Club colour: {club_info.colours}")
                            for team_ID in club_info.teams:
                                team=self.logic_wrapper.get_team_by_ID(team_ID)
                                if isinstance(team, Team):
                                    print(team.name)
                                



                case "4": 
                    clubID = self.functionFile.checkTeamID()
                    self.edit_club_menu(clubID)
                case "b": 
                    return
            
    
    def edit_club_menu(self, clubID:int):
        temp : Club | int = self.logic_wrapper.get_club_by_ID(clubID)
        while True:
            print(
""" 
Edit Club Menu

1. Change club name
2. Change club colour
3. Add Team to club
4. Remove team from club
b. Back


""")
            choice=input("Enter input: ")
            if choice not in ["1","2","3","4","b","B"]:
                
                print(
""" 
Invalid Input!!

Edit Club Menu

1. Change club name
2. Change club colour
3. Add Team to club
4. Remove team from club
b. Back

Try again!!
""")
            if isinstance(temp,int):
                print("Club not found")
            else:
                match choice.lower():
                    case "1": 
                        inp = self.functionFile.inputClubName()
                        if isinstance(inp,str):
                            temp.name=inp
                        if inp == False:
                            return
                    case "2": 
                        inp = self.functionFile.inputClubColor()
                        if isinstance(inp,str):
                            temp.colours=inp
                        if inp == False:
                            return
                    case "3": 
                        team=self.functionFile.checkTeamID()
                        if team==False:
                            return
                        else:
                            temp.teams.append(team)
                    case "4": 
                        club = self.logic_wrapper.get_club_by_ID(clubID)
                        counter = 0
                        if isinstance(club,Club):
                            for _ in club.teams:
                                counter += 1
                            if counter == 0:
                                print("Clubs are empty")
                                return
                            team = self.functionFile.checkTeamID()
                            if team==False:
                                return
                            else:
                                temp.teams.remove(team)
                    case "b": 
                        return
                self.logic_wrapper.modify_club(temp)
                print("Club has been modified!")
    
    #-------------Functions-----------------
