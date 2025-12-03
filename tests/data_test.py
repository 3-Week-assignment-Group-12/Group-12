import os
import sys
from pathlib import Path

# ensure project root is importable
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from data.main_data_manager import Main_data
from models.player import Player
from models.team import Team
from models.tournament import Tournament
from data.data_wrapper import DataWrapper


class FakeMainData(Main_data):
    def __init__(self):
        self.playerFilePath = "players.csv"
        self.teamFilePath = "teams.csv"
        self.tournamentFilePath = "tournaments.csv"
        self.saved_player = None
        self.saved_team = None
        self.saved_tournament = None

    def get_players(self, path=None):
        return [Player(1, "P", "2000-01-01", 111, "A", "a@b.com")]

    def get_teams(self, path=None):
        return [Team(1, "T", "TG", 1, 5, [1])]

    def write_player(self, new_player):
        self.saved_player = new_player
        return True

    def write_team(self, new_team):
        self.saved_team = new_team
        return True

    def write_tournament(self, new_taurnament):
        self.saved_tournament = new_taurnament
        return True

    def get_tournaments(self, path=None):
        return [Tournament(1, "Cup", "2025-12-01", "2025-12-03", "Stadium", "Contact", "c@example.com", "555-0000", [1], [1])]

def test_get_tournaments_reads_file(tmp_path):
    csv_content = "1,MyCup,2025-12-01,2025-12-03,MainVenue,Org,org@example.com,5551111,1,2\n"
    file = tmp_path / "tournaments_test.csv"
    file.write_text(csv_content, encoding="utf-8")

    md = Main_data()
    tours = md.get_tournaments(str(file))
    assert isinstance(tours, list)
    assert len(tours) == 1
    t = tours[0]
    assert isinstance(t, Tournament)
    assert t.id == 1
    assert t.name == "MyCup"

def test_datawrapper_player_and_team_write_and_reads():
    dw = DataWrapper()
    fake = FakeMainData()
    dw.main_data = fake  # inject fake data manager

    players = dw.get_players()
    assert isinstance(players, list) and len(players) == 1
    assert isinstance(players[0], Player)

    teams = dw.get_teams()
    assert isinstance(teams, list) and len(teams) == 1
    assert isinstance(teams[0], Team)

    new_p = Player(2, "B", "1999-01-01", 222, "B addr", "b@b.com")
    assert dw.write_player(new_p) is True
    assert fake.saved_player is new_p

    new_t = Team(2, "L", "LG", 2, 6, [2])
    assert dw.write_team(new_t) is True
    assert fake.saved_team is new_t


def test_datawrapper_tournament_wrappers():
    dw = DataWrapper()
    fake = FakeMainData()
    dw.main_data = fake

    tours = dw.get_tournaments()
    assert isinstance(tours, list)
    assert tours and isinstance(tours[0], Tournament)

    new_tour = Tournament(2, "Cup2", "2026-01-01", "2026-01-02", "Hall", "Org", "org@e.com", "000", [2], [20])
    assert dw.write_tournament(new_tour) is True
    assert fake.saved_tournament is new_tour