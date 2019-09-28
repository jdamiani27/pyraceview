import pytest
from pyraceview.messages import MsgTrackConfig


raw = b"\xab\xcdAb\x00\x14O\x00\xb3\xfe \x009\x15]\x00\x00\x00Urichmond"


@pytest.fixture
def msg_track_config():
    return MsgTrackConfig(raw)


def test_header(msg_track_config):
    header = msg_track_config.header
    assert (
        header.sync == 43981
        and header.clock == 16738
        and header.size == 20
        and header.byte_type == "O"
    )


def test_local_origin_x(msg_track_config):
    assert msg_track_config.local_origin_x == 11796000


def test_local_origin_y(msg_track_config):
    assert msg_track_config.local_origin_y == 3741021


def test_local_origin_z(msg_track_config):
    assert msg_track_config.local_origin_z == 85


def test_track_name(msg_track_config):
    assert msg_track_config.track_name == "richmond"
