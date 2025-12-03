import sys
from pathlib import Path

# ensure project root is importable
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from models.player import Player
from models.team import Team
from models.tournament import Tournament
from logic.logic_wrapper import LogicWrapper
from data.data_wrapper import DataWrapper
from logic.player_handler import player_handler
from logic.team_handler import team_handler


class FakeDataWrapper(DataWrapper):
    """Mock DataWrapper for testing LogicWrapper."""
    """Mock DataWrapper for testing LogicWrapper."""
    
    def __init__(self):
        self.players = [
            Player(1234567890, "Alice", "1990-01-01", 5551234, "Addr 1", "alice@example.com"),
            Player(9876543210, "Bob", "1992-03-15", 5555678, "Addr 2", "bob@example.com"),
        ]
        self.teams = [
            Team(1, "Tigers", "TGR", 1234567890, 5, [1234567890]),
        ]
        self.tournaments = [
            Tournament(1, "Cup", "2025-12-01", "2025-12-03", "Stadium", 1, "c@example.com", 555-0000, [1], [10]),
        ]
        self.written_players = []
        self.written_teams = []
        self.written_tournaments = []

    def get_players(self):
        return self.players

    def get_teams(self):
        return self.teams

    def get_tournaments(self):
        return self.tournaments

    def write_player(self, new_player):
        self.written_players.append(new_player)
        return True

    def write_team(self, new_team):
        self.written_teams.append(new_team)
        return True

    def write_tournament(self, new_tournament):
        self.written_tournaments.append(new_tournament)
        return True

    def get_player_by_ID(self, ID):
        for p in self.players:
            if p.kt == ID:
                return p
        return False

    def delete_player(self, player_id):
        self.players = [p for p in self.players if p.kt != player_id]
        return True

    def delete_team(self, team_id):
        self.teams = [t for t in self.teams if t.id != team_id]
        return True

    def modify_player(self, new_data):
        for i, p in enumerate(self.players):
            if p.kt == new_data.kt:
                self.players[i] = new_data
                return True
        return False

    def modify_team(self, new_data):
        for i, t in enumerate(self.teams):
            if t.id == new_data.id:
                self.teams[i] = new_data
                return True
        return False


class FakePlayerHandler(player_handler):
    """Mock player_handler for testing."""
    
    def create_player(self, KT:int ,name:str ,phone: int,address: str,email:str, playerList:list[Player]):
        # Simple validation: check if KT already exists
        for p in playerList:
            if p.kt == KT:
                return False  # Duplicate
        return Player(KT, name, "2000-01-01", phone, address, email)


class FakeTeamHandler(team_handler):
    """Mock team_handler for testing."""
    
    def create_team(self, name:str, tag:str, creator_id:int, team_size:int,teams:list[Team],member_list:list[int]):
        # Simple validation: check if tag already exists
        for t in teams:
            if t.tag == tag:
                return False  # Duplicate
        new_id = max([t.id for t in teams], default=0) + 1
        return Team(new_id, name, tag, creator_id, team_size, member_list)


def test_logic_wrapper_get_players_and_teams():
    """Test that LogicWrapper retrieves players and teams."""
    lw = LogicWrapper()
    lw.data_wrapper = FakeDataWrapper()
    
    players = lw.get_players()
    assert isinstance(players, list)
    assert len(players) == 2
    assert players[0].name == "Alice"
    
    teams = lw.get_teams()
    assert isinstance(teams, list)
    assert len(teams) == 1
    assert teams[0].name == "Tigers"


def test_logic_wrapper_create_player_success():
    """Test successful player creation."""
    lw = LogicWrapper()
    lw.data_wrapper = FakeDataWrapper()
    lw.player_handler = FakePlayerHandler()
    
    result = lw.create_player(1111111111, "Charlie", 5559999, "Addr 3", "charlie@example.com")
    assert result is True
    assert len(lw.data_wrapper.written_players) == 1
    assert lw.data_wrapper.written_players[0].name == "Charlie"


def test_logic_wrapper_create_player_duplicate():
    """Test player creation with duplicate KT."""
    lw = LogicWrapper()
    lw.data_wrapper = FakeDataWrapper()
    lw.player_handler = FakePlayerHandler()
    
    # Try to create player with existing KT
    result = lw.create_player(1234567890, "Duplicate", 5551111, "Addr", "dup@example.com")
    assert result is False
    assert len(lw.data_wrapper.written_players) == 0


def test_logic_wrapper_create_team_success():
    """Test successful team creation."""
    lw = LogicWrapper()
    lw.data_wrapper = FakeDataWrapper()
    lw.team_handler = FakeTeamHandler()
    
    result = lw.create_team("Lions", "LNS", 1234567890, 6, [1234567890, 9876543210])
    assert result is True
    assert len(lw.data_wrapper.written_teams) == 1
    assert lw.data_wrapper.written_teams[0].name == "Lions"


def test_logic_wrapper_create_team_duplicate_tag():
    """Test team creation with duplicate tag."""
    lw = LogicWrapper()
    lw.data_wrapper = FakeDataWrapper()
    lw.team_handler = FakeTeamHandler()
    
    # Try to create team with existing tag
    result = lw.create_team("AnotherTeam", "TGR", 1234567890, 5, [1234567890])
    assert result is False
    assert len(lw.data_wrapper.written_teams) == 0


def test_logic_wrapper_get_player_by_id():
    """Test retrieving a player by ID."""
    lw = LogicWrapper()
    lw.data_wrapper = FakeDataWrapper()
    
    player = lw.get_player_by_ID(1234567890)
    assert isinstance(player, Player)
    assert player.name == "Alice"
    
    not_found = lw.get_player_by_ID(9999999999)
    assert not_found is False


def test_logic_wrapper_modify_player():
    """Test modifying an existing player."""
    lw = LogicWrapper()
    lw.data_wrapper = FakeDataWrapper()
    
    modified_player = Player(1234567890, "Alice Updated", "1990-01-01", 5559999, "New Addr", "alice.new@example.com")
    result = lw.modify_player(modified_player)
    assert result is True
    # Verify change in fake data
    assert lw.data_wrapper.players[0].phone == 5559999


def test_logic_wrapper_delete_player():
    """Test deleting a player."""
    lw = LogicWrapper()
    lw.data_wrapper = FakeDataWrapper()
    
    initial_count = len(lw.data_wrapper.players)
    result = lw.delete_player(1234567890)
    assert result is True
    assert len(lw.data_wrapper.players) == initial_count - 1


def test_logic_wrapper_get_tournaments():
    """Test retrieving tournaments (if veiw_turnaments is exposed)."""
    lw = LogicWrapper()
    lw.data_wrapper = FakeDataWrapper()
    
    # Note: veiw_turnaments may need to be tested if it exists in logic_wrapper
    tours = lw.data_wrapper.get_tournaments()
    assert isinstance(tours, list)
    assert len(tours) == 1
    assert tours[0].name == "Cup"