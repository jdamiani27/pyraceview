import pytest
from pyraceview.messages import MsgRaceStatus


raw = (
    b"\xab\xcd*T\x02Cs\x04\x90\x90[3\x10\xcc\x89\xb8V\x00\x00"
    b"\x00\x05q\xe0\x03 \x00y\x86\xb9\x00\x00$\x00\x10\x10\x06"
    b"\x0e\xe8\x00\x06\x0f\x91k\xe5\x00\x00&\x00\x15\xce\x05\xb9x"
    b"\x00\x07\t\x8d^\x8d\x00\x00\x16\x00\x1c\xc2\x05\xcb\xa1\x90"
    b"\x05\xdd\x91L\xb3\x00\x00\x04\x00!\xece\xb1\xf9\x90\x07\x9f"
    b"\x91@\xe5\x00\x00(\x00%R\x05P\xc8\x00\x05G\x8d2a\x00\x00\x0c"
    b"\x00'\xe8\x05d\x01\x90\x07;\x911i\x00\x00\x08\x00+z\x05'!"
    b"\x90\x07m\x91&S\x00\x00\x12\x005\x08\x05\x1ba\x90\x07m\x91"
    b"\x00\xb5\x00\x00T\x006\xaa\x05\x00\xa8\x00\x07\xd1\x90\xfaC"
    b"\x00\x00`\x00<\x1c\x05\xa9q\x90\t/\x8c\xe8g\x00\x00\x1c\x00=>"
    b'\x053\xf1\x90\x08\x99\x90\xe2\xd3\x00\x00"\x00?(\x05jh\x00\ta'
    b"\x8c\xdb\xcf\x00\x00\x18\x00@\xa6\xe0\x00\x01\x90\x08g\x90\xd6"
    b"\xe7\x00\x00\x02\x00A\xec\xe0\x00\x00\x00\x08\x03\x8c\xd3\xc9"
    b"\x00\x00R\x00E\xde\x00\x00\x01\x90\ta\x90\xc3\xa3\x00\x00\xbe"
    b"\x00If\x00\x00\x00\x00\x08\x99\x8c\xb9\x9f\x00\x00\x14\x00p$"
    b"\x00\x00\x01\x90\x08\x99\x8c\x16\xdb\x00\x00D\x00\xbeD\x05\x95!"
    b"\x90\x07\x9e~\x04Q\x00\x00,\x00\xc1\xde\x05\xaf\xd9\x90\x084}"
    b"\xf7\xd9\x00\x00L\x00\xdc\x88\x04\x8e`\x00\x06@i\x97\x9b\x00"
    b"\x000\x10\x00\x02\x05\x8d\xa8\x00\x08\x98~\x15\x0b\x00\x00\xb0"
    b"\x10\x00\x02\x05\xda\x91\x90\x08\x98}\xf1\xc7\x00\x00\x06\x10"
    b"\x00\x02\x05\xc3\x10\x00\x05\xaa}\xeb\x9b\x00\x00\x1a\x10\x00"
    b"\x02\x85\xb4!\x90\t\xc4}\xe0\xa1\x00\x00H\x10\x00\x02\x05\xb9y"
    b"\x90\n(}\xd9\xa3\x00\x00@\x10\x00\x02\x05\xb0\xe9\x90\x08\x02m"
    b"\xca\xe7\x00\x00*\x10\x00\x02\x06\x1b\xb9\x90\t\x92}\xc0\xc7\x00"
    b"\x00\x10\x10\x00\x02\x04\x8b1\x90\x07:}\xaaE\x00\x00\x01\x10\x00"
    b"\x02\x04\xa5\xe0\x00\x06@m\x9es\x00\x00^\x10\x00\x04\x06\x02\x18"
    b"\x00\t`n\x0e{\x00\x00J\x10\x00\x04\x05\xb8a\x90\t.q\xc6\x9f\x00"
    b"\x00f\x10\x00\x06\x04\xfbY\x90\x07:}\xb2\xc3\x00\x00h\x10\x00\x08"
    b"\x04\xaeq\x93&\xa4q\xa9\xb9\x00\x00j\x10\x00\n\x05\xb9x\x00\x07"
    b"\xd0u\xfcm\x00\x006\x10\x00\x0c\x05\x7f\xc8\x00\t\xc4u\xd0\xb7"
    b"\x00\x00\x9a\x10\x00\x0c\x04\x98\x00\x00\x06@u\x8b\xdd\x00\x00"
    b"\x1e\x10\x00J\x04\xa5\xe0\x00\x04~\xc5\x92\x1d\x00\x00"
)


@pytest.fixture
def status():
    return MsgRaceStatus(raw).car_data[-1]


def test_car_id(status):
    assert status.car_id == 30


def test_status(status):
    assert status.status == 0


def test_tol_type(status):
    assert status.tol_type == 1


def test_time_off_leader(status):
    assert status.time_off_leader == 37.0


def test_event(status):
    assert status.event == 0


def test_speed(status):
    assert status.speed == 38.076


def test_throttle(status):
    assert status.throttle == 0


def test_brake(status):
    assert status.brake == 0


def test_rpm(status):
    assert status.rpm == 2300


def test_fuel(status):
    assert status.fuel == 49


def test_steer_angle(status):
    assert status.steer_angle == 0


def test_lap_fraction(status):
    assert status.lap_fraction == 0.5147