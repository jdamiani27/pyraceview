from ..messages import MsgBase
from ..util import BitBuffer, ByteArray
from dataclasses import dataclass
from typing import List


START_LAP_BITS = 12
NUM_LAP_ENTRIES_BITS = 12
RESERVED_BITS = 8
TIMECODE_INDICES_BITS = 17
FLAGS_BITS = 3


@dataclass
class MsgVitcToLap(MsgBase):
    start_idx: int
    num_lap_entries: int
    timecode_indices: List[int]
    flags: List[int]

    def __init__(self, msg_bytes: bytes):
        super().__init__(msg_bytes)
        
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self.start_idx = int(bit_buffer.get_bits(START_LAP_BITS))
        self.num_lap_entries = int(bit_buffer.get_bits(NUM_LAP_ENTRIES_BITS))

        bit_buffer.get_bits(RESERVED_BITS)

        self.timecode_indices = []
        self.flags = []

        for _ in range(self.num_lap_entries):
            self.timecode_indices.append(
                int(bit_buffer.get_bits(TIMECODE_INDICES_BITS))
            )
            self.flags.append(int(bit_buffer.get_bits(FLAGS_BITS)))
