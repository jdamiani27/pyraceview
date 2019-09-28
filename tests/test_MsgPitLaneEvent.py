import pytest
from pyraceview.messages import MsgPitLaneEvent


raw = b"\xab\xcd\x00\x00\x00\x03P\x0c\x07\x03"


@pytest.fixture
def msg_pit_lane_event():
    return MsgPitLaneEvent(raw)


def test_header(msg_pit_lane_event):
    header = msg_pit_lane_event.header
    assert (
        header.sync == 43981
        and header.clock == 0
        and header.size == 3
        and header.byte_type == "P"
    )


def test_car_id(msg_pit_lane_event):
    assert msg_pit_lane_event.car_id == 12


def test_event_id(msg_pit_lane_event):
    assert msg_pit_lane_event.event_id == 7
