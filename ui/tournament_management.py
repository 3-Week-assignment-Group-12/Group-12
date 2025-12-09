from __future__ import annotations
from re import Match
# ui_layer/main_menu.py
from logic.logic_wrapper import LogicWrapper


from models.tournament import Tournament

from ui.function_file import functionFile



class TournamentManagement():
    def __init__(self,low : LogicWrapper,functionFile:functionFile) -> None:
        self.logic_wrapper = low
        self.functionFile = functionFile
        

    #--------------Menus--------------------





    #--------------Tournament Management Menu--------------------






    def tournament_management_menu(self):
        
        
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
            choice=input("Enter input: ")
            
                
                
            
            match choice:
                case "1": 
                    name = input("Name of Tournament: ")
                    startDate = input("Start date: ")
                    endDate = input("End date: ")
                    venue=input("Location of Tournament: ")
                    contactID = self.functionFile.check_for_tournament_ID()
                    contactEmail = input("Contact Email: ")
                    contactPhone = input("Contact Phone: ")

                                       
                    team_list:list[int] = []
                    choice = input("add teams? (y/n): ").lower()
                    
                    if choice == "y":
                        existing_teams = self.logic_wrapper.get_teams()
                        while True:
                            
                            val = input("Enter team id (q to stop): ")
                            if val.lower() == "q":
                                break
                            
                            for x in existing_teams:
                                if val == str(x.id) and x.id not in team_list:
                                    team_list.append(int(val))
                                    continue
                                
                            print("team id not registered")
                            print()
                    
                    matches:list[int] = []
                    choice = input("add matches? (y/n): ").lower()
                    
                    if choice == "y":
                        existing_matches = self.logic_wrapper.get_match()
                        while True:
                            
                            val = input("Enter match id (q to stop): ")
                            if val.lower() == "q":
                                break
                            
                            for x in existing_matches:
                                if val == str(x.id) and x.id not in matches:
                                    matches.append(int(val))
                                    continue
                                
                            print("match id not registered")
                            print()
                    
                    
                    
                    ret =self.logic_wrapper.create_tournament(name,startDate,endDate,venue,contactID,contactEmail,contactPhone,team_list,matches)
                    if ret == 1:
                        print("Tournament created successfully!")
                    elif ret == -1:
                        print("Error creating tournament!")
                    elif ret == -2:
                        print("Validation failed, tournament not created!")
                    
                case "2": 
                    ID = self.logic_wrapper.inputTournamentID()
                    self.edit_tournament_menu(ID)
                case "3": 
                    ID = self.logic_wrapper.inputTournamentID()
                    if isinstance(ID,str):
                        x = input("Are you sure? (Y/N): ").upper()
                        if x == "y" or x == "Y":
                            self.logic_wrapper.delete_tournament(int(ID))
                        return
                case "4": 
                    ID = self.logic_wrapper.inputTournamentID()
                    self.select_tournament_menu(ID)
                case "b": 
                    return
                case _:
                    print("Invalid input")





    #--------------Edit Tournament Menu--------------------





    def edit_tournament_menu(self,tournamentID):
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
            
        temp : Tournament|bool = self.logic_wrapper.get_tournament_by_ID(tournamentID)   
        while True:
            choice=input("Enter input: ")
            if choice not in ["1","2","3","4","5","6","7","b","B"]:

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
            if isinstance(temp, bool):
                print("Tournament not found")
                return
            cancel_flag = False
            match choice:
                case "1": 
                    temp_name = self.functionFile.input_name()
                    for x in self.logic_wrapper.get_tournaments():
                        if temp_name == x.name:
                            print("name is the same as existing tournament")
                            cancel_flag = True
                case "2": 
                    temp.start_date = input("Enter New Start Date(q to cancel): ")
                    if temp.start_date.lower() == "q":
                        cancel_flag = True
                case "3": 
                    temp.end_date = input("Enter New End date(q to cancel): ")
                    if temp.end_date.lower() == "q":
                        cancel_flag = True
                case "4": 
                    temp.venue_name = input("Enter New venue(q to cancel): ")
                    if temp.venue_name.lower() == "q":
                        cancel_flag = True
                case "5": 
                    temp.contact_id = input("Enter New Contact ID(q to cancel): ")
                    if temp.contact_id.lower() == "q":
                        cancel_flag = True
                case "6": 
                    temp.contact_email = input("Enter New Contact Email(q to cancel): ")
                    if temp.contact_email.lower() == "q":
                        cancel_flag = True
                case "7": 
                    temp.contact_phone = input("Enter New Contact Phone Number(q to cancel): ")
                    if temp.contact_phone.lower() == "q":
                        cancel_flag = True
                case "8": 
                    print("Alert! existing teams will be cleared")
                    new_teams: list[int] = []
                    existing_teams = self.logic_wrapper.get_teams()
                    while True:
                        
                        val = input("Enter team id (q to stop): ")
                        if val.lower() == "q":
                            cancel_flag =True
                            break
                        
                        for x in existing_teams:
                            if val == str(x.id) and x.id not in new_teams:
                                new_teams.append(int(val))
                                continue
                            
                        print("team id not registered")
                        print()
                    temp.team_list = new_teams
                case "9": 
                    print("Alert! existing matches will be cleared")
                    new_matches: list[int] = []
                    
                    existing_matches = self.logic_wrapper.get_match()
                    while True:
                        
                        val = input("Enter match id (q to stop): ")
                        if val.lower() == "q":
                            cancel_flag = True
                            break
                        
                        for x in existing_matches:
                            if val == str(x.id) and x.id not in new_matches:
                                new_matches.append(int(val))
                                continue
                            
                        print("match id not registered")
                        print()
                    temp.matches = new_matches
                    
                case "b": 
                    pass
            
            if cancel_flag == False:
                self.logic_wrapper.modify_tournament(temp)
          

          


    #--------------Select Tournement Menu--------------------





    def select_tournament_menu(self, ID):

        while True:
            print(
f""" 
Selected: "{self.logic_wrapper.get_tournament_by_ID(ID) := result; result.name if isinstance(result, Tournament)}"

1. Generate Schedule
2. Record Game Results
3. Accept Teams
4. Manage Rewards
5. Retrieve Records
b. Back 


""")
            choice=input("Enter input: ")
            if choice not in ["1","2","3","4","5","b","B"]:

                print(
f""" 
Invalid Input!!

Select {self.logic_wrapper.get_tournament_by_ID(ID) := result; result.name if isinstance(result, Tournament)}

1. Generate Schedule
2. Record Game Results
3. Accept Teams
4. Manage Rewards
5. Retrieve Records
b. Back 

Try again!!
""")

            match choice:
                case "1": 
                    self.logic_wrapper.generate_bracket(ID)
                case "2": 
                    team1_id = self.logic_wrapper.inputTeamID()
                    team2_id = self.logic_wrapper.inputTeamID()
                    if team1_id == team2_id:
                        print("Teams cannot be the same")
                        continue
                    
                    tournament_id = self.logic_wrapper.inputTournamentID()
                    if not isinstance(tournament_id,str):
                        continue
                    tournament_id = int(tournament_id)
                    
                    date = input("Enter date of match: ")
                    time = input("enter match time: ")
                    server_id = int(input("enter server id: "))
                    winner_id = input("Enter winner id: ")
                    while winner_id != team1_id and winner_id != team2_id:
                        print("Winner must be one of the teams")
                        winner_id = input("Enter winner id: ")
                        
                    score = int(input("Enter score:"))
                    
                    
                    ret =self.logic_wrapper.create_match(team1_id, team2_id, tournament_id, date, time, server_id, winner_id, score)
                    if ret ==-2:
                        print("failure in creating match")
                    
                case "3": 
                    pass
                case "4": 
                    pass
                case "5": 
                    
                    for x in self.logic_wrapper.get_matches_by_tournament_ID(ID):
                        print(x)
                case "b": 
                    pass
            



# ------------------Functions----------------------


