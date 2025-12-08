from __future__ import annotations
# ui_layer/main_menu.py
from logic.logic_wrapper import LogicWrapper


from models.player import Player

from models.tournament import Tournament

from models.team import Team

class TournamentManagement():
    def __init__(self,low : LogicWrapper) -> None:
        self.logic_wrapper = low
        pass

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
                    contactID = self.check_for_tournament_ID()
                    contactEmail = input("Contact Email: ")
                    contactPhone = int(input("Contact Phone: "))
                    team_list=[]  # SKoða þetta
                    matches=[]    # sKoða þetta
                    self.logic_wrapper.create_tournament(name,startDate,endDate,venue,contactID,contactEmail,contactPhone,team_list,matches)
                case "2": 
                    ID = self.inputTournamentID()
                    self.edit_tournament_menu(ID)
                case "3": 
                    ID = self.inputTournamentID()
                    x = input("Are you sure? (Y/N): ")
                    if x == "y" or x == "Y":
                        self.logic_wrapper.delete_tournament(ID)
                    return
                case "4": 
                    ID = self.inputTournamentID()
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
b. Back 

Try again!!
""")
            if isinstance(temp, bool):
                print("Tournament not found")
                return
            match choice:
                case "1": 
                    temp.name = input("Enter New Name: ")
                case "2": 
                    temp.start_date = input("Enter New Start Date: ")
                case "3": 
                    temp.end_date = input("Enter New End date: ")
                case "4": 
                    temp.venue_name = input("Enter New : ")
                case "5": 
                    temp.contact_id = int(input("Enter New Contact ID: "))
                case "6": 
                    temp.contact_email = input("Enter New Contact Email: ")
                case "7": 
                    temp.contact_phone = int(input("Enter New Contact Phone Number: "))
                case "8": 
                    pass
                    #temp.team_list 
                case "9": 
                    pass
                    #temp.matches 
                case "b": 
                    pass
            
            self.logic_wrapper.modify_tournament(temp)
          

          


    #--------------Select Tournement Menu--------------------





    def select_tournament_menu(self, ID):

        while True:
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
            if choice not in ["1","2","3","4","5","b","B"]:

                print(
""" 
Invalid Input!!

Select "nafn liðs"   ATH !!!!

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
                    pass
                case "3": 
                    pass
                case "4": 
                    pass
                case "5": 
                    pass
                case "b": 
                    pass
            



# ------------------Functions----------------------


    def check_for_tournament_ID(self):
        ID = int(input("Contact ID"))
        list_of_tournaments=self.logic_wrapper.get_tournaments()
        while True:
            
            if list_of_tournaments is None or list_of_tournaments == []:
                return ID
            for tournamentID in list_of_tournaments:
                tournament_info=self.logic_wrapper.get_team_by_ID(tournamentID.id)
                if isinstance(tournament_info,Tournament):
                    if ID == tournament_info.id: 
                        print("This tournament ID already exists!")
                        ID = int(input("Enter different Contact ID"))
                    else:
                        return ID
    


    def inputTournamentID(self):
        tournamentID=int(input("Enter Tournament ID: "))
        check= self.logic_wrapper.get_tournament_by_ID(tournamentID)
        while check is False:
            print("Tournament does not exist, Try different ID")
            tournamentID=int(input("Enter Tournament ID: "))
            check= self.logic_wrapper.get_tournament_by_ID(tournamentID)
        return tournamentID