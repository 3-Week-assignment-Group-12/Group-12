from __future__ import annotations
# ui_layer/main_menu.py
from models.club import Club
from logic.logic_wrapper import LogicWrapper
from models.team import Team
from models.tournament import Tournament
from models.player import Player
from ui.function_file import functionFile





class PublicMainMenu():

    def __init__(self,low : LogicWrapper,functionFile:functionFile) -> None:
        self.logic_wrapper = low
        self.functionFile = functionFile

    #-----------------------Public Main menu----------------------------
    def public_menu(self):

        while True:
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
            if choice not in ["1","2","3","4","5","6","b","B"]:
                
                print(
""" 
Invalid Input!!

Public main menu

1. View Players
2. View Teams
3. View Tournaments
4. View Clubs
5. View Scoreboard
6. View Organizers
b. Back

Try again!!
""")

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
                    return
           
    
#-----------------------Veiw player ----------------------------




    def view_players_menu(self):

        while True:
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
            if choice not in ["1","2","3","4","5","b","B"]:
                
                print(
""" 
Invalid Input!!

View Players menu

1. View All Players
2. View Player In Teams
3. View PLayers In Tournaments
4. View Specific Players
5. View Statistics
b. Back

Try again!!
""")

            match choice:
                case "1": 
                    list_of_players=self.logic_wrapper.get_players() #view all players
                    count = 1
                    for i in list_of_players:
                        print(f"{count}: {i.name}, ID: {i.id}")
                        count +=1
                        
                case "2": 
                    teams=self.logic_wrapper.get_teams()
                    for x in teams:
                        team=self.logic_wrapper.get_team_by_ID(x.id)
                        if type(team) == Team:
                            print(f"Team: {team.name}\n")
                            count = 0
                            for pl in team.member_list:
                                player = self.logic_wrapper.get_player_by_ID(pl)
                                if type(player) == Player:
                                    
                                    print(f"{count}: {player.name}, ID: {player.id}")
                                    count +=1
                                    
                    # View players in team
                case "3": 
                    tournaments=self.logic_wrapper.get_tournaments()
                    for i in tournaments:
                        tournament=self.logic_wrapper.get_tournament_by_ID(i.id) # type: ignore
                        if type(tournament) == Tournament:
                            print(f"Tournament: {tournament.name}\n")
                            for j in tournament.team_list:
                                team = self.logic_wrapper.get_team_by_ID(j)
                                if type(team) == Team:
                                    print(f"Team: {team.name}\n")
                                    count =1
                                    for pl in team.member_list:
                                        player = self.logic_wrapper.get_player_by_ID(pl)
                                        if type(player) == Player:
                                    
                                            print(f"{count}: {player.name}, ID: {player.id}")
                                            count +=1
                                            
                case "4":
                    while True:
                        player_ID = input("Enter player ID: ")
                        if isinstance(self.logic_wrapper.get_player_by_ID(player_ID),int) :
                            print("Incorrect ID")
                        else:
                            playerinfo = self.logic_wrapper.get_player_by_ID(player_ID)
                            if isinstance(playerinfo, Player):
                                print(f"name: {playerinfo.name}") 
                                print(f"KT: {playerinfo.id}")
                                print(f"dob: {playerinfo.dob}")
                                print(f"phone: {playerinfo.phone}")
                                print(f"address: {playerinfo.address}")
                                print(f"email: {playerinfo.email}")
                case "5": 
                    pass # view statistics team
                case "b": 
                    return
        





#----------------------- Veiw Team ----------------------------




    def view_team_menu(self):
        while True:
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
                    teamID = self.logic_wrapper.get_teams()
                    for team in teamID:
                        print(team.name)

                case "2": 
                    tournaments = self.logic_wrapper.get_tournaments()
                    for i in tournaments:
                        tournament=self.logic_wrapper.get_tournament_by_ID(i.id) # type: ignore
                        if type(tournament) == Tournament:
                            print(f"Tournament: {tournament.name}\n")
                            for teamID in tournament.team_list:
                                team = self.logic_wrapper.get_team_by_ID(teamID)
                                if type(team) == Team:
                                    print(f"Team: {team.name}\n")

                case "3": 
                    pass
                case "4": 
                    pass
                case "5":
                    while True:
                        team_ID = int(input("Enter team ID: "))
                        if self.logic_wrapper.get_team_by_ID(team_ID) is False:
                            print("Incorrect ID")
                        else:
                            team = self.logic_wrapper.get_team_by_ID(team_ID)
                            if type(team) == Team:
                                print(f"name: {team.name}")
                                print(f"tag: {team.tag}")
                                print(f"creator_id: {team.creator_id}")
                                print(f"team_size: {team.team_size}")
                                print(f"member_list: {team.member_list}")

                case "b": 
                    return
            return
    




