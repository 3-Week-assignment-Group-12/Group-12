from models.player import Player
import csv

class DataWrapper:
    def __init__(self):
        self.playerFilePath:str = "./data/files/filename.txt" #the file location
        pass
    
    
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
                player = Player( line[0] ) # more attrebutes as needed currently only has name
                Players.append(player)  #add player to players list

        theFile.close()
        return Players #return the players
        
        
