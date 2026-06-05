import pytest
import sys
import os
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)
from parking_logic import ( 
    calculate_distance,
    get_direction,
    parking_status
)


def test_calculate_distance():
    distance = calculate_distance(
        600, 620,
        900, 280
    )

    assert distance > 0


def test_turn_right():
    direction = get_direction(
        600,
        900
    )

    assert direction == "TURN RIGHT"


def test_turn_left():
    direction = get_direction(
        950,
        900
    )

    assert direction == "TURN LEFT"


def test_straight():
    direction = get_direction(
        900,
        900
    )

    assert direction == "STRAIGHT"


def test_searching_status():
    assert parking_status(300) == "SEARCHING"


def test_slow_down_status():
    assert parking_status(100) == "SLOW DOWN"


def test_parked_status():
    assert parking_status(30) == "PARKED"