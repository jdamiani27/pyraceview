import pytest
from pyraceview.messages import MsgPitWindow


raw = (
    b"\xab\xcd\x06\xcc\x00\x99F&\x01\x07pw\x02\x07pw\x04\x07pw\x06"
    b"\x07pw\x08\x07pw\x0c\x07pw\x10\x07pw\x12\x07pw\x14\x07pw\x16"
    b'\x07pw\x18\x07pw\x1a\x07pw\x1c\x07pw\x1e\x07\x80x"\x07pw$\x07pw&'
    b"\x07pw(\x07pw*\x07pw,\x07pw0\x07pw6\x07\x80x@\x07pwD\x07pwH"
    b"\x07pwJ\x07pwL\x07pwR\x07pwT\x07pwV\x07pw^\x07pw`\x07pwf\x07"
    b"\x80xh\x07\x80xj\x07\x80x\x9a\x07\x80x\xb0\x07pw\xbe\x07pw"
)


@pytest.fixture
def car():
    return MsgPitWindow(raw).car_data[-1]


def test_car_id(car):
    assert car.car_id == 190


def test_low(car):
    assert car.low == 119


def test_high(car):
    assert car.high == 119
