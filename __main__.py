
from UI_layer.UL_API import UL_API
from logic_layer.LL_API import LL_API 
from data_layer.DL_API import DL_API 

def main():
    
    UL_api, LL_api, DL_api = run_setup()
    

    





def run_setup() -> tuple[UL_API, LL_API, DL_API]:
    
    UL_api = UL_API.create_api()    
    LL_api = LL_API.create_api()    
    DL_api = DL_API.create_api()
    
   
    
    return (UL_api, LL_api, DL_api)


if __name__ == "__main__":
    main()

