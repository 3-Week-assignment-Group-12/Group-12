import sys
from pathlib import Path

# ensure project root is importable
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from models.player import Player
from models.team import Team
from models.tournament import Tournament


def test_player_to_csv_and_str():
    p = Player(1234567890, "Alice Example", "1990-01-01", 5551234, "Addr 1", "a@example.com")
    assert p.toCSVList() == [1234567890, "Alice Example", "1990-01-01", 5551234, "Addr 1", "a@example.com"]
    s = str(p)
    assert "Alice Example" in s and "1234567890" in s


def test_team_to_csv_and_factory():
    t = Team(1, "Tigers", "TGR", 1234567890, 5, [123, 456])
    assert t.toCSVList() == ["Tigers", "TGR", 1234567890, 5, [123, 456]]
    t2 = t.create_team(2, "Lions", "LNS", 9876543210, 6, [789])
    assert isinstance(t2, Team)
    assert t2.id == 2
    assert "Tigers" in str(t)


def test_tournament_to_csv_and_str():
    # use simple values; tests don't enforce date type to avoid coupling to implementation
    tour = Tournament(1, "Cup", "2025-12-01", "2025-12-03", "Stadium", "Contact", "c@example.com", "555-0000", [1, 2], [10, 11])
    csv = tour.toCSVList()
    assert csv[0] == 1
    assert csv[4] == "Stadium"
    assert csv[-2] == [1, 2] or csv[-1] == [10, 11]
    assert "Cup" in str(tour)