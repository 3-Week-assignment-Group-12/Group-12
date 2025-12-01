from __future__ import annotations
from main_UI_manager import UI_manager

class UL_API:
    def __init__(self) -> None:
        self.UI_manager = UI_manager()

    @staticmethod
    def create_api() -> UL_API:
        return UL_API()
        
    def start_menu(self) -> int:
        
        return self.UI_manager.start_menu()