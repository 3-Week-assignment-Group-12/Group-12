# ui_layer/main_menu.py
from logic.logic_wrapper import LogicWrapper

class MainMenu:
    def __init__(self):
        # The UI creates an instance of the Logic Wrapper
        self.logic_wrapper = LogicWrapper()





    def run(self):
        print(
""" 
Welcome To the menu. 
little functionality has been added 


""")
        
        
        
        
        
        
    def create_player(self): # Requirement nr 1
        # UI gathers input
        name = input("Name: ")
        kt = int(input("kennitala:"))
        phone = int(input("phone: "))
        address = input("address: ")
        email = input("email: ")
        # UI talks ONLY to Logic
        self.logic_wrapper.create_player(kt,name,phone,address,email)
        