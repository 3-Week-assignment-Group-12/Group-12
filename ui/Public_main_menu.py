from __future__ import annotations
# ui_layer/main_menu.py
from logic.logic_wrapper import LogicWrapper
from models.team import Team
from models.tournament import Tournament

from models.player import Player
from ui.Organizer_menu import OrganizerMenu
from ui.tournament_management import TournamentManagement



class PublicMainMenu():

    def __init__(self,low : LogicWrapper) -> None:
        self.logic_wrapper = low
        pass

    
    def public_menu(self):
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
        while True:
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
                    pass
           
    


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
        while True:
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
                    for i in list_of_players:
                        print(i.name)
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
                    player_ID = int(input("Enter player ID: "))
                    x = self.logic_wrapper.get_player_by_ID(player_ID)
                    print(f"name: {x.name}") 
                    print(f"KT: {x.kt}")
                    print(f"dob: {x.dob}")
                    print(f"phone: {x.phone}")
                    print(f"address: {x.address}")
                    print(f"email: {x.email}")
                case "5": 
                    pass # view statistics team
                case "b": 
                    pass
        

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
                teams = self.logic_wrapper.get_teams()
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
View Tournament menu

1. View All tournaments
2. View Visual Tournament Tree
3. View Visual match results
4. View Statistics
b. Back


""")
        while True:
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
                    pass
                case "2": 
                    pass
                case "3": 
                    pass
                case "4": 
                    pass
                case "b": 
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
        while True:
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
                    pass
                case "2": 
                    pass
                case "3": 
                    pass
                case "b": 
                    pass
        

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
                    pass
                case "b": 
                    pass
            
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
                    pass
                case "b": 
                    pass
            
        
    