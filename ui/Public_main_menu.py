from __future__ import annotations
from re import Match
from xmlrpc.client import Boolean
# ui_layer/main_menu.py
from models.bracket import Bracket
from models.club import Club
from logic.logic_wrapper import LogicWrapper
from models.team import Team
from models.tournament import Tournament
from models.player import Player
from models.tournament import Tournament
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
5. View Scoreboard [not fully implamanted]
6. View Organizers [not implamanted]
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
3. View Visual Team Tournaments [not implamanted]
4. View Statistics [not implamanted]
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
2. View Visual Tournament Tree [not implamanted]
3. View Visual match results [not implamanted]
4. View Statistics
5. View teams in tournament
6. View tournaemnt schedule
b. Back


""")
            choice=input("Enter input: ")
            if choice not in ["1","2","3","4","5","6","b","B"]:
                
                print(
""" 
Invalid Input!!

View Tournament menu

1. View All tournaments
2. View Visual Tournament Tree [not implamanted]
3. View Visual match results [not implamanted]
4. View Statistics
5. View teams in tournaemnt
6. View schedule in tournaemnt
b. Back

Try again!!
""")
                continue

            match choice:
                case "1": 
                    list_of_tournaments=self.logic_wrapper.get_tournaments()
                    if not list_of_tournaments:
                        print("No tournaments found.")
                    else:
                        print("\nAll tournaments:")
                        for t in list_of_tournaments:
                            print(f"  ID {t.id}: {t.name}")
                    input("\nPress Enter to return to this menu...")
                case "2": 
                    pass # c Requirement
                case "3": 
                    pass 
                case "4": 
                    pass
                    
                case "5":
                    team_list:list[Team]| bool = self.logic_wrapper.get_team_by_tournament_id(self.functionFile.inputTournamentID())
                    if isinstance(team_list,bool):
                        print("data not found")
                    else:

                        count =1
                        for x in team_list:
                            print()
                            print(f"Team: {count}: {x.name}, tag: {x.tag}")
                            print(f"Size: {x.team_size}, ID: {x.id}")
                            print("Players:")
                            count1 = 1
                            if x.member_list == []:
                                print("player list is empty")
                            else:
                                for j in x.member_list:
                                    
                                    play = self.logic_wrapper.get_player_by_ID(j)
                                    if isinstance(play,Player):
                                        
                                        print(f"{count1}: {play.name} \"{play.handle}\", {play.id}") # type: ignore handle comes later
                                        count1 +=1
                                    else:
                                        print("player not found")
                            
                                count +=1
                                
                case "6":
                    tour = self.logic_wrapper.get_tournament_by_ID(self.functionFile.inputTournamentID())
                    if isinstance(tour,Tournament):
                        round_count =0
                        for match_bundle in tour.matches:
                            
                            if match_bundle == [] and tour.matches.__len__() >1:

                                winning_match = self.logic_wrapper.get_match_by_ID(tour.matches[tour.matches.__len__()-2][0])
                                if isinstance(winning_match,Boolean):
                                    pass
                                else:
                                    winning_team = self.logic_wrapper.get_team_by_ID(winning_match.winner_id)
                                    if isinstance(winning_team,Team):
                                        print()
                                        print(f"Winner is {winning_team.name}")
                                        continue
                            
                            else:
                                
                                print(f"    Round {round_count+1}:")
                                round_count +=1
                                for match in match_bundle:
                                    mat = self.logic_wrapper.get_match_by_ID(match)
                                    if isinstance(mat,bool):
                                        
                                        print("match not found")
                                        
                                    else:
                                        print()
                                        print(f"Match id: {mat.id}, Team {mat.team1_id} VS Team {mat.team2_id}")
                                        print(f"Winner: {mat.winner_id}, Score: {mat.Score}")
                                        print(f"Date: {mat.date}, Time: {mat.match_time}, ")
                            
                            
                                    
                    

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
3. View Statistics [not implamanted]
b. Back


""")
            choice=input("Enter input: ")
            if choice not in ["1","2","3","b","B"]:
                
                print(
""" 
Invalid Input!!

View Clubs Menu

1. View All Clubs
2. View Club by ID [not fully implamanted]
3. View Statistics [not implamanted]
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
2. View specific Organizer
b. Back


""")
        while True:
            choice=input("Enter input: ")
            if choice not in ["1","2","b","B"]:
                
                print(
""" 
Invalid Input!!

View All Organizers Menu

1. View All Organizers
2. View specific Organizer
b. Back

Try again!!
""")

            match choice.lower():
                case "1": 
                    tournaments=self.logic_wrapper.get_tournaments() 
                    counter=1
                    if tournaments==[]:
                        continue
                    else:
                        for tournament in tournaments:
                            print(f"Organizer:{counter}, Email:{tournament.contact_email}, Phone:{tournament.contact_phone}, National ID:{tournament.contact_id}")
                            counter+=1
                case "2":
                    contactID=self.functionFile.input_contact_ID()
                    tournaments=self.logic_wrapper.get_tournaments()
                    for tournament in tournaments:
                        if tournament.contact_id==contactID:
                            print(f"Email:{tournament.contact_email}, Phone:{tournament.contact_phone}, National ID:{tournament.contact_id}")
                case "b": 
                    return
    #----------------------- Veiw Scoreboard ----------------------------     
    def view_scoreboard(self):
        print(
""" 
View Clubs Menu

1. View All Tournaments [not fully implamanted]
b. Back


""")
        while True:
            choice=input("Enter input: ")
            if choice not in ["1","b","B"]:
                
                print(
""" 
Invalid Input!!

View Clubs Menu

1. View All Tournaments [not fully implamanted]
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