from logic.logic_wrapper import LogicWrapper
from models.team import Team
from ui.function_file import functionFile
from models.club import Club
from models.player import Player


class TeamLeader():
    """Menu and actions available for team leaders.

    This class provides interactive menus for team leaders to:
        - View their teams and tournaments.
        - Create, edit, and delete teams.
        - Manage club membership and club data.
        - Access reward-related menus (currently placeholders).
    """
    def __init__(self,low : LogicWrapper,functionFile:functionFile) -> None:
        """Initialize TeamLeader menu with shared dependencies.

        Args:
            low (LogicWrapper):
                Logic wrapper instance responsible for business logic and
                data access operations.
            functionFile (functionFile):
                Helper instance for user input and shared utility functions.
        """
        self.logic_wrapper = low
        self.functionFile = functionFile



    def teamleader_menu(self) -> None:
        """Display the top-level Team Leader menu and route to sub-menus.

        Options:
            1 -> View My Team Info (shortcut into public view)
            2 -> Register for Tournaments (currently placeholder)
            3 -> Create Team
            4 -> Edit Team
            5 -> Delete Team
            6 -> Manage Club
            7 -> Reward menu (not implemented)
            b -> Back

        The loop continues until the user chooses 'b' / 'B'.
        """
        while True:
            print(
""" 
Team Leader Menu

1. View My Team Info
2. Create Team
3. Edit Team
4. Delete Team
5. Manage Club
b. Back 
""")
            choice = input("Enter input: ")
            if choice not in ["1","2","3","4","5","b","B"]:

                print(
""" 
Invalid Input!!

Team Leader Menu

1. View My Team Info
2. Create Team
3. Edit Team
4. Delete Team
5. Manage Club
b. Back 

Try again!!
""")

            match choice:
                case "1": 
                    self.view_team_teamleader_menu() 

                case "2": 
                    name = self.functionFile.inputTeamName()
                    if name == False:
                        continue

                    team_tag = self.functionFile.inputTeamTag()
                    if team_tag == False:
                        continue

                    creator_id = self.functionFile.input_creatorID()
                    if creator_id == False:
                        continue
                    
                    team_list = []
                    val = input("Add members? (y/n): ")
                    if val.lower() == "y":
                        while True:
                            team_size = self.functionFile.teamSize()
                            if team_size > 21:
                                print("Team too big")
                                continue

                            if team_size > self.logic_wrapper.get_players().__len__():
                                print("Not enough players in system for team size")

                            else:
                                break

                        while team_list.__len__() != team_size:
                            team_list.append(self.functionFile.inputplayersID())

                    else:
                        team_size = self.functionFile.teamSize()

                    ret = self.logic_wrapper.create_team(name, team_tag, creator_id, team_size, team_list) 
                    if ret == 1:
                        print("Team has been created!") 

                    elif ret == -1:
                        print("Error creating team!")

                    elif ret == -2:
                        print("Validation failed, team not created!")

                    elif ret == -3:
                        print("tag already exists")

                    elif ret == -4:
                        print("invalid format")

                    elif ret == -5:
                        print("team size too big")
                    
                case "3": 
                    ID = self.functionFile.checkTeamID()
                    if ID == False:
                        continue

                    self.edit_team_menu(ID) 

                case "4": 
                    ID = self.functionFile.checkTeamID()
                    if ID == False:
                        continue

                    x = input("Are you sure? (Y/N): ")
                    if x.lower() == "y":
                        self.logic_wrapper.delete_team(ID) 
                        print("Team has been removed!")

                    else:
                        print("Deletion, canceled")
                        continue
                    
                case "5": 
                    self.club_menu() 

                case "b": 
                    return
           

    def view_team_teamleader_menu(self) -> None:
        """Display view-only options for the current team leader.

        Options:
            1 -> View my team info (full team details and members)
            2 -> View the tournaments my team participates in
            b -> Back
        """
        while True:
            print(
""" 
View Team

1. View My Team Info
2. View My Tournaments
b. Back 
""")
            choice = input("Enter input: ")
            if choice not in ["1","2","b","B"]:

                print(
""" 
Invalid Input!!

View Team

1. View My Team Info
2. View My Tournaments
b. Back 

Try again!!
""")

            match choice:
                case "1": 
                    teamID = self.functionFile.checkTeamID()
                    if teamID == False:
                        continue

                    team = self.logic_wrapper.get_team_by_ID(teamID)
                    if team == False:
                        continue

                    if isinstance(team, Team):
                        print(f"Team ID: {team.id}")  # call function for specific team to check out
                        print(f"Team name: {team.name}")
                        print(f"Team tag: {team.tag}")
                        print(f"Creator ID: {team.creator_id}")
                        print(f"Team size: {team.team_size}")
                        print("Team members")
                        counter = 1
                        for id in team.member_list:
                            member = self.logic_wrapper.get_player_by_ID(id)
                            if isinstance(member,Player):
                                print(f"Member {counter}: {member.name}")
                                counter += 1

                case "2": 
                    teamID = self.functionFile.checkTeamID()
                    list_of_tournaments = self.logic_wrapper.get_tournaments()
                    for tournament in list_of_tournaments:
                        listOfTeamID = tournament.team_list
                        if teamID in listOfTeamID:
                            print(tournament.name)

                case "b": 
                    return


    def edit_team_menu(self,teamID:int) -> None:
        """Display and handle the Edit Team menu for a specific team.

        Allows:
            - Adding members to the team.
            - Removing members from the team.
            - Changing the team name.
            - Changing the team tag.
            - Placeholder for ASCII art modification.

        Args:
            teamID (int): ID of the team to edit.
        """
        temp: Team | int = self.logic_wrapper.get_team_by_ID(teamID)
        while True:
            print(
""" 
Edit Team Menu

1. Add Member
2. Remove Member
3. Change Team Name
4. Change Team Tag
b. Back 


""")
            choice = input("Enter input: ")
            if choice not in ["1","2","3","4","b","B"]:
                
                print(
""" 
Invalid Input!!

Edit Team Menu

1. Add Member
2. Remove Member
3. Change Team Name
4. Change Team Tag
b. Back 

Try again!!
""")
                
            if isinstance(temp, int):
                print("Player not found")

            else:
                match choice:
                    case "1": 
                        counter = 0
                        for _ in temp.member_list:
                            counter += 1

                        if counter == temp.team_size:
                            print("Team is full")
                            continue

                        else:
                            member = self.functionFile.check_existingID()
                            if member == False:
                                print("Addition of member canceled!")
                                continue

                            else:
                                temp.member_list.append(member)

                    case "2": 
                            counter = 0
                            for _ in temp.member_list:
                                counter += 1

                            if counter == 0:
                                print("Team is empty")
                                continue

                            member = self.functionFile.check_existingID()
                            if member == False:
                                print("Removal of player canceled!")
                                continue

                            else:
                                temp.member_list.remove(member)

                    case "3": 
                        imp = self.functionFile.inputTeamName()
                        if imp == False:
                            print("Name change aborted!")
                            continue
                        
                        temp.name = imp

                    case "4": 
                        imp = self.functionFile.inputTeamTag()
                        if imp == False:
                            print("Team tag change aborted!")
                            continue

                        temp.tag = imp

                    case "b": 
                        return
                
                self.logic_wrapper.modify_team(temp)
                print("Team has been modified!")
           
               
    def club_menu(self) -> None:
        """Display the club management menu for team leaders.

        Options:
            1 -> Create club (single-use; removed after creation)
            2 -> Join club (placeholder)
            3 -> View my club info
            4 -> Edit club
            b -> Back
        """
        while True:
            print(
""" 
Club Menu

1. Create Club
2. View My Club Info
3. Edit Club
b. Back 


""")
            choice = input("Enter input: ")
            if choice not in ["1","2","3","b","B"]:
                
                print(
""" 
Invalid Input!!

Club Menu

1. Create Club
2. View My Club Info
3. Edit Club
b. Back  

Try again!!
""")

            match choice:
                case "1":
                    name = self.functionFile.inputClubName()
                    if name == False:
                        continue

                    club_color = self.functionFile.inputClubColor()
                    if club_color == False:
                        continue

                    team_list = [] 
                    team = self.functionFile.checkTeamID()
                    if team == False:
                        continue

                    else:
                        team_list.append(team)

                    self.logic_wrapper.create_club(name,club_color,team_list) #create club function
                    print("Club has been created!")

                case "2": 
                    club_id = self.functionFile.inputClubID()
                    if club_id == False:
                        continue

                    else:
                        club_info = self.logic_wrapper.get_club_by_ID(club_id) # view club by id
                        if isinstance(club_info,Club):
                            print(f"Club name: {club_info.name}")
                            print(f"Club colour: {club_info.colours}")
                            for team_ID in club_info.teams:
                                team = self.logic_wrapper.get_team_by_ID(team_ID)
                                if isinstance(team, Team):
                                    print(team.name)
                                
                case "3": 
                    clubID = self.functionFile.inputClubID()
                    if clubID == False:
                        continue
                    
                    self.edit_club_menu(clubID)

                case "b": 
                    return
            
    
    def edit_club_menu(self, clubID:int) -> None:
        """Display and handle the Edit Club menu.

        Allows:
            - Changing club name.
            - Changing club colour.
            - Adding a team to the club.
            - Removing a team from the club.

        Args:
            clubID (int): ID of the club to edit.
        """
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
            choice = input("Enter input: ")
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
                        if inp == False:
                            continue
                        
                        temp.name = inp

                        if inp == False:
                            continue

                    case "2": 
                        inp = self.functionFile.inputClubColor()
                        if inp == False:
                            continue

                        temp.colours = inp

                    case "3": 
                        team = self.functionFile.checkTeamID()
                        if team == False:
                            continue

                        else:
                            temp.teams.append(team)

                    case "4": 
                        club = self.logic_wrapper.get_club_by_ID(clubID)
                        if club == False:
                            continue

                        counter = 0
                        if isinstance(club,Club):       
                            for _ in club.teams:
                                counter += 1

                            if counter == 0:
                                print("Clubs are empty")
                                continue

                            team = self.functionFile.checkTeamID()
                            if team == False:
                                continue

                            else:
                                temp.teams.remove(team)

                    case "b": 
                        return
                    
                self.logic_wrapper.modify_club(temp)
                print("Club has been modified!")