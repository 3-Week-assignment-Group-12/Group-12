from __future__ import annotations
from .main_data_manager import MainData

class DL_API:
    
    def __init__(self) -> None:
        self.UI_manager = MainData()

    @staticmethod
    def create_api() -> DL_API:
        return DL_API()
        
    def start_menu(self) -> None:
        self.UI_manager.example()
    