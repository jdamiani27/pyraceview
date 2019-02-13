import numpy as np
from .messages import (MsgHeader, MsgCarStats, MsgPitLaneExtended, MsgCupInfo, #MsgPitLane,
                       MsgPitWindow, #MsgHeartbeat,
                       MsgLapInfo, MsgTrackConfig,
                       MsgPitLaneEvent, MsgRaceStatus, #MsgTicker,
                       #MsgVitcOctoTime,
                       MsgVitcToLap, MsgCarPosition,
                       #MsgDriverPerformance
                      )


_parsers = {
    "a": MsgCarStats,
    "b": MsgPitLaneExtended,
    "d": MsgPitLaneExtended,
    "C": MsgCupInfo,
    # "D": MsgPitLane,
    "F": MsgPitWindow,
    # "H": MsgHeartbeat,
    "l": MsgLapInfo,
    "O": MsgTrackConfig,
    "P": MsgPitLaneEvent,
    "s": MsgRaceStatus,
    # "T": MsgTicker,
    # "U": MsgVitcOctoTime,
    "V": MsgVitcToLap,
    "W": MsgCarPosition,
    # "z": MsgDriverPerformance
}


def read_file(path):
    """
    Load raceview data from a flat file
    Parameters
    ----------
    path : string
        File path

    Returns
    -------
    Race?
    """
    with open(path) as f:
        blob = b''.join(eval(l) for l in f)

    PREAMBLE = b'\xab\xcd'
    raw_messages = []

    i_0 = blob.find(PREAMBLE)

    while i_0 > -1:
        data_size = np.frombuffer(blob[i_0 + 4: i_0 + 6],
                                  dtype=np.dtype('>H'), count=1)[0]
        i_1 = i_0 + 7 + int(data_size)
        raw_messages.append(blob[i_0:i_1])
        i_0 = blob.find(PREAMBLE, i_1)

    return raw_messages


def parse_message(raw_bytes):
    header = MsgHeader(raw_bytes)
    return _parsers[header.byte_type](raw_bytes)