#-----------------------Veiw Tournament ----------------------------




    def view_tournaments_menu(self):

        while True:
            print(
""" 
View Tournament menu

1. View All tournaments
2. View Visual Tournament Tree
3. View Visual match results
4. View Statistics
b. Back


""")
            choice=input("Enter input: ")
            if choice not in ["1","2","3","4","b","B"]:
                
                print(
""" 
Invalid Input!!

View Team menu

1. View All tournaments
2. View Visual Tournament Tree
3. View Visual match results
4. View Statistics
b. Back

Try again!!
""")

            match choice:
                case "1": 
                    list_of_tournaments=self.logic_wrapper.get_tournaments()
                    for id in list_of_tournaments:
                        tournament=self.logic_wrapper.get_tournament_by_ID(id.id)
                        if isinstance(tournament, Tournament):
                            print(tournament.name)
                case "2": 
                    pass # c Requirement
                case "3": 
                    pass 
                case "4": 
                    pass
                case "b": 
                    return
                




    #-----------------------Veiw Clubs ----------------------------     




    def view_clubs(self):

        while True:
            print(
""" 
View Clubs Menu

1. View All Clubs
2. View Club by ID
3. View Statistics
b. Back


""")
            choice=input("Enter input: ")
            if choice not in ["1","2","3","b","B"]:
                
                print(
""" 
Invalid Input!!

View Clubs Menu

1. View All Clubs
2. View Club by ID
3. View Statistics
b. Back

Try again!!
""")

            match choice:
                case "1": 
                    list_of_clubs=self.logic_wrapper.get_clubs()
                    for clubID in list_of_clubs:
                        club= self.logic_wrapper.get_club_by_ID(clubID.id)
                        if isinstance(club, Club):
                            print(club.name)
                case "2": 
                    while True:
                        int(input("Enter club ID: "))
                    self.logic_wrapper.get_club_by_ID()
                case "3": 
                    pass
                case "b": 
                    return
                





                
        
#-----------------------Veiw Organizer ----------------------------
    def view_organizers(self):
        print(
""" 
View All Organizers Menu

1. View All Organizers
b. Back


""")
        while True:
            choice=input("Enter input: ")
            if choice not in ["1","b","B"]:
                
                print(
""" 
Invalid Input!!

View All Organizers Menu

1. View All Organizers
b. Back

Try again!!
""")

            match choice:
                case "1": 
                    list_of_organizer=self.logic_wrapper.get_Organizer() # type: ignore
                    for organizerID in list_of_organizer:
                        organizer=self.logic_wrapper.get_organizer_by_ID(organizerID) # type: ignore
                        #if type(organizer) == Organizer:
                        #   #print(organizer.name)
                    pass
                case "b": 
                    return
    #----------------------- Veiw Scoreboard ----------------------------     
    def view_scoreboard(self):
        print(
""" 
View Clubs Menu

1. View All Tournaments
b. Back


""")
        while True:
            choice=input("Enter input: ")
            if choice not in ["1","b","B"]:
                
                print(
""" 
Invalid Input!!

View Clubs Menu

1. View All Tournaments
b. Back

Try again!!
""")

            match choice:
                case "1": 
                    tournaments=self.logic_wrapper.get_tournaments()
                    for tour in tournaments:
                        tournamentinfo= self.logic_wrapper.get_tournament_by_ID(tour.id)
                        if isinstance(tournamentinfo,Tournament):
                            print(tournamentinfo.name)
                    
                case "b": 
                    return
            
    #--------------Functions-------------------
    #     