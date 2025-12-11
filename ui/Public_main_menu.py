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
    """Public-facing menu for viewing tournament-related data.

    This class contains read-only menus for:
        - Viewing players and their statistics.
        - Viewing teams and team-related statistics.
        - Viewing tournaments, schedules, and derived statistics.
        - Viewing clubs and aggregated statistics by club.
        - Viewing organizers and basic scoreboard info.
    """
    def __init__(self,low : LogicWrapper,functionFile:functionFile) -> None:
        """Initialize PublicMainMenu with shared dependencies.

        Args:
            low (LogicWrapper):
                Shared logic layer facade used for data retrieval and
                higher-level operations.
            functionFile (functionFile):
                Helper instance containing input utilities and statistics helpers.
        """
        self.logic_wrapper = low
        self.functionFile = functionFile

    #-----------------------Public Main menu----------------------------
    def public_menu(self) -> None:
        """Display the public main menu and route to sub-menus.

        Options:
            1 -> View Players
            2 -> View Teams
            3 -> View Tournaments
            4 -> View Clubs
            5 -> View Scoreboard (partially implemented)
            6 -> View Organizers (partially implemented)
            b -> Back

        The method loops until the user chooses 'b' / 'B'.
        """
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




    def view_players_menu(self)-> None:
        """Display the View Players menu and handle user actions.

        Options:
            1 -> View all players (basic info)
            2 -> View players grouped by team (incl. dynamic_data)
            3 -> View players grouped by tournament
            4 -> View a specific player's basic info
            5 -> View statistics for all players (dynamic_data)
            6 -> View statistics for a single player (dynamic_data)
            b -> Back

        Uses LogicWrapper to fetch players, teams, and tournaments,
        and prints information directly to the console.
        """
        while True:
            print(
""" 
View Players menu

1. View All Players
2. View Player In Teams
3. View PLayers In Tournaments
4. View Specific Players
5. View Statistics for all players
6. view Statistics for one player
b. Back


""")
            choice=input("Enter input: ")
            if choice not in ["1","2","3","4","5","6","b","B"]:
                
                print(
""" 
Invalid Input!!

View Players menu

1. View All Players
2. View Player In Teams
3. View PLayers In Tournaments
4. View Specific Players
5. View Statistics for all players
6. view Statistics for one player
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
                            count = 1
                            for pl in team.member_list:
                                player = self.logic_wrapper.get_player_by_ID(pl)
                                if type(player) == Player:
                                    
                                    print(f"{count}: {player.name}, ID: {player.id}")
                                    for key in player.dynamic_data.keys():
                                        print(f"{key}: {player.dynamic_data[key]}")
                                    count +=1
                            print("")
                            print("")
                                    
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
                                    print("")
                                    print("")
                                            
                case "4":
                    while True:
                        player_ID = input("Enter player ID: ")
                        if player_ID == "q":
                            return
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
                    list_of_players=self.logic_wrapper.get_players() #view all players
                    count = 1
                    for i in list_of_players:
                        print()
                        print(f"{count}: {i.name}, Handle: {i.handle}, ID: {i.id}")
                        count +=1
                        for key in i.dynamic_data.keys():
                            print(f"\t{key}: {i.dynamic_data[key]}")
                
                case "6":
                    ide = self.functionFile.check_excistingID()
                    if isinstance(ide,str):
                        play = self.logic_wrapper.get_player_by_ID(ide)
                        if isinstance(play,Player):
                            print(f"Name: {play.name}, Handle: {play.handle}")
                            for key in play.dynamic_data.keys():
                                    print(f"\t{key}: {play.dynamic_data[key]}")
                    
                            
                case "b": 
                    return
        





#----------------------- Veiw Team ----------------------------




    def view_team_menu(self) -> None:
        """Display the View Team menu and handle user actions.

        Options:
            1 -> View all teams
            2 -> View teams grouped by tournaments
            3 -> View visual tournaments (not implemented)
            4 -> View team statistics (aggregated dynamic_data)
            5 -> View specific team details
            b -> Back
        """
        while True:
            print(
""" 
View Team menu

1. View All Teams
2. View Teams In Tournament
3. View Visual Team Tournaments [not implamanted]
4. View Statistics of team
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
                            counter = 1
                            for teamID in tournament.team_list:
                                team = self.logic_wrapper.get_team_by_ID(teamID)
                                if type(team) == Team:
                                    print(f"Team {counter}: {team.name}\n")
                                    counter += 1

                case "3": 
                    pass
                case "4": 
                    ID = self.functionFile.checkTeamID()
                    data = self.functionFile.get_data_from_team(ID)
                    print(f"Displaying total data for team {ID}")
                    if isinstance(data,dict):
                        for key in data.keys():
                            print(f"{key}: {data[key]}")
                
                
                
                case "5":
                    while True:
                        team_ID = input("Enter team ID: ")
                        if team_ID == "q":
                            return False
                        try:
                            team_ID = int(team_ID)
                            if self.logic_wrapper.get_team_by_ID(team_ID) is False:
                                print("Incorrect ID, try again!")
                            else:
                                team = self.logic_wrapper.get_team_by_ID(team_ID)
                                if type(team) == Team:
                                    print(f"name: {team.name}")
                                    print(f"tag: {team.tag}")
                                    print(f"creator_id: {team.creator_id}")
                                    print(f"team_size: {team.team_size}")
                                    print(f"member_list: {team.member_list}")
                        except:
                            print("Team ID can only contain digits!")

                case "b": 
                    return
            return
    




#-----------------------Veiw Tournament ----------------------------




    def view_tournaments_menu(self) -> None:
        """Display the View Tournament menu and handle user actions.

        Options:
            1 -> View all tournaments
            2 -> View visual tournament tree (not implemented)
            3 -> View visual match results (not implemented)
            4 -> View tournament-wide statistics (aggregated dynamic_data)
            5 -> View teams in a tournament
            6 -> View schedule in a tournament
            b -> Back
        """
        while True:
            print(
""" 
View Tournament menu

1. View All tournaments
2. View Visual Tournament Tree [not implamanted]
3. View Visual match results [not implamanted]
4. View Statistics for tournament
5. View teams in tournaemnt
6. View schedule in tournaemnt
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
4. View Statistics for tournaemnt
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
                    
                    tour_id = self.functionFile.inputTournamentID()
                    if isinstance(tour_id,int):
                        tour = self.logic_wrapper.get_tournament_by_ID(tour_id)
                        if isinstance(tour,Tournament):
                            big_total: dict[str,int] = {}
                            
                            teams = self.logic_wrapper.get_team_by_tournament_id(tour.id)
                            if isinstance(teams,bool):
                                print("data not found")
                                continue
                            
                            for team in teams:
                                data = self.functionFile.get_data_from_team(team.id)
                                print()
                                print(f"Displaying total data for team {team.name}")
                                if isinstance(data,dict):
                                    
                                    for key in data.keys():
                                        print(f"{key}: {data[key]}")
                                        try:
                                            big_total[key] += data[key]
                                        except:
                                            big_total[key] = 0
                                            big_total[key] += data[key]
                            
                            print()
                            print("Total data in tournament:")
                            for key in big_total.keys():
                                print(f"{key}: {big_total[key]}")
                    
                    
                    
                    
                case "5":
                    tournamentID=self.functionFile.inputTournamentID()
                    if tournamentID==None:
                        continue
                    team_list:list[Team]| bool = self.logic_wrapper.get_team_by_tournament_id(tournamentID)
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
                    tournamentID=self.functionFile.inputTournamentID()
                    if tournamentID==None:
                        continue
                    tour = self.logic_wrapper.get_tournament_by_ID(tournamentID)
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




    def view_clubs(self) -> bool | None:
        """Display the View Clubs menu and handle user actions.

        Options:
            1 -> View all clubs
            2 -> View club by ID
            3 -> View aggregated statistics per club (dynamic_data)
            b -> Back

        Returns:
            bool | None:
                False when the user cancels an inner prompt with 'q',
                otherwise None when returning normally.
        """
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
                        clubID = input("Enter club ID: ")
                        if clubID == "q":
                            return False
                        try:
                            clubID = int(clubID)
                            if self.logic_wrapper.get_club_by_ID(clubID) is False:
                                print("Incorrect ID, try again!")
                            else:
                                club = self.logic_wrapper.get_club_by_ID(clubID)
                                if type(club) == Club:
                                    print(f"Club ID: {club.id}")
                                    print(f"Club name: {club.name}")
                                    print(f"Club colour: {club.colours}")
                        except:
                            print("Club ID must contain only digits!")
                case "3": 
                    
                    club_id = self.functionFile.inputClubID()
                    if isinstance(club_id,int):
                        tour = self.logic_wrapper.get_club_by_ID(club_id)
                        if isinstance(tour,Club):
                            big_total: dict[str,int] = {}
                            
                            teams = self.logic_wrapper.get_team_by_club_id(tour.id)
                            if isinstance(teams,bool):
                                print("data not found")
                                continue
                            
                            for team in teams:
                                data = self.functionFile.get_data_from_team(team.id)
                                print()
                                print(f"Displaying total data for team {team.name}")
                                if isinstance(data,dict):
                                    
                                    for key in data.keys():
                                        print(f"{key}: {data[key]}")
                                        try:
                                            big_total[key] += data[key]
                                        except:
                                            big_total[key] = 0
                                            big_total[key] += data[key]
                            
                            print()
                            print("Total data in club:")
                            for key in big_total.keys():
                                print(f"{key}: {big_total[key]}")
                    
                    
                    
                case "b": 
                    return
                





                
        
#-----------------------Veiw Organizer ----------------------------
    def view_organizers(self):
        """Display organizer contact information.

        Options:
            1 -> View all organizers (from tournaments contact info)
            2 -> View a specific organizer by contact ID
            b -> Back

        Organizers are implicitly modeled via Tournament.contact_* fields.
        """
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
                    if contactID == False:
                        return
                    tournaments=self.logic_wrapper.get_tournaments()
                    for tournament in tournaments:
                        if tournament.contact_id==contactID:
                            print(f"Email:{tournament.contact_email}, Phone:{tournament.contact_phone}, National ID:{tournament.contact_id}")
                case "b": 
                    return
    #----------------------- Veiw Scoreboard ----------------------------     
    def view_scoreboard(self):
        """Display basic scoreboard-related menu.

        Options:
            1 -> View all tournaments (as a simple list)
            b -> Back

        Note:
            Functionality is marked as 'not fully implemented'.
        """
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