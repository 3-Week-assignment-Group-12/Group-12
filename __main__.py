from __future__ import annotations

from UI_layer.UL_API import UL_API

def main():
    UI_api = run_setup()
    UI_api.start_menu()


def run_setup():
    return UL_API.create_api()

def test(x,y):
    return x+y