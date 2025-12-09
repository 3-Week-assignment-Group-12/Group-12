

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
                    


    def inputTeamID(self):
        teamID=int(input("Enter Team ID: "))
        check= self.logic_wrapper.get_team_by_ID(teamID)
        while check is False:
            print("Team does not exist, Try different ID")
            teamID=int(input("Enter Team ID: "))
            check= self.logic_wrapper.get_team_by_ID(teamID)
        return teamID
    
    def check_excistingID(self):
        playersID=input("Enter National ID: ")
        check = self.logic_wrapper.get_player_by_ID(playersID)
        while check is not isinstance(check, Player):
            print("Player does not exist, Try different ID")
            playersID=input("Enter National ID: ")
            check= self.logic_wrapper.get_player_by_ID(playersID)
        return playersID
    


    def check_for_player_kt(self,nID):
          
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
        list_of_players=self.logic_wrapper.get_players()
        if list_of_players is None or list_of_players == []:
            return True
        for player in list_of_players:
            playerinfo=self.logic_wrapper.get_player_by_ID(player.id)
            if isinstance(playerinfo,Player):
                if email == playerinfo.email: 
                    print("This email already exists!")
                    return False
                else:
                    return True
                
    

    def input_phone_nr(self):
        while True:
            number:str=input("Phone number:")
            check = self.logic_wrapper.check_phone_nr(number)
            if check == "1":
                print("Phone number is not the correct length!")
            elif check == "2":
                print("Only digits in phone number allowed!")

    def input_name(self):
        while True:
            name:str=input("Name: ")
            check = self.logic_wrapper.check_name(name)
            if check == "1":
                print("Numbers are not allowed in name!")
                
    def input_email(self):
        check2= False
        email=""
        while check2 == False :
            email:str=input("Email: ")
            check1=self.logic_wrapper.check_email(email)
            if check1 ==True:
                check2=self.check_for_player_email(email)
        return email
    



    def inputplayersID(self):
        playersID=input("Enter National ID: ")
        check1=self.logic_wrapper.valid_kt(playersID)
        if check1 =="1":
            print("National ID needs to be exactly 10 numbers")
        elif check1=="2":
            print("National ID cant have letters")
        elif check1=="3" or check1=="4":
            print("This ID does not exist")
        else:
            check2=self.check_for_player_kt(playersID)
            #check= self.logic_wrapper.get_player_by_ID(playersID)
            #while isinstance(check,int):
                #print("Player does not exist, Try different ID")
                #playersID=input("Enter National ID: ")
                #check= self.logic_wrapper.get_player_by_ID(playersID)
                #if playersID=="q":
                    #return False
            if check2==True:
                return playersID
            else: 
                return False
            
        

