
from UI_layer.UL_API import UL_API
from logic_layer.
from data_layer.DL_API import DL_API

def main():
    
    # UL_api, LL_api, DL_api = run_setup() # pyright: ignore[reportUnusedVariable]
    UL_api = run_setup()
    
    while True:
    
        ret = UL_api.start_menu()
        if ret == 1:
            
            break



def run_setup() -> UL_API:
    
    UL_api = UL_API.create_api()    

   
    
    return UL_api

"""

def run_setup() -> tuple[UL_API, LL_API, DL_API]:
    
    UL_api = UL_API.create_api()    
    LL_api = LL_API.create_api()    
    DL_api = DL_API.create_api()
   
    
    return (UL_api, LL_api, DL_api)
"""

if __name__ == "__main__":
    main()

# example not allowed in strict
#def test(x,y):
#    return x+y