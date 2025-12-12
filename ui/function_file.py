

from logic.logic_wrapper import LogicWrapper
from models.tournament import Tournament
from models.player import Player
from models.team import Team


class functionFile:
    """Helper class for UI input and validation.

    This class encapsulates functions that:
    - Collect user input from the console.
    - Call the LogicWrapper to validate or manipulate data.
    - Return cleaned/validated values back to UI menus.
    """

    def __init__(self,logic_wrapper:LogicWrapper) -> None:
        """Initialize functionFile with a LogicWrapper instance.

        Args:
            logic_wrapper (LogicWrapper):
                The logic layer interface used to access and modify data.
        """
        self.logic_wrapper = logic_wrapper



        #------------------Functions--------------------------#
    def create_team(self):
        """Create a new team via user input and send it to the logic layer.

        Prompts the user for team information (captain ID, name, tag,
        team size, and optional list of members) and calls
        LogicWrapper.create_team().

        Returns:
            None
        """
        id_of_user= input("Enter Captains National ID: ")
        name = input("Enter team name: ")
        tag = input("Enter team tag (max 20 char): ")
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
                    
                    for x in existing_players:
                        if val == str(x.id) and x.id not in team_list:
                            team_list.append(int(val))
                            continue
                        
                    print("player id not registered")
                    print()
                        
            self.logic_wrapper.create_team(name,tag,id_of_user,team_size,team_list)
            

    def teamSize(self):
            while True:
                team_size = input("Enter team size: ")
                if team_size=="q":
                    return False
                try:
                    team_size=int(team_size)
                    return team_size
                except:
                    print("Team size must be digits only!")
                
        
        
        
    
        

    def get_players(self): #Requirement 4
        """Trigger retrieval of all players from the logic layer.

        Note:
            This function delegates to LogicWrapper.get_players().
            It does not return or print the list by itself.

        Returns:
            None
        """
        # UI talks ONLY to Logic
        self.logic_wrapper.get_players()

    def check_for_tournament_ID(self):
        """Request a contact/tournament ID and ensure it is unique.

        Prompts the user for an ID and checks against existing tournaments.
        If the ID is already in use, repeatedly asks for a new one.

        Returns:
            str:
                A contact/tournament ID that does not conflict with
                existing tournaments.
        """
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
    

    

    def check_for_team_name(self):
        """Prompt for a team name and ensure it is unique.

        Returns:
            str:
                A team name that does not already exist in the system.
        """
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
        """Prompt for a team tag and ensure it is unique.

        Returns:
            str:
                A team tag that does not already exist in the system.
        """
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
        """Ask for a team ID and verify that it exists in the system.

        The user can enter 'q' to cancel the operation.

        Returns:
            int | bool:
                * int: Valid team ID if the team exists.
                * False: If user cancels with 'q'.
        """
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
                

    
    def check_existingID(self):
        """Request an existing player ID and validate it.

        Prompts until a valid player ID is entered or 'q' is used
        to cancel.

        Returns:
            str | bool:
                * str: Valid player national ID.
                * False: If the user cancels with 'q'.
        """
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
            """Check if a national ID (KT) is already in use.

            Args:
                nID (str):
                    National ID to be checked.

            Returns:
                bool:
                    * True: ID is not in use and can be used.
                    * False: ID already exists in the system.
            """
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
        """Check if an email is already in use by another player.

        Args:
            email (str):
                Email to check for uniqueness.

        Returns:
            bool:
                * True: Email is not in use.
                * False: Email already exists in the system.
        """
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
        """Prompt user for a phone number and validate it.

        Validation:
            - Must be length 7.
            - Must contain digits only.
            - Must not already exist in the system.

        Returns:
            str | bool:
                * str: Valid phone number.
                * False: If the user cancels with 'q'.
        """
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
        """Prompt user for a name and validate it.

        Validation:
            - Name must contain letters only (no digits).

        Returns:
            str | bool:
                * str: Valid name string.
                * False: If the user cancels with 'q'.
        """
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
        """Prompt user for an email and validate format + uniqueness.

        Validation:
            - Must contain exactly one '@'.
            - Must not already exist in the system.

        Returns:
            str | bool:
                * str: Valid and unique email address.
                * False: If the user cancels with 'q'.
        """
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
        """Prompt user for a player national ID and validate it.

        Validation:
            - Delegates format checks to LogicWrapper.valid_kt().
            - Ensures ID is not already in use.

        Returns:
            str | bool:
                * str: Valid and unique national ID.
                * False: If the user cancels with 'q'.
        """
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
                
                
    def inputPlayerHandle(self):
        """Prompt user for a player handle and ensure it is unique.

        Returns:
            str | bool:
                * str: Valid and unique player handle.
                * False: If the user cancels with 'q'.
        """
        while True:
            player_handle:str = input("Enter player handle: ")
            if player_handle == "q":
                return False
            check = self.logic_wrapper.check_player_handle(player_handle)
            if check == False:
                print("Player handle is taken!")
            else:
                return player_handle
            
    def inputPlayerLink(self):
        """Prompt user for a player link and ensure it is unique.

        Returns:
            str | bool:
                * str: Valid and unique player link.
                * False: If the user cancels with 'q'.
        """
        while True:
            player_link:str = input("Enter player link: ")
            if player_link == "q":
                return False
            check = self.logic_wrapper.check_player_link(player_link)
            if check == False:
                print("Player link is taken!")
            else:
                return player_link
            
                
    
    #-----------------TeamLeader------------------

    def inputTeamName(self):
        """Prompt user for a team name and validate it for length and uniqueness.

        Validation:
            - Name length must be <= 20.
            - Name must not already exist.

        Returns:
            str | bool:
                * str: Valid team name.
                * False: If the user cancels with 'q'.
        """
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
        """Prompt user for a team tag and validate it via logic layer.

        Validation (by logic layer):
            - Tag length must be <= 5.
            - Tag must be unique.

        Returns:
            str | bool:
                * str: Valid team tag.
                * False: If the user cancels with 'q' or validation fails.
        """
        while True:
            tag:str=input("Enter Tag ( max 5 letters/numbers ): ")
            if tag=="q":
                return False
            check=self.logic_wrapper.check_for_team_tag(tag)
            if check=="1":
                print("Too many letters/numbers!")
                return False
            if check=="2":
                print("Team tag already exists!")
                return False
            else:
                return tag
            
    def input_creatorID(self):
        """Prompt user for a creator (captain) national ID and validate it.

        Validation:
            - Delegates to LogicWrapper.valid_kt() for format checks.

        Returns:
            str:
                The entered creator national ID (even if invalid; validation
                feedback is printed but value is still returned).
        """
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
        """Prompt user for a club name and validate it.

        Validation:
            - Length must be <= 20.
            - Only letters allowed.
            - Club name must be unique.

        Returns:
            str | bool:
                * str: Valid club name.
                * False: If the user cancels with 'q'.
        """
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
        """Prompt user for club colour and validate it as letters-only.

        Returns:
            str | bool:
                * str: Valid club colour string.
                * False: If the user cancels with 'q'.
        """
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
        """Prompt user for a tournament name and ensure it is unique.

        Returns:
            str | bool:
                * str: Valid tournament name.
                * False: If the user cancels with 'q'.
        """
        while True:
            tournament_name:str=input("Tournament name: ")
            if tournament_name=="q":
                return False
            check = self.logic_wrapper.check_for_tournament_name(tournament_name)
            if check == False:
                print("Tournament name already exists!")
            else:
                return tournament_name
            

    def input_start_date(self):
        while True:
            startDate = input("Enter Start Date: ")
            if startDate == "q":
                return False
            check = self.logic_wrapper.validateDate(startDate)       
            if check == "1":
                print("Date format is wrong! (example of correct format: 11.12.2025)") 
            elif check == "2":
                print("Date format is wrong! (example of correct format: 11.12.2025)") 
            elif check == "3":
                print("Date format is wrong! (example of correct format: 11.12.2025)") 
            elif check == "4":
                print("Date format is wrong! (example of correct format: 11.12.2025)") 
            elif check == "5":
                print("Date format is wrong! (example of correct format: 11.12.2025)") 
            elif check == "6":
                print("Date format is wrong! (example of correct format: 11.12.2025)") 
            elif check == "7":
                print("Date format is wrong! (example of correct format: 11.12.2025)") 
            else:
                return startDate

    def input_end_date(self, startDate):
        while True:
            endDate = input("Enter End Date: ")
            if endDate == "q":
                return False
            check = self.logic_wrapper.validateDate(endDate)       
            if check == None:
                print("Date format is wrong! (example of correct format: 12.12.2025)") 
            check2 = self.logic_wrapper.validEndDate(startDate,endDate)
            if check2 == False:
                print("EndDate cannot occur before StartDate!")
            else:
                return endDate

    def input_contact_ID(self):
        """Prompt user for a contact ID (organizer ID) and validate it.

        Validation:
            - Delegates to LogicWrapper.valid_kt().
            - Must be exactly 10 digits and a valid "date" encoding.

        Returns:
            str | bool:
                * str: Valid contact ID.
                * False: If the user cancels with 'q'.
        """
        while True:
            contactID=input("Enter Contact ID: ")
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
            
    def input_contact_email(self):
        while True:
            contactEmail = input("Enter Contact Email: ")
            if contactEmail == "q":
                return False
            check = self.logic_wrapper.check_email(contactEmail)
            if check == "1":
                print("Email must have 1 @ symbol!")
            else:
                return contactEmail
            
    def input_contact_phone_nr(self):
        while True:
            contactPhone = input("Enter Contact Phone Number: ")
            if contactPhone == "q":
                return False
            check = self.logic_wrapper.check_contact_phone_nr(contactPhone)
            if check == "1":
                print("Phone number must be exactly 7 digits long!")
            elif check == "2":
                print("Phone number cannot contain any letters!")
            else:
                return contactPhone


            

            
    def add_data_to_team_int(self,team_id:int,key:str, value:int):
        """assigns data to all players in team

        Args:
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
        
    def add_data_to_player_int(self,player_id:str, key:str, value:int):
        """assign data to single player

        Args:
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
            
        
    def get_data_from_team(self,team_id:int, key:str="") -> dict[str,int]|int|bool:
        """Gets totaled dynamic data

        Args:
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
              
    
    def inputClubID(self):
        """Prompt user for a club ID and validate existence.

        The user can enter 'q' to cancel the operation.

        Returns:
            int | bool:
                * int: Valid club ID.
                * False: If the user cancels with 'q'.
        """
        while True:
            clubID=input("Enter Club ID: ")
            if clubID=="q":
                return False
            try:
                clubID=int(clubID)
                check= self.logic_wrapper.get_club_by_ID(clubID)
                if check == False:
                    print("Club does not exist, Try different ID")
                else:
                    return clubID
            except:
                print("ClubID must be digits only!")

    
    def inputTournamentID(self) -> int | None:
        """Prompt user for a tournament ID and validate existence.

        The user can enter 'q' to cancel the operation.

        Returns:
            int | None:
                * int: Valid tournament ID.
                * None: If the user cancels with 'q'.
        """
        while True:
            tournamentID=input("Enter Tournament ID(q for cancel): ")
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
                
    
    def score(self):
        while True:
            score = input("Enter score: ")
            if score=="q":
                return False
            try:
                score=int(score)
                return score
            except:
                print("score must be digits only!")

    def winner(self):
        while True:
            winner = input("Enter winner id: ")
            if winner=="q":
                return False
            try:
                winner=int(winner)
                return winner
            except:
                print("winner id must be digits only!")

        
    
        
        
  
