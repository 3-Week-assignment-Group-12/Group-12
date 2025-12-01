from __future__ import annotations

from .main_UI_manager import UI_manager



class UL_API:

    
    def __init__(self) -> None:
        self.UI_manager = UI_manager()
        self.LL_API_link = None
        self.wrap_to_LL = []

    @staticmethod
    def create_api() -> UL_API:
        return UL_API()
    