import pytest
from pyraceview.messages import MsgHeartbeat


raw = b'\xab\xcd\x06\xdc\x00\x00H'


@pytest.fixture
def msg_heartbeat():
    return MsgHeartbeat(raw)


def test_header(msg_heartbeat):
    header = msg_heartbeat.header
    assert (
        header.sync == 43981
        and header.clock == 1756
        and header.size == 0
        and header.byte_type == "H"
    )
