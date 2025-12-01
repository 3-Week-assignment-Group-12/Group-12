
carFilepath:str = "./filename.txt"
def write_str(data:str):
    
    with open(carFilepath, 'ax' ) as theFile:
        theFile.write(data)