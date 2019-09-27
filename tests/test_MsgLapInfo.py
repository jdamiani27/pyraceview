import pytest
from pyraceview.messages import MsgLapInfo


raw = (
    b"\xab\xcdAz\x00.l\x04\xbd\xba\xfeND\x04\x0c\x87"
    b"\xc8\x08\x0b\xd1\xe1[,\x00K\x88\x1c\x0b\xfe"
    b"\x01_(\x003\xcaR\x0b\xc6\xe1a|\x00\x03\x89\xb0"
    b"\x0b\xae\xa1e\xf4\x00\x00\x1a"
)


@pytest.fixture
def msg_lap_info():
    return MsgLapInfo(raw)


def test_lap(msg_lap_info):
    assert msg_lap_info.lap == 313


def test_num_cautions(msg_lap_info):
    assert msg_lap_info.num_cautions == 4


def test_last_flag_change_lap(msg_lap_info):
    assert msg_lap_info.last_flag_change_lap == 249


def test_num_leaders(msg_lap_info):
    assert msg_lap_info.num_leaders == 3


def test_lead_changes(msg_lap_info):
    assert msg_lap_info.lead_changes == 4


def test_timecode(msg_lap_info):
    assert msg_lap_info.timecode == 79543038


def test_num_cars(msg_lap_info):
    assert msg_lap_info.num_cars == 4
