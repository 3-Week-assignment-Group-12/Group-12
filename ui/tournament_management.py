from __future__ import annotations
# ui_layer/main_menu.py
from logic.logic_wrapper import LogicWrapper
from models.team import Team
from models.tournament import Tournament

from models.player import Player
from ui.Organizer_menu import OrganizerMenu
from ui.tournament_management import TournamentManagement

class TournamentManagement():
    def __init__(self,low : LogicWrapper) -> None:
        self.logic_wrapper = low
        pass

    

    #--------------Functions---------------












    #--------------Menus--------------------

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

Try again!!
""")
            choice=input("Enter input: ")
            
                
                
            
            match choice:
                case "1": 
                    name = input("Name of Tournament: ")
                    startDate = input("Start date: ")
                    endDate = input("End date: ")
                    venue=input("Location of Tournament: ")
                    contactID = int(input("Contact ID"))
                    contactEmail = input("Contact Email: ")
                    contactPhone = int(input("Contact Phone: "))
                    team_list=[]  # SKoða þetta
                    matches=[]    # sKoða þetta
                    self.logic_wrapper.create_tournament(name,startDate,endDate,venue,contactID,contactEmail,contactPhone,team_list,matches)
                case "2": 
                    self.edit_tournament_menu(int(input("Enter Tournament ID: ")))
                case "3": 
                    TID=int(input("Tournament ID"))
                    self.logic_wrapper.delete_tournament(TID)
                case "4": 
                    self.select_tournament_menu()
                case "b": 
                    return
                case _:
                    print("Invalid input")


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
            
        temp : Tournament = self.logic_wrapper.get_tournament_by_ID(tournamentID)   
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
          
    def select_tournament_menu(self):
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
        while True:
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
                    pass
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
            


