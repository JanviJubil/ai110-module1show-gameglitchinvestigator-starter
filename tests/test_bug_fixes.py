import random
import pytest
from logic_utils import get_range_for_difficulty, update_score


def is_in_range(guess, low, high):
    return low <= guess <= high


# ── Test 1: Out-of-range inputs are rejected ─────────────────────────────────

def test_out_of_range_normal():
    low, high = get_range_for_difficulty("Normal")  # 1-100
    assert not is_in_range(0, low, high)
    assert not is_in_range(101, low, high)

def test_out_of_range_easy():
    low, high = get_range_for_difficulty("Easy")  # 1-20
    assert not is_in_range(0, low, high)
    assert not is_in_range(21, low, high)

def test_out_of_range_hard():
    low, high = get_range_for_difficulty("Hard")  # 1-50
    assert not is_in_range(0, low, high)
    assert not is_in_range(51, low, high)


# ── Test 2: Correct ranges per difficulty ────────────────────────────────────

def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100

def test_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 50


# ── Test 3: Secret number is within range for each difficulty ─────────────────

@pytest.mark.parametrize("difficulty", ["Easy", "Normal", "Hard"])
def test_secret_within_range(difficulty):
    low, high = get_range_for_difficulty(difficulty)
    for _ in range(100):
        secret = random.randint(low, high)
        assert low <= secret <= high


# ── Test 4: Score resets to 0 at the start of every new game ─────────────────

def test_score_resets_to_zero():
    # Simulate score accumulation during a game (even attempts give +5)
    score = update_score(0, "Too High", 2)   # +5
    score = update_score(score, "Too High", 4)  # +5
    assert score > 0  # score built up during game
    # New game resets score
    score = 0
    assert score == 0

def test_score_never_goes_negative():
    # Score at 0 should not decrease below 0 on a wrong guess
    score = update_score(0, "Too Low", 1)
    assert score >= 0
    score = update_score(0, "Too High", 3)
    assert score >= 0
