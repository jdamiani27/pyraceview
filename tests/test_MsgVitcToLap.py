import pytest
from pyraceview.messages import MsgVitcToLap


raw = (
    b"\xab\xcd*V\x02\x05V\x00\x00\xcd\x00\x8b\x05\x98\xb1\x11"
    b"\x8b\x1c\x18\xb2y\x8b2\x98\xb3\xd9\x8bI\x18\xb5A\x8b_\x98"
    b"\xb6\xb1\x8bv\x18\xb8\x19\x8b\x8d\x18\xb9\x89\x8b\xa4\x18"
    b"\xba\xf9\x8b\xbb\x18\xbcq\x8b\xd2\x98\xbd\xe1\x8b\xe9\x98"
    b"\xbfY\x8c\x01\x98\xc0\xd1\x8c\x19\x18\xc2Q\x8c0\x98\xc3"
    b"\xc9\x8cH\x98\xc5A\x8c`\x18\xc6\xc1\x8cw\x98\xc89\x8c\x8f"
    b"\x98\xc9\xb9\x8c\xa7\x18\xcb1\x8c\xbf\x18\xcc\xb1\x8c\xd7"
    b"\x18\xce1\x8c\xef\x18\xcf\xb1\x8d\x07\x18\xd19\x8d\x1f\x98"
    b"\xd2\xb9\x8d8\x18\xd4A\x8dP\x18\xd5\xc1\x8dh\x18\xd7A\x8d"
    b"\x80\x98\xd8\xc9\x8d\x98\x98\xdaI\x8d\xb0\x98\xdb\xc9\x8d"
    b"\xc8\x98\xddQ\x8d\xe1\x18\xde\xd1\x8d\xf9\x18\xe0Y\x8e\x11"
    b"\x98\xe1\xd9\x8e)\x98\xe3a\x8eB\x18\xe4\xe1\x8eZ\x98\xe6i"
    b"\x8er\x98\xe7\xe9\x8e\x8b\x18\xe9q\x8e\xa3\x18\xea\xf1\x8e"
    b"\xbb\x98\xecy\x8e\xd4\x18\xee\x01\x8e\xec\x98\xef\x89\x8f"
    b"\x05\x18\xf1\x11\x8f\x1d\x98\xf2\xa1\x8f6\x98\xf41\x8fO\x18"
    b"\xf5\xb9\x8fh\x18\xf7I\x8f\x80\x98\xf8\xd1\x8f\x99\x98\xfaY"
    b'\x8f\xb2\x18\xfc"\x8f\xdb(\xff\x82\x90\x14\xa9\x03Z\x90P)'
    b"\x06\xf2\x90\x8b\x19\ti\x90\xa2\x19\n\xd1\x90\xbf)\r\x92"
    b"\x90\xf6)\x11:\x910\x99\x13\xb9\x91G\x19\x15!\x91]\x99\x16"
    b"\x89\x91t\x19\x17\xf1\x91\x8a\x99\x19a\x91\xa1\x99\x1a\xd1"
    b"\x91\xb8\x99\x1cA\x91\xcf\x99\x1d\xb9\x91\xe7\x19\x1f)\x91"
    b'\xfe\x99 \xa1\x92\x16\x19"\x19\x92-\x99#\x91\x92E\x19%\t'
    b"\x92\\\x99&\x81\x92t\x19(\x01\x92\x8c\x19)\x81\x92\xa3\x99*"
    b"\xf9\x92\xbb\x99,y\x92\xd3\x99-\xf9\x92\xeb\x99/y\x93\x03"
    b"\x990\xf9\x93\x1b\x992y\x933\x993\xf9\x93L\x195\x81\x93d\x197"
    b"\x01\x93|\x998\x89\x93\x94\x99:\t\x93\xac\x99;\x89\x93\xc5"
    b"\x19=\x11\x93\xdd\x99>\x99\x93\xf6\x19@!\x94\x0e\x99A\xa9"
    b"\x94&\x99C1\x94?\x19D\xb1\x94W\x19F9\x94o\x99G\xc1\x94\x88"
    b"\x19II\x94\xa0\x99J\xc9\x94\xb9\x19LQ\x94\xd1\x99M\xe1\x94"
    b"\xea\x19Oi\x95\x03\x19P\xf9\x95\x1b\x99R\xca\x95F)V2\x95\x7f\xa0"
)


@pytest.fixture
def msg_vitc_to_lap():
    return MsgVitcToLap(raw)


def test_header(msg_vitc_to_lap):
    header = msg_vitc_to_lap.header
    assert (
        header.sync == 43981
        and header.clock == 10838
        and header.size == 517
        and header.byte_type == "V"
    )


def test_flags(msg_vitc_to_lap):
    flags = msg_vitc_to_lap.flags
    assert flags == [
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,2,2,2,2,
    ]


def test_start_idx(msg_vitc_to_lap):
    assert msg_vitc_to_lap.start_idx == 0


def test_timecode_indices(msg_vitc_to_lap):
    timecode_indices = msg_vitc_to_lap.timecode_indices
    assert timecode_indices == [
        71179,71202,71224,71247,71269,71291,71314,71336,71359,71382,
        71404,71427,71450,71473,71496,71519,71542,71566,71589,71612,
        71635,71659,71683,71706,71730,71754,71777,71801,71825,71848,
        71872,71896,71919,71943,71967,71991,72014,72038,72062,72086,
        72110,72134,72158,72182,72206,72231,72255,72279,72304,72328,
        72352,72376,72400,72424,72449,72473,72497,72521,72545,72569,
        72593,72618,72642,72666,72690,72715,72739,72763,72787,72812,
        72836,72860,72885,72909,72933,72957,72982,73006,73030,73054,
        73079,73103,73128,73152,73177,73201,73226,73250,73275,73300,
        73325,73350,73374,73399,73424,73449,73473,73498,73523,73547,
        73572,73604,73654,73712,73769,73835,73888,73950,74006,74029,
        74052,74074,74110,74162,74220,74279,74337,74359,74382,74404,
        74427,74449,74472,74494,74517,74540,74563,74586,74609,74632,
        74655,74679,74702,74725,74749,74772,74796,74819,74843,74866,
        74890,74913,74937,74960,74984,75008,75032,75056,75079,75103,
        75127,75151,75175,75199,75223,75247,75271,75295,75319,75343,
        75367,75391,75416,75440,75464,75488,75513,75537,75561,75585,
        75609,75633,75658,75682,75707,75731,75756,75780,75805,75829,
        75853,75878,75902,75926,75950,75975,75999,76024,76048,76073,
        76097,76121,76146,76170,76195,76220,76244,76269,76294,76319,
        76343,76377,76428,76486,76543,
    ]


def test_num_lap_entries(msg_vitc_to_lap):
    assert msg_vitc_to_lap.num_lap_entries == 205
