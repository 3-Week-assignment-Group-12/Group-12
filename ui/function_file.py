

from typing import Literal
from logic.logic_wrapper import LogicWrapper
from models.tournament import Tournament
from models.player import Player
from models.team import Team
from typing import Literal


class functionFile:
    """Helper class for UI input and validation."""

    def __init__(self,logic_wrapper:LogicWrapper) -> None:
        """Initialize functionFile with a LogicWrapper instance.

        Args:
            logic_wrapper (LogicWrapper): The logic layer interface used to access and modify data.
        """
        self.logic_wrapper = logic_wrapper



    #------------------Functions--------------------------#
    def create_team(self):
        """Create a new team via user input and send it to the logic layer."""
        
        id_of_user= input("Enter Captains National ID (q to stop): ")
        name = input("Enter team name (q to stop): ")
        tag = input("Enter team tag (max 20 char) (q to stop): ")
        while True:

            team_size=self.teamSize()
            team_list = []
            choice = input("add members? (y/n): ").lower()
            
            if choice == "y":
                existing_players = self.logic_wrapper.get_players()
                while True:
                    
                    val = input("Enter team member Kennitala (q to stop): ")
                    if val.lower() == "q":
                        break
                    
                    for x in existing_players: # check if team already exists in list, if not then player gets added
                        if val == str(x.id) and x.id not in team_list:
                            team_list.append(int(val))
                            continue
                        
                    print("player id not registered")
                    print()
                        
            self.logic_wrapper.create_team(name,tag,id_of_user,team_size,team_list)
            

    def teamSize(self) -> int | Literal[False]:  # function to handle and prevent invalid input
        """function to handle and prevent invalid input

        Returns:
            int | bool -- int as output valid team size, false otherwise
        """
        while True:
            team_size = input("Enter team size (q to stop): ")
            if team_size=="q":
                return False
            
            try:
                team_size=int(team_size)
                return team_size
            except:
                print("Team size must be digits only!")

    def check_for_tournament_ID(self) -> int | str: # function to handle and prevent invalid input
        """function to handle and prevent invalid input

        Returns:
            int | str -- int as output valid id, str if contact id had to change
        """
        ID = input("Contact ID (q to stop): ")
        list_of_tournaments=self.logic_wrapper.get_tournaments()
        while True:
            
            if list_of_tournaments is None or list_of_tournaments == []:
                return ID
            
            for tournamentID in list_of_tournaments:
                tournament_info=self.logic_wrapper.get_team_by_ID(tournamentID.id)
                if isinstance(tournament_info,Tournament):
                    if ID == tournament_info.id: 
                        print("This tournament ID already exists!")
                        ID = input("Enter different Contact ID (q to stop): ")
                    else:
                        return ID
    

    

    def check_for_team_name(self) -> str: # function to handle and prevent invalid input
        """Prompt for a team name and ensure it is unique.

        Returns:
            str: A team name that does not already exist in the system.
        """
        name = input("Enter team name (q to stop): ")
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
                            name = input("Enter different team name (q to stop): ")
                        else:
                            return name
                        
                    else:
                        print("invalid name")
                        name = input("Enter different team name (q to stop): ")
            
    def check_for_team_tag(self) -> str: # function to handle and prevent invalid input
        """function to handle and prevent invalid input

        Returns:
            str -- outputs valid tag
        """
        tag = input("Enter team tag (q to stop): ")
        list_of_teams=self.logic_wrapper.get_teams()
        while True: 
            
            if list_of_teams is None or list_of_teams == []:
                    return tag
            for teamID in list_of_teams:
                teaminfo=self.logic_wrapper.get_team_by_ID(teamID.id)
                if isinstance(teaminfo,Team):
                    if tag == teaminfo.tag: 
                        print("Tag already exists!")
                        tag = input("Enter different team tag (q to stop): ")
                    else:
                        return tag
                    


    def checkTeamID(self) -> int | Literal[False]: # function to handle and prevent invalid input
        """function to handle and prevent invalid input

        Returns:
            int | Literal[False] -- int as output of valid id, false otherwise
        """
        while True:
            teamID=input("Enter Team ID (q to stop): ")
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
                

    
    def check_existingID(self) -> str | Literal[False]: # function to handle and prevent invalid input
        """function to handle and prevent invalid input

        Returns:
            str | Literal[False] -- str as output of valid id, false otherwise
        """
        playersID=input("Enter National ID (q to stop): ")
        if playersID=="q":
            return False
        
        check = self.logic_wrapper.get_player_by_ID(playersID)
        while not isinstance(check, Player):
            print("Player does not exist, Try different ID")
            playersID=input("Enter National ID (q to stop): ")
            if playersID == "q":
                return False

        return playersID
    


    def check_for_player_kt(self,nID: str) -> bool:# function to handle and prevent invalid input
        """function to check if id is available

        Arguments:
            nID {str} -- player id to check for

        Returns:
            bool -- true if id is available, false if not
        """
        list_of_players= self.logic_wrapper.get_players()
        if list_of_players is None or list_of_players == []:
            return True
        
        for player in list_of_players:
            playerinfo = self.logic_wrapper.get_player_by_ID(player.id)
            if isinstance(playerinfo,Player):
                if nID == playerinfo.id: 
                    print("This national ID already exists!")
                    return False
                
                else:
                    return True
            
        return False
                        

    def check_for_player_email(self,email:str) -> bool:# function to handle and prevent invalid input
        """function to check if id is available

        Arguments:
            email {str} -- email to check for

        Returns:
            bool -- true if it is available, false if not
        """
        list_of_players = self.logic_wrapper.get_players()
        if list_of_players is None or list_of_players == []:
            return True
        
        for player in list_of_players:
            playerinfo = self.logic_wrapper.get_player_by_ID(player.id)
            if isinstance(playerinfo,Player):
                if email == playerinfo.email: 
                    return False
                
        return True
                
    

    def input_phone_nr(self) -> str | Literal[False]:# function to handle and prevent invalid input
        """function to receive phone number and validate it

        Returns:
            str | Literal[False] -- str as output valid phone number, false otherwise
        """
        while True:
            number:str=input("Phone number (q to stop):")
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
        

    def input_name(self) -> str | Literal[False]:# function to handle and prevent invalid input
        """function to receive name and to validate it

        Returns:
            str | Literal[False] -- str as valid name, false otherwise
        """
        while True:
            name:str=input("Name (q to stop): ")
            if name=="q":
                return False
            
            check = self.logic_wrapper.check_name(name)
            if check == "1":
                print("Numbers are not allowed in name!")

            else:
                return name
                
    def input_email(self) -> str | Literal[False]:# function to handle and prevent invalid input
        """function to receive email and to validate it

        Returns:
            str | Literal[False] -- str as valid email, false otherwise
        """
        check2 = False
        email =""
        while check2 == False :
            email:str=input("Email (q to stop): ")
            if email=="q":
                return False
            
            check1 = self.logic_wrapper.check_email(email)
            if check1 == "1":
                print("Email must contain @ symbol!")

            else:
                check2=self.check_for_player_email(email)
                if check2 == False:
                    print("Email already exists in system!")

                else:
                    return email
                
        return False
    



    def inputplayersID(self) -> str | Literal[False]:# function to handle and prevent invalid input
        """function to receive player id and validate it

        Returns:
            str | Literal[False] -- str as valid id, false otherwise
        """
        while True:
            playersID=input("Enter National ID (q to stop): ")
            if playersID=="q":
                return False
            
            check1 = self.logic_wrapper.valid_kt(playersID)
            if check1 == "1":
                print("National ID needs to be exactly 10 numbers")

            elif check1 == "2":
                print("National ID cant have letters")

            elif check1 == "3" or check1 == "4":
                print("This ID does not exist")

            else:
                check2 = self.check_for_player_kt(playersID)
                if check2 == True:
                    return playersID
                
                
    def inputPlayerHandle(self) -> str | Literal[False]:# function to handle and prevent invalid input
        """function to receive player handle

        Returns:
            str | Literal[False] -- str as valid handle, false otherwise
        """
        while True:
            player_handle:str = input("Enter player handle (q to stop): ")
            if player_handle == "q":
                return False
            
            check = self.logic_wrapper.check_player_handle(player_handle)
            if check == False:
                print("Player handle is taken!")

            else:
                return player_handle
            
    def inputPlayerLink(self) -> str | Literal[False]:# function to handle and prevent invalid input
        """function to receive player link

        Returns:
            str | Literal[False] -- str as valid link, false otherwise
        """
        while True:
            player_link:str = input("Enter player link (q to stop): ")
            if player_link == "q":
                return False
            
            check = self.logic_wrapper.check_player_link(player_link)
            if check == False:

                print("Player link is taken!")

            else:
                return player_link
            
                
    
    #-----------------TeamLeader------------------

    def inputTeamName(self) -> str | Literal[False]: # function to handle and prevent invalid input
        """function to receive team name

        Returns:
            str | Literal[False] -- str as valid name, false otherwise
        """
        while True:
            name:str=input("Name (q to stop): ")
            if name=="q":
                return False
            
            if len(name)>20:
                print("Team name too long!")
                print("can not be longer then 20")
            
            check= self.logic_wrapper.check_for_team_name(name)
            if check == False:
                print("Team name already exists!")

            else:
                return name
        ## check if team name is already in use, create a function in logiclayer for that and call it here
            
    def inputTeamTag(self) -> str |Literal[False]:
        """function to receive team tag

        Returns:
            str |Literal[False] -- str as valid tag, false otherwise
        """
        while True:
            tag:str=input("Enter Tag ( max 5 letters/numbers ) (q to stop): ")
            if tag=="q":
                return False
            
            check = self.logic_wrapper.check_for_team_tag(tag)
            if check == "1":
                print("Too many letters/numbers!")
                continue
            
            if check == "2":
                print("Team tag already exists!")
                continue
            else:
                return tag
            
    def input_creatorID(self) -> str | Literal[False]: # function to handle and prevent invalid input
        """function to receive creator id

        Returns:
            str -- str as valid creator id
        """
        while True:
            creatorID=input("Enter Creator National ID (q to stop): ")
            if creatorID == "q":
                return False
            
            check1 = self.logic_wrapper.valid_kt(creatorID)
            if check1 == "1":
                print("National ID needs to be exactly 10 numbers")
                continue

            elif check1=="2":
                print("National ID cant have letters")
                continue

            elif check1=="3" or check1=="4":
                print("This ID does not exist")  
                continue

            else:
                return creatorID
        

    
    #-----------Clubs----------
    def inputClubName(self) -> str | Literal[False]: # function to handle and prevent invalid input
        """function to receive club name

        Returns:
            str | Literal[False] -- str as valid club name, false otherwise
        """
        while True:
            name:str=input("Name (q to stop): ")
            if name=="q":
                return False
            
            if len(name) > 20:
                print("club name too long!")
                print("can not be longer then 20")
                continue

            check1 = self.logic_wrapper.check_name(name)
            if check1 == "1":
                print("Club name can only contain letters!")
                continue

            else:
                check2= self.logic_wrapper.check_for_club_name(name)
                if check2 ==False:
                    print("club name already exists!")
                    continue

                else:
                    return name
            
    def inputClubColor(self) -> str | Literal[False]:# function to handle and prevent invalid input
        """function to receive club colour

        Returns:
            str | Literal[False] -- str as valid colour
        """
        while True:
            color:str=input("Color (q to stop): ")
            if color=="q":
                return False
            
            check1 = self.logic_wrapper.check_name(color)
            if check1 == "1":
                print("Club color can only contain letters!")
                continue

            else:
                return color


    def input_tournament_name(self) -> str | Literal[False]:# function to handle and prevent invalid input
        """function to receive tournament name

        Returns:
            str | Literal[False] -- str as valid name, false otherwise
        """
        while True:
            tournament_name:str=input("Tournament name (q to stop): ")
            if tournament_name=="q":
                return False
            
            check = self.logic_wrapper.check_for_tournament_name(tournament_name)
            if check == False:
                print("Tournament name already exists!")

            else:
                return tournament_name
            

    def input_start_date(self) -> str | Literal[False]:# function to handle and prevent invalid input
        """function to receive start date

        Returns:
            str | Literal[False] -- str as valid start date, false otherwise
        """
        while True:
            startDate = input("Enter Start Date (q to stop): ")
            if startDate == "q":
                return False
            
            check = self.logic_wrapper.validateDate(startDate)       
            if check == None:
                print("Date format is wrong! (example of correct format: dd.mm.yyyy)") 
                continue

            else:
                return startDate

    def input_end_date(self, startDate:str) -> str | Literal[False]: # function to handle and prevent invalid input
        """function to receive end date

        Arguments:
            startDate {str} -- start date to base by

        Returns:
            str | Literal[False] -- str as valid end date, false for otherwise
        """
        while True:
            endDate = input("Enter End Date (q to stop): ")
            if endDate == "q":
                return False
            
            check = self.logic_wrapper.validateDate(endDate)       
            if check == None:
                print("Date format is wrong! (example of correct format: dd.mm.yyyy)") 

            check2 = self.logic_wrapper.validEndDate(startDate,endDate)
            if check2 == False:
                print("EndDate cannot occur before StartDate!")

            else:
                return endDate
        
    def input_match_time(self) -> str | Literal[False]: # function to handle and prevent invalid input
        """function to receive match time

        Returns:
            str | Literal[False] -- str as valid time, false otherwise
        """
        while True:
            matchTime = input("Enter Match Time (MM:SS) (q to stop): ")
            if matchTime == "q":
                return False
            
            check = self.logic_wrapper.validateMatchTime(matchTime)       
            if check == None:
                print("Match Time format is wrong! (example of correct format: MM:SS - minutes:seconds)") 
                continue

            else:
                return matchTime

    def input_contact_ID(self) -> str |Literal[False]:# function to handle and prevent invalid input
        """function to receive contact id

        Returns:
            str |Literal[False] -- str as valid id, false otherwise
        """
        while True:
            contactID=input("Enter Contact ID (q to stop): ")
            if contactID == "q":
                return False
            
            check = self.logic_wrapper.valid_kt(contactID)
            if check == "1":
                print("Contact ID should be exactly 10 numbers!")

            elif check == "2":
                print("ID must only contain numbers!")

            elif check == "3":
                print("Day date in ID is invalid!")

            elif check == "4":
                print("Month date in ID is invalid!")

            else:
                return contactID
            
    def input_contact_email(self) -> str | Literal[False]: # function to handle and prevent invalid input
        """function to receive contact email

        Returns:
            str | Literal[False] -- str as valid email, false otherwise
        """
        while True:
            contactEmail = input("Enter Contact Email (q to stop): ")
            if contactEmail == "q":
                return False
            
            check = self.logic_wrapper.check_email(contactEmail)
            if check == "1":
                print("Email must have 1 @ symbol!")

            else:
                return contactEmail
            
    def input_contact_phone_nr(self) -> str | Literal[False]:# function to handle and prevent invalid input
        """function to receive contact phone

        Returns:
            str | Literal[False] -- str as valid phone, false otherwise
        """
        while True:
            contactPhone = input("Enter Contact Phone Number (q to stop): ")
            if contactPhone == "q":
                return False
            
            check = self.logic_wrapper.check_contact_phone_nr(contactPhone)
            if check == "1":
                print("Phone number must be exactly 7 digits long!")

            elif check == "2":
                print("Phone number cannot contain any letters!")

            else:
                return contactPhone


            

            
    def add_data_to_team_int(self,team_id:int,key:str, value:int) -> None: # add data to dynamic data in team
        """assigns data to all players in team

        Arguments:
            team_id (int): team id
            key (str): what key to the value under
            value (int): the value, is additive

        Returns:
            None
        """
        
        team = self.logic_wrapper.get_team_by_ID(team_id)
        if isinstance(team,Team):
            for p in team.member_list:
                play = self.logic_wrapper.get_player_by_ID(p)
                if isinstance(play,Player):
                    play.dynamic_data[key] += value
                    self.logic_wrapper.modify_player(play)
        
    def add_data_to_player_int(self,player_id:str, key:str, value:int) -> None:# add data to dynamic data
        """assign data to single player

        Arguments:
            player_id (str): player id
            key (str): what key to the value under
            value (int): the value, is additive

        Returns:
            None
        """
        play = self.logic_wrapper.get_player_by_ID(player_id)
        if isinstance(play,Player):
            
            play.dynamic_data[key] += value
            
            self.logic_wrapper.modify_player(play)
            
        
    def get_data_from_team(self,team_id:int, key:str="") -> dict[str,int]|int|bool: # gets dynamic data
        """Gets totaled dynamic data

        Arguments:
            team_id (int): team id
            key (str, optional): key from where to get data. Defaults to "".

        Returns:
            dict|int|bool: 
                dict of all data if key is not provided
                int of total data if key is provided
                bool for failure
        """
        players = self.logic_wrapper.get_players_by_team_ID(team_id)
        if isinstance(players,bool):
            return False
            
        if key == "": #case: no key provided
            
            grouped_data = {}
            for p in players:
            
                for k in p.dynamic_data.keys():
                    
                    try:
                        grouped_data[k] += p.dynamic_data[k]
                    
                    except:
                        grouped_data[k] = 0
                        grouped_data[k] += p.dynamic_data[k]
                    
            return grouped_data
        
        else:
            value = 0
            for p in players:

                value += p.dynamic_data[key]
            return value            
              
    
    def inputClubID(self) -> int | Literal[False]: # add data to dynamic data in team
        """function to receive club id

        Returns:
            int | Literal[False] -- int as valid id, false otherwise
        """
        while True:
            clubID=input("Enter Club ID (q to stop): ")
            if clubID=="q":
                return False
            try:
                clubID = int(clubID)
                check = self.logic_wrapper.get_club_by_ID(clubID)
                if check == False:
                    print("Club does not exist, Try different ID")

                else:
                    return clubID
            except:
                print("ClubID must be digits only!")

    
    def inputTournamentID(self) -> int | None: # add data to dynamic data in team
        """function to receive tournament id

        Returns:
            int | None -- int as valid id, false otherwise
        """
        while True:
            tournamentID = input("Enter Tournament ID(q for cancel): ")
            if tournamentID.lower() == "q":
                return None

            if not tournamentID.isdigit():
                print("Please enter a numeric tournament ID")
                continue

            tid = int(tournamentID)
            check = self.logic_wrapper.get_tournament_by_ID(tid)
            if check is False:
                print("Tournament does not exist, Try different ID")
                continue

            return tid
                
    
    def score(self) -> int | Literal[False]: # add data to dynamic data in team
        """function to receive score

        Returns:
            int | Literal[False] -- int as valid score, false otherwise
        """
        while True:
            score = input("Enter score (q to stop): ")
            if score=="q":
                return False
            
            try:
                score = int(score)
                return score
            
            except:
                print("score must be digits only!")

    def winner(self) -> int | Literal[False]: # add data to dynamic data in team
        """function to receive winner id

        Returns:
            int | Literal[False] -- int as valid winner id, false otherwise
        """
        while True:
            winner = input("Enter winner id (q to stop): ")
            if winner=="q":
                return False
            
            try:
                winner = int(winner)
                return winner
            
            except:
                print("winner id must be digits only!")

        
    
        
        
  
