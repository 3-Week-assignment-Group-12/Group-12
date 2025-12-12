from random import randint
from models.bracket import Bracket
from logic.logic_wrapper import LogicWrapper
from models.tournament import Tournament
from models.team import Team
from ui.function_file import functionFile



class TournamentManagement():
    """Menu and operations for managing tournaments.

    This class provides organizer-facing functionality for:

    - Creating, editing, and cancelling tournaments.
    - Selecting a tournament to manage schedules and results.
    - Generating brackets and recording match outcomes.
    """
    def __init__(self,low : LogicWrapper,functionFile:functionFile) -> None:
        """Initialize the TournamentManagement menu.

        Args:
            low (LogicWrapper):
                Logic wrapper responsible for business logic and data access.
            functionFile (functionFile):
                Helper object for reusable input and utility functions.
        """
        self.logic_wrapper = low
        self.functionFile = functionFile
        

    #--------------Menus--------------------





    #--------------Tournament Management Menu--------------------






    def tournament_management_menu(self) -> None:
        """Display and handle the top-level Tournament Management menu.

        Options:
            1 -> Create Tournament
            2 -> Edit Tournament information
            3 -> Cancel Tournament
            4 -> Select Tournament
            b -> Back

        The loop continues until the user chooses 'b' / 'B'.
        """
        while True:
            print(
""" 

Tournament Management 

1. Create Tournament
2. Edit Tournament information 
3. Cancel Tournament
4. Select Tournament
b. Back 


""")
            choice = input("Enter input (q to stop): ")
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
                continue
                
            match choice:
                case "1": 
                    name = self.functionFile.input_tournament_name()
                    if name == False:
                        continue

                    startDate = self.functionFile.input_start_date()
                    if startDate == False:
                        continue

                    endDate = self.functionFile.input_end_date(startDate)
                    if endDate == False:
                        continue

                    venue = input("Location of Tournament (q to stop): ")
                    if venue == "q":
                        continue

                    contactID = self.functionFile.input_contact_ID()
                    if contactID == False:
                        continue

                    contactEmail = self.functionFile.input_contact_email()
                    if contactEmail == False:
                        continue

                    contactPhone = self.functionFile.input_contact_phone_nr()
                    if contactPhone == False:
                        continue
                             
                    team_list:list[int] = []
                    choice = input("Add teams? (y/n, q to stop): ").lower()
                    
                    if choice == "y":
                        existing_teams = self.logic_wrapper.get_teams()
                        counter = 0

                        while True:
                            print(f"current teams in tournament: {counter}")
                            val = input("Enter team id (q to stop): ")

                            if val.lower() == "q":
                                break
                            found = False
                            for x in existing_teams:
                                if val == str(x.id):
                                    if x.id not in team_list:
                                        team_list.append(x.id)
                                        counter += 1

                                    found = True
                                    break

                            if not found:
                                print("team id not registered")

                            else:
                                print(f"team id {val} added.")

                                print(team_list)
                                print()
                    
                    matches:list[int] = []
                    choice = input("add matches? (y/n, q to stop): ").lower()
                    if choice == "y":
                        existing_matches = self.logic_wrapper.get_match()
                        while True:
                            
                            val = input("Enter match id (q to stop): ")
                            if val.lower() == "q":
                                break
                            
                            for x in existing_matches:
                                if val == str(x.id) and x.id not in matches:
                                    matches.append(int(val))
                                    print("match has been added")
                                else:
                                    print("match id already exists")
                                
                            
                            print()

                    barches:list[list[int]] = []
                    barches.append(matches)
                        
                    
                    ret = self.logic_wrapper.create_tournament(name,startDate,endDate,venue,contactID,contactEmail,contactPhone,team_list,barches)
                    if ret == 1:
                        print("Tournament created successfully!")

                    elif ret == -1:
                        print("Error creating tournament!")

                    elif ret == -2:
                        print("Validation failed, tournament not created!")
                    
                case "2": 
                    ID = self.functionFile.inputTournamentID()
                    if ID is None:
                        continue

                    self.edit_tournament_menu(ID)

                case "3": 
                    ID = self.functionFile.inputTournamentID()
                    if ID is None:
                        continue

                    x = input("Are you sure? (Y/N) (q to stop): ").lower()
                    if x == "y":
                        self.logic_wrapper.delete_tournament(int(ID))
                        print("Tournament has been canceled!")

                    elif x == "n":
                        print("Tournament deletion aborted!")

                    continue

                case "4": 
                    ID = self.functionFile.inputTournamentID()
                    if ID is None:
                        continue

                    self.select_tournament_menu(ID)

                case "b": 
                    return
                
                case _:
                    print("Invalid input")





    #--------------Edit Tournament Menu--------------------





    def edit_tournament_menu(self,tournamentID: int | str) -> None:
        """Display and handle the Edit Tournament menu for a specific tournament.

        Provides editing of:
            - Name
            - Start / end date
            - Venue
            - Contact information
            - Team list (rebuild)
            - Match list (append new match bundle)

        Args:
            tournamentID (int | str):
                Tournament ID to edit. If a string is provided, it is
                converted to int where possible.
        """
        if isinstance(tournamentID, str):
            try:
                tournamentID = int(tournamentID)
            except ValueError:
                print("Invalid tournament ID")
                return

  
        temp: Tournament | bool = self.logic_wrapper.get_tournament_by_ID(tournamentID)
        if not isinstance(temp, Tournament):
            print("Tournament not found")
            return

        while True:
            print(
""" 
Edit Tournament Information

1. Name Of Tournament
2. Start Date 
3. End Date
4. Venue name
5. Contact ID
6. Contact Email
7. Contact Phone
8. Team list
9. Match list
b. Back 


""")
            choice = input("Enter input (q to stop): ")
            if choice not in ["1","2","3","4","5","6","7","8","9","b","B"]:

                 print(
""" 
Invalid Input!!

Edit Tournament Information

1. Name Of Tournament
2. Start Date 
3. End Date
4. Venue name
5. Contact ID
6. Contact Email
7. Contact Phone
8. Team List
9. Match list
b. Back 

Try again!!
""")
                 continue
            
            cancel_flag = False

            match choice:
                case "1": 
                    new_name = self.functionFile.input_name()
                    for t in self.logic_wrapper.get_tournaments():
                        if t.id != temp.id and t.name == new_name:
                            print("A tournament with this name already exists.")
                            cancel_flag = True
                            break

                    if not cancel_flag and isinstance(new_name,str):
                        temp.name = new_name

                case "2": 
                    new_start = self.functionFile.input_start_date()
                    if new_start == False:
                        cancel_flag = True

                    else:
                        temp.start_date = new_start

                case "3": 
                    tournament = self.logic_wrapper.get_tournament_by_ID(tournamentID)
                    if isinstance(tournament,Tournament):
                        new_end = self.functionFile.input_end_date(tournament.start_date)
                        if new_end == False:
                            cancel_flag = True

                        else:
                            temp.end_date = new_end

                case "4": 
                    new_venue = input("Enter New venue name (q to cancel): ")
                    if new_venue.lower() == "q":
                        cancel_flag = True

                    else:
                        temp.venue_name = new_venue

                case "5": 
                    new_contact_id = self.functionFile.input_creatorID()
                    if new_contact_id == False:
                        cancel_flag = True

                    else:
                        temp.contact_id = new_contact_id

                case "6": 
                    new_email = self.functionFile.input_email()
                    if new_email == False:
                        cancel_flag = True

                    else:
                        temp.contact_email = new_email

                case "7": 
                    new_phone = self.functionFile.input_phone_nr()
                    if new_phone == False:
                        cancel_flag = True

                    else:
                        temp.contact_phone = new_phone

                case "8": 
                    print("Alert! existing teams will be cleared")
                    new_teams: list[int] = []
                    counter = len(new_teams)
                    existing_teams = self.logic_wrapper.get_teams()
                    while True:
                        print(f"Amount of teams in new list: {counter}")
                        val = input("Enter team id (q to stop): ")
                        if val.lower() == "q":
                            break
                        
                        found = False
                        for x in existing_teams:
                            if val == str(x.id):
                                if x.id not in new_teams:
                                    new_teams.append(x.id)
                                    counter += 1

                                found = True
                                break

                        if not found:
                            print("team id not registered")

                        else:
                            print(f"team id {val} added.")

                    temp.team_list = new_teams

                case "9": 
                    print("Alert! existing matches will be cleared")
                    new_matches: list[int] = []
                    
                    existing_matches = self.logic_wrapper.get_match()
                    while True:
                        if new_matches.__len__() == temp.team_list.__len__()/2:
                            print("max amount of matches added, ending")
                            break

                        val = input("Enter match id (q to stop): ")
                        if val.lower() == "q":
                            break
                        
                        found = False
                        for x in existing_matches:
                            if val == str(x.id):
                                if x.id not in new_matches:
                                    new_matches.append(x.id)

                                found = True
                                break

                        if not found:
                            print("match id not registered")

                        else:
                            print(f"match id {val} added.")

                    temp.matches.append(new_matches)
                    
                case "b": 
                    return
            
            if not cancel_flag:
                self.logic_wrapper.modify_tournament(temp)
                print("Tournament has been modified!")
          

          


    #--------------Select Tournement Menu--------------------





    def select_tournament_menu(self, ID:int) -> None:
        """Display and handle the menu for a selected tournament.

        Allows:
            - Generating and recording bracket-based schedules.
            - Recording custom game results.
            - Viewing existing match records.

        Args:
            ID (int): Tournament ID to select.
        """
        tourn = self.logic_wrapper.get_tournament_by_ID(ID)
        if isinstance(tourn, bool):
            print("error fetching team")
            return

        while True:
            print(
f""" 
Selected: "{tourn.name}"

1. Generate Schedule
2. Record Game Results
3. Retrieve Records
b. Back 


""")
            choice = input("Enter input (q to stop): ")
            if choice not in ["1","2","3","b","B"]:

                print(
f""" 
Invalid Input!!

Select {tourn.name}

1. Generate Schedule
2. Record Game Results
3. Retrieve Records
b. Back 

Try again!!
""")

            match choice:
                case "1": 
                      
                    bracket = self.logic_wrapper.generate_bracket(tourn)
                    
                    if bracket == 2:
                        print("Bracket is compleate")
                    
                    if isinstance(bracket, Bracket):
                        print(bracket.matchups)
                        

                        inp = input("bracket generated, use? (y/n, q to stop): ")

                            
                        if inp.lower() == "y":
                            self.logic_wrapper.data_wrapper.write_bracket(bracket)
                            
                            inp2 = input("enter Results now? (y/n, q to stop): ")
                            if inp2.lower() == "y":
                                match_bundle = []
                                for matchup in bracket.matchups:
                                    while True:
                                        
                                        team1 = self.logic_wrapper.get_team_by_ID(matchup[0])
                                        team2 = self.logic_wrapper.get_team_by_ID(matchup[1])
                                        if isinstance(team1,Team) and isinstance(team2,Team):
                                            print(f"Team{team1.id} vs Team{team2.id}")
                                            print(f"{team1.name} vs {team2.name}")
                                            print()

                                        else:
                                            print("error getting team names")
                                            print(f"Team numbers: team1: {matchup[0]} vs team2: {matchup[1]}")
                                        
                                        date = tourn.start_date
                                        time = self.functionFile.input_match_time()
                                        if isinstance(time, bool):
                                            break
                                        server_id = randint(1,10)
                                        winner_id = self.functionFile.winner()
                                        while winner_id != matchup[0] and winner_id != matchup[1]:
                                            print(f"Winner must be one ether: {matchup[0]} or {matchup[1]}")
                                            winner_id = self.functionFile.winner()
                                            
                                            self.functionFile.add_data_to_team_int(winner_id,"wins",1)
                                            loser = [matchup[0],matchup[1]]
                                            loser.remove(winner_id)
                                            self.functionFile.add_data_to_team_int(loser[0],"losses",1)
                                        
                                   
                                        score = self.functionFile.score()
                                        
                                        self.functionFile.add_data_to_team_int(winner_id,"total score",score)
                                        
                                        
                                        ret = self.logic_wrapper.create_match(matchup[0], matchup[1], tourn.id, date, time, server_id, winner_id, score)
                                        if ret == -2:
                                            print("failure in creating match")
                                            print("try againe")
                                            continue

                                        if ret >= 0:
                                            print("sucsess in creating match")
                                            
                                            print()
                                            
                                            match_bundle.append(ret)
                                            break

                                tourn.matches.append(match_bundle)
                                
                                if tourn.matches[-1].__len__() == 1:
                                    print("Schedule completed")
                                    
                                    tourn.matches.append([])
                                    
                                self.logic_wrapper.modify_tournament(tourn)
                                continue
                                    
                    else:
                        match bracket:
                            case -1:
                                print("not enough teams")

                            case -2:
                                print("odd number of teams")

                            case -3:
                                print("error in generating bracket")
                                
                case "2": 
                    print("team 1 ")
                    team1_id = self.functionFile.checkTeamID()
                    if team1_id == False:
                        continue

                    print("team 2 ")
                    team2_id = self.functionFile.checkTeamID()
                    if team2_id == False:
                        continue

                    if team1_id == team2_id:
                        print("Teams cannot be the same")
                        continue
        
                    date = self.functionFile.input_start_date()
                    if date == False:
                        continue

                    time = self.functionFile.input_match_time()
                    if time == False:
                        continue

                    server_id = randint(1,10)
                    winner_id = self.functionFile.winner()
                    while winner_id != team1_id and winner_id != team2_id:
                        print("Winner must be one of the teams")
                        winner_id = self.functionFile.winner()
                        
                    score = self.functionFile.score()
                    
                    
                    ret = self.logic_wrapper.create_match(team1_id, team2_id, tourn.id, date, time, server_id, winner_id, score)
                    if ret == -2:
                        print("failure in creating match")

                    if ret >= 0:
                        print("creating match sucsessful")
                        
                        tourn.matches[-1].append(ret)
                        self.logic_wrapper.modify_tournament(tourn)

                case "3": 
                    
                    for x in self.logic_wrapper.get_matches_by_tournament_ID(ID):
                        print(f"Match: {x.id}")
                        print(f"Team{x.team1_id} VS Team{x.team2_id}")
                        print(f"Winner Team: {x.winner_id}, Score: {x.Score}")
                        print(f"Date: {x.date}, match time: {x.match_time}, server id: {x.server_id}")
                        print()
                        
                case "b": 
                    return
            
