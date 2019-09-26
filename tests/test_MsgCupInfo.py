import pytest
from pyraceview.messages import MsgCupInfo


raw = (
    b"\xab\xcd\x00\x00\x00tCd&\x01\x00\x00\x02?\x18\x04@P"
    b"\x06\x0f\xf0\x08@\xf8\x0c?X\x10\x0cH\x12@H\x14?\x88"
    b'\x16@@\x18?\xb8\x1a\x0ep\x1c>\xe0\x1e\x00\x00"\x0f'
    b"\xa0$@x&A\x10(>\xb8*\x12\xb0,@\xd80?\xc06\x028@\t"
    b"\x98D\n\x88H\x08\x98J\x11\xe8L\t`R\x15\x00T?\xe0V"
    b"\x0bh^\x0b``\x13\xd8f\x00Ph\x00\x00j\x00\x00\x9a\x02"
    b"\xd0\xb0?\xa8\xbe\x0f\xb0"
)


@pytest.fixture
def msg_cup_info():
    return MsgCupInfo(raw)


def test_header(msg_cup_info):
    header = msg_cup_info.header
    assert (
        header.sync == 43981
        and header.clock == 0
        and header.size == 116
        and header.byte_type == "C"
    )


def test_lap(msg_cup_info):
    assert msg_cup_info.lap == 400


def test_num_cars(msg_cup_info):
    assert msg_cup_info.num_cars == 38
