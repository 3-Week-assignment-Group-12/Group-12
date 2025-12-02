from models.player import Player
import csv

from models.team import Team

to_int = lambda a: int(a)
    
class Main_data:
    def __init__(self):
        self.playerFilePath:str = "./data/files/players_data.txt" #the file location
        self.teamFilePath:str = "./data/files/teams_data.txt"
    
    
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
            
            
            
    def get_players(self) -> list[Player]:
        """ opens file and returns a list of players """
        Players = [] # empty list 
        
        with open( self.playerFilePath, "r+" ) as theFile: # opens file in read mode
            
            csvReader = csv.reader(theFile) #creates a csv handler
            
            #next(csvReader) # skip header    -- add when file has header
            
            for line in csvReader: # reads line by line
                
				# turn csv line into player instance
                player = Player( int(line[0]),line[1],line[2], int(line[3]),line[4],line[5] ) # more attrebutes as needed currently only has name
                Players.append(player)  #add player to players list

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
    
    def get_teams(self) -> list[Team]:
        """ opens file and returns a list of Teams """
        
        teams: list[Team] = [] # empty list 
        
        with open( self.teamFilePath, "r+" ) as theFile: # opens file in read mode
            
            csvReader = csv.reader(theFile) #creates a csv handler
            
            #next(csvReader) # skip header    -- add when file has header
            
            for line in csvReader: # reads line by line
                
				# turn csv line into team instance
                
                team = Team( int(line[0]),line[1],line[2], int(line[3]),int(line[4]), [( lambda a: int(a)) (x) for x in line[5].split(",")]) # uses list comprehension to convert str to list[int]
                teams.append(team)  #add player to team list

        theFile.close()
        return teams #return the players
    
    
        
