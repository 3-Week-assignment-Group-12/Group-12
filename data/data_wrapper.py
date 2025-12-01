from models.player import Player
import csv

class DataWrapper:
    def __init__(self):
        self.playerFilePath:str = "./data/files/filename.txt"
        pass
    
    def write_player(self, new_player:Player) -> bool:
        """ Writes new player data. returns False if failed and True if it worked"""
        
        with open( self.playerFilePath, 'a' ) as theFile:
            csvWriter = csv.writer(theFile)
            try:
                csvWriter.writerow( new_player.toCSVList( ) )
            except:
				# if we fail, we return false to indicate this.
                return False
        theFile.close()
        return True
            
    def get_players(self) -> list[Player]:
        Players = [] # empty list 
        
        with open( self.playerFilePath, "r+" ) as theFile:
            csvReader = csv.reader(theFile)
            next(csvReader) # skip header
            for line in csvReader:
				# turn csv line into player instance
                player = Player( line[0] ) # more attrebutes as needed
                Players.append(player) 

        theFile.close()
        return Players 
        
        
