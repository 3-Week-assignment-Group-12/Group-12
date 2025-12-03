import os
from models.player import Player
import csv

from models.team import Team
from models.tournament import Tournament
    
class Main_data:
    def __init__(self):
        self.playerFilePath:str = "./data/files/players_data.csv"
        self.teamFilePath:str = "./data/files/teams_data.csv"
        self.tournamentFilePath:str = "./data/files/tournaments_data.csv"
        

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
        
        try:
            file =open(self.tournamentFilePath, "x")
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
    
    
    
    def write_tournament(self, new_taurnament:Tournament) -> bool:
        """ Writes new tournament data. returns False if failed and True if it worked"""
        
        with open( self.tournamentFilePath, 'a' ) as theFile: #open file in append mode
            
            csvWriter = csv.writer(theFile) #creates a csv handler
            
            try:
                csvWriter.writerow( new_taurnament.toCSVList( ) ) # try to write a row
            except:
				# if we fail, we return false to indicate this.
                return False
            
        theFile.close()
        return True # return True
            
            
            
    def get_players(self,path:str) -> list[Player]:
        """ opens file and returns a list of players """
        Players: list[Player] = [] # empty list 
        
        with open( path, "r+" ) as theFile: # opens file in read mode
            
            csvReader = csv.reader(theFile) #creates a csv handler
            
            for line in csvReader: # reads line by line
                
				# turn csv line into player instance
                try:
                    player = Player( int(line[0]),line[1],line[2], int(line[3]),line[4],line[5] ) # more attrebutes as needed currently only has name
                    Players.append(player)  #add player to players list
                except (IndexError, ValueError):
                    # Skip lines that don't match expected format
                    pass

        theFile.close()
        return Players #return the players
    
    
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
                except (IndexError, ValueError):
                    # Skip lines that don't match expected format
                    pass

        theFile.close()
        return teams #return the players
    
    
    def get_tournaments(self, path: str) -> list[Tournament]:
        """
        Opens the tournament file and returns a list of Tournament instances.

        Args:
            path (str): Path to the tournament CSV file (use self.tournamentFilePath).

        Returns:
            list[Tournament]: List of all Tournament objects found in the file.
        """
        tournaments: list[Tournament] = []

        with open(path, "r") as theFile:  # opens file in read mode
            csvReader = csv.reader(theFile)
            for line in csvReader:
                # Each line should represent a tournament; parse and convert fields
                try:
                    tournament_id = int(line[0])
                    name = line[1]
                    start_date = line[2]
                    end_date = line[3]
                    venue_name = line[4]
                    contact_name = line[5]
                    contact_email = line[6]
                    contact_phone = line[7]
                    team_list = [int(x) for x in line[8].split(",") if x]
                    matches = [int(x) for x in line[9].split(",") if x]
                    tournament = Tournament(
                        tournament_id, name, start_date, end_date, venue_name,
                        contact_name, contact_email, contact_phone, team_list, matches
                    )
                    tournaments.append(tournament)
                except (IndexError, ValueError):
                    # Skip lines that don't match expected format
                    pass

        return tournaments
    
    

    

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
        
        with open( self.teamFilePath, "w" ) as theFile: # wipes file. then writes
            
            csvWriter = csv.writer(theFile)
            
            for team in new_list:
                try:
                    csvWriter.writerow( team.toCSVList( ) ) # try to write a row
                except:
                    # if we fail, we return false to indicate this.
                    return False
        
        return True

    def overwrite_tournaments(self, new_list:list[Tournament]) -> bool:
        
        with open( self.tournamentFilePath, "w" ) as theFile: # wipes file. then writes
            
            csvWriter = csv.writer(theFile)
            
            for tournament in new_list:
                try:
                    csvWriter.writerow( tournament.toCSVList( ) ) # try to write a row
                except:
                    # if we fail, we return false to indicate this.
                    return False
        
        return True
    
    def modify_tournament(self,new_data_tournament:Tournament) -> bool:
        
        tournament_list = self.get_tournaments(self.tournamentFilePath)

        
        index = 0
        for x in tournament_list:
            if x.name == new_data_tournament.name:
                break
            index +=1
        if index == len(tournament_list)+1:
            return False
            
        tournament_list[index] = new_data_tournament
        
        self.overwrite_tournaments(tournament_list)
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









