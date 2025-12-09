from ui.main_menu import MainMenu

def main():
    # Instantiate the UI
    ui = MainMenu()
    # Start the application loop
    ui.logic_wrapper.get_dummy_data()

    ui.run()
    
    

if __name__ == "__main__":
    main()
    