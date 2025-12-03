import os
from models.player import Player
import csv

from models.team import Team
    
class Main_data:
    def __init__(self):
        #self.playerFilePath:str = "./data/files/players_data.csv" #the file location dummy_data/dummy_player.csv
        self.playerFilePath:str = "./dummy_data/dummy_player.csv"
        self.teamFilePath:str = "./data/files/teams_data.csv"
        

        self.check_files()
        
        
        
    def check_files(self) -> None:
        # make sure the folder exists
        os.makedirs("./data/files", exist_ok=True)
        
        # attempts to create files if they dont exist
        try:
            file = open(self.teamFilePath, "x")
            file.close()
        except FileExistsError:
            pass # if file exists, then ignore
        
        try:
            file =open(self.playerFilePath, "x")
            file.close()
        except FileExistsError:
            pass # if file exists, then ignore
    
    
    def write_player(self, new_player:Player) -> bool:
        """ Writes new player data. returns False if failed and True if it worked"""
        
        with open( self.playerFilePath, 'a' ) as theFile: #open file in append mode
            
            csvWriter = csv.writer(theFile) #creates a csv handler
            
            try:
                csvWriter.writerow( new_player.toCSVList( ) ) # try to write a row
            except:
				# if we fail, we return false to indicate this.
                return False
            
        theFile.close()
        return True # return True
            
            
            
    def get_players(self,path:str) -> list[Player]:
        """ opens file and returns a list of players """
        Players = [] # empty list 
        
        with open( path, "r+" ) as theFile: # opens file in read mode
            
            csvReader = csv.reader(theFile) #creates a csv handler
            
            for line in csvReader: # reads line by line
                
				# turn csv line into player instance
                try:
                    player = Player( int(line[0]),line[1],line[2], int(line[3]),line[4],line[5] ) # more attrebutes as needed currently only has name
                    Players.append(player)  #add player to players list
                except IndexError:
                    pass

        theFile.close()
        return Players #return the players
        
        
    def write_team(self, new_team:Team) -> bool:
        """ Writes new Team data. returns False if failed and True if it worked"""
        
        with open( self.teamFilePath, 'a' ) as theFile: #open file in append mode
            
            csvWriter = csv.writer(theFile) #creates a csv handler
            
            try:
                csvWriter.writerow( new_team.toCSVList( ) ) # try to write a row
            except:
				# if we fail, we return false to indicate this.
                return False
            
        theFile.close()
        return True # return True
    
    def get_teams(self,path) -> list[Team]:
        """ opens file and returns a list of Teams

        Args:
            path (str): use self.teampath

        Returns:
            list[Team]: list of all teams
        """
        
        
        
        teams: list[Team] = [] # empty list 
        
        with open( path, "r+" ) as theFile: # opens file in read mode
            
            csvReader = csv.reader(theFile) #creates a csv handler
            
            for line in csvReader: # reads line by line
                
				# turn csv line into team instance
                try:
                    team = Team( int(line[0]),line[1],line[2], int(line[3]),int(line[4]), [( lambda a: int(a)) (x) for x in line[5].split(",")]) # uses list comprehension to convert str to list[int]
                    teams.append(team)  #add player to team list
                except IndexError:
                    pass

        theFile.close()
        return teams #return the players
    

    def overwrite_players(self, new_list:list[Player]) -> bool:
        print(os.path.abspath(self.playerFilePath))
        with open( os.path.abspath(self.playerFilePath), "w" ) as theFile: # wipes file. then writes
            
            csvWriter = csv.writer(theFile)
            
            for player in new_list:
                try:
                    csvWriter.writerow( player.toCSVList( ) ) # try to write a row
                except:
                    # if we fail, we return false to indicate this.
                    return False
        
        return True
    
    
    def overwrite_teams(self, new_list:list[Team]) -> bool:
        
        with open( self.teamFilePath, "W" ) as theFile: # wipes file. then writes
            
            csvWriter = csv.writer(theFile)
            
            for team in new_list:
                try:
                    csvWriter.writerow( team.toCSVList( ) ) # try to write a row
                except:
                    # if we fail, we return false to indicate this.
                    return False
        
        return True
                
    
    
    def modify_player(self,new_data_player:Player) -> bool:
        
        player_list = self.get_players(self.playerFilePath)

        
        index = 0
        for x in player_list:
            if x.kt == new_data_player.kt:
                break
            index +=1
        if index == len(player_list)+1:
            return False
            
        player_list[index] = new_data_player
        
        self.overwrite_players(player_list)
        return True
        
    def modify_team(self,new_data_team:Team) -> bool:
        
        team_list = self.get_teams(self.teamFilePath)

        
        index = 0
        for x in team_list:
            if x.id == new_data_team.id:
                break
            index +=1
        if index == len(team_list)+1:
            return False
            
        team_list[index] = new_data_team
        
        self.overwrite_teams(team_list)
        return True
    
    
        
    def get_players_by_ID(self,ID):
        for x in self.get_players(self.playerFilePath):
            if x.kt==ID:
                return x
        return False
        
        
    def delete_player(self,player_id:int) -> bool:
        player_list = self.get_players(self.playerFilePath)
        
        count:int = 0
        for player in player_list:
            if player.kt == player_id:
                break
            count +=1
        if count == len(player_list)+1:
            return False
        
        player_list.pop(count)
        
        self.overwrite_players(player_list)
        return True
        
        
    def delete_team(self,team_id:int) -> bool:
        
        team_list = self.get_teams(self.teamFilePath)
        
        count:int = 0
        for player in team_list:
            if player.id == team_id:
                break
            count +=1
        if count == len(team_list)+1:
            return False
        
        team_list.pop(count)
        
        self.overwrite_teams(team_list)
        return True
        
                
        
        
        
        
    
    
        
