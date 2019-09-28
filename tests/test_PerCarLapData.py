import pytest
from pyraceview.messages import MsgLapInfo


raw = (
    b"\xab\xcdAz\x00.l\x04\xbd\xba\xfeND\x04\x0c\x87"
    b"\xc8\x08\x0b\xd1\xe1[,\x00K\x88\x1c\x0b\xfe"
    b"\x01_(\x003\xcaR\x0b\xc6\xe1a|\x00\x03\x89\xb0"
    b"\x0b\xae\xa1e\xf4\x00\x00\x1a"
)


@pytest.fixture
def car():
    return MsgLapInfo(raw).car_data[-1]


def test_car_id(car):
    assert car.car_id == 176


def test_last_lap_time(car):
    assert car.last_lap_time == 23925


def test_fastest_lap_time(car):
    assert car.fastest_lap_time == 22909


def test_laps_led(car):
    assert car.laps_led == 0


def test_laps_in_top_10(car):
    assert car.laps_in_top_10 == 0


def test_rank(car):
    assert car.rank == 26
