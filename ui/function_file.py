

from logic.logic_wrapper import LogicWrapper
from models.tournament import Tournament
from models.player import Player
from models.team import Team


class functionFile:
    def __init__(self,logic_wrapper:LogicWrapper) -> None:
        self.logic_wrapper = logic_wrapper



        #------------------Functions--------------------------#
    def create_team(self):
        id_of_user= input("Enter Captains National ID: ")
        name = input("Enter team name: ")
        tag = input("Enter team tag (max 20 char): ")
        team_size = int(input("Enter team size: "))
        team_list = []
        choice = input("add members? (y/n): ").lower()
        
        if choice == "y":
            existing_players = self.logic_wrapper.get_players()
            while True:
                
                val = input("Enter team member Kennitala (q to stop): ")
                if val.lower() == "q":
                    break
                
                for x in existing_players:
                    if val == str(x.id) and x.id not in team_list:
                        team_list.append(int(val))
                        continue
                    
                print("player id not registered")
                print()
                    
        self.logic_wrapper.create_team(name,tag,id_of_user,team_size,team_list)
        
        
    def create_player(self): # Requirement nr 1
        # UI gathers input
        name = input("Enter player Name: ")
        kt = int(input("Enter player kennitala:"))
        phone = int(input("Enter player phone: "))
        address = input("Enter player address: ")
        email = input("Enter player email: ")
        # UI talks ONLY to Logic
        self.logic_wrapper.create_player(kt,name,phone,address,email)
        

    def get_players(self): #Requirement 4
        # UI talks ONLY to Logic
        self.logic_wrapper.get_players()

    def check_for_tournament_ID(self):
        ID = input("Contact ID")
        list_of_tournaments=self.logic_wrapper.get_tournaments()
        while True:
            
            if list_of_tournaments is None or list_of_tournaments == []:
                return ID
            for tournamentID in list_of_tournaments:
                tournament_info=self.logic_wrapper.get_team_by_ID(tournamentID.id)
                if isinstance(tournament_info,Tournament):
                    if ID == tournament_info.id: 
                        print("This tournament ID already exists!")
                        ID = input("Enter different Contact ID")
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
    

    def check_for_team_name(self):

        name = input("Enter team name: ")
        list_of_teams=self.logic_wrapper.get_teams()
        if list_of_teams.__len__() == 0:
            return name
        else:
            while True:
                for team in list_of_teams:
                    teaminfo=self.logic_wrapper.get_team_by_ID(team.id)
                    if isinstance(teaminfo,Team):
                        if name == teaminfo.name:
                            print("Name already exists!")
                            name = input("Enter different team name: ")
                        else:
                            return name
                    else:
                        print("invalid name")
                        name = input("Enter different team name: ")
            
    def check_for_team_tag(self):
    
        tag = input("Enter team tag: ")
        list_of_teams=self.logic_wrapper.get_teams()
        while True: 
            
            if list_of_teams is None or list_of_teams == []:
                    return tag
            for teamID in list_of_teams:
                teaminfo=self.logic_wrapper.get_team_by_ID(teamID.id)
                if isinstance(teaminfo,Team):
                    if tag == teaminfo.tag: 
                        print("Tag already exists!")
                        tag = input("Enter different team tag: ")
                    else:
                        return tag
                    


    def checkTeamID(self):
        """ takes a team id and checks if the id exists in the system"""
        while True:
            teamID=input("Enter Team ID: ")
            if teamID=="q":
                    return False
            try:
                teamID = int(teamID)
                check= self.logic_wrapper.get_team_by_ID(teamID)
                if check == False:
                    print("Team does not exist, Try different ID")
                else:
                    return teamID
            except:
                print("TeamID must be digits only!")
                

    
    def check_excistingID(self):
        """Gets ID for existing player"""
        playersID=input("Enter National ID: ")
        if playersID=="q":
            return False
        check= self.logic_wrapper.get_player_by_ID(playersID)
        while not isinstance(check, Player):
            print("Player does not exist, Try different ID")
            playersID=input("Enter National ID: ")
            if playersID == "q":
                return False
            check= self.logic_wrapper.get_player_by_ID(playersID)
        return playersID
    


    def check_for_player_kt(self,nID):
            """checks if id is in use"""
          
            list_of_players= self.logic_wrapper.get_players()
            if list_of_players is None or list_of_players == []:
                return True
            for player in list_of_players:
                playerinfo=self.logic_wrapper.get_player_by_ID(player.id)
                if isinstance(playerinfo,Player):
                    if nID == playerinfo.id: 
                        print("This national ID already exists!")
                        return False
                    else:
                        return True
                        

    def check_for_player_email(self,email):
        """Gets email for existing player"""
        list_of_players=self.logic_wrapper.get_players()
        if list_of_players is None or list_of_players == []:
            return True
        for player in list_of_players:
            playerinfo=self.logic_wrapper.get_player_by_ID(player.id)
            if isinstance(playerinfo,Player):
                if email == playerinfo.email: 
                    return False
        return True
                
    

    def input_phone_nr(self):
        while True:
            number:str=input("Phone number:")
            if number=="q":
                return False
            check = self.logic_wrapper.check_phone_nr(number)
            if check == "1":
                print("Phone number is not the correct length!")
            elif check == "2":
                print("Only digits in phone number allowed!")
            elif check=="3":
                print("Number already exists!")
            else:
                return number
        

    def input_name(self):
        while True:
            name:str=input("Name: ")
            if name=="q":
                return False
            check = self.logic_wrapper.check_name(name)
            if check == "1":
                print("Numbers are not allowed in name!")
            else:
                return name
                
    def input_email(self):
        check2= False
        email=""
        while check2 == False :
            email:str=input("Email: ")
            if email=="q":
                return False
            check1=self.logic_wrapper.check_email(email)
            if check1 == "1":
                print("Email must contain @ symbol!")
            else:
                check2=self.check_for_player_email(email)
                if check2 == False:
                    print("Email already exists in system!")
                else:
                    return email
        return False
    



    def inputplayersID(self):
        while True:
            playersID=input("Enter National ID: ")
            if playersID=="q":
                return False
            check1=self.logic_wrapper.valid_kt(playersID)
            if check1 =="1":
                print("National ID needs to be exactly 10 numbers")
            elif check1=="2":
                print("National ID cant have letters")
            elif check1=="3" or check1=="4":
                print("This ID does not exist")
            else:
                check2=self.check_for_player_kt(playersID)
                if check2==True:
                    return playersID
                else: 
                    return False
                
    
    #-----------------TeamLeader------------------

    def inputTeamName(self):
        while True:
            name:str=input("Name: ")
            if name=="q":
                return False
            if len(name)>20:
                print("Team name too long!")
                print("can not be longer then 20")
            
            check= self.logic_wrapper.check_for_team_name(name)
            if check ==False:
                print("Team name already exists!")
            else:
                return name
        ## check if team name is already in use, create a function in logiclayer for that and call it here
            
    def inputTeamTag(self):
        while True:
            tag:str=input("Enter Tag ( max 5 letters/numbers ): ")
            if tag=="q":
                return False
            check=self.logic_wrapper.check_for_team_tag(tag)
            if check=="-1":
                print("Too many letters/numbers")
            else:
                return tag
            
    def input_creatorID(self):
        creatorID=input("Enter Creator National ID: ")
        check1 = self.logic_wrapper.valid_kt(creatorID)
        if check1 =="1":
            print("National ID needs to be exactly 10 numbers")
        elif check1=="2":
            print("National ID cant have letters")
        elif check1=="3" or check1=="4":
            print("This ID does not exist")  
        return creatorID
        

    
    #-----------Clubs----------
    def inputClubName(self):
        while True:
            name:str=input("Name: ")
            if name=="q":
                return False
            if len(name)>20:
                print("club name too long!")
                print("can not be longer then 20")
            check1 = self.logic_wrapper.check_name(name)
            if check1 == "1":
                print("Club name can only contain letters!")
            else:
                check2= self.logic_wrapper.check_for_club_name(name)
                if check2 ==False:
                    print("club name already exists!")
                else:
                    return name
            
    def inputClubColor(self):
        while True:
            color:str=input("Color: ")
            if color=="q":
                return False
            check1 = self.logic_wrapper.check_name(color)
            if check1 == "1":
                print("Club color can only contain letters!")
            else:
                return color


    def input_tournament_name(self):
        while True:
            tournament_name:str=input("Tournament name: ")
            if tournament_name=="q":
                return False
            check = self.logic_wrapper.check_for_tournament_name(tournament_name)
            if check == False:
                print("Tournament name already exists!")
            else:
                return tournament_name
            

    def input_contact_ID(self):
        while True:
            contactID=input("Enter Contact ID: ")
            if contactID == "q":
                return False
            check = self.logic_wrapper.valid_kt(contactID)
            if check == "1":
                print("Contact ID must be 10 numbers long!")
            elif check == "2":
                print("ID must only contain numbers!")
            elif check == "3":
                print("Day date in ID is invalid!")
            elif check == "4":
                print("Month date in ID is invalid!")
            else:
                return contactID
            

    def string_to_int(self,string):
        converted = int(string)
        return converted
            