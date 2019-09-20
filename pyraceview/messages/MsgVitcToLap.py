from numpy import uint32
from ..util import BitBuffer, ByteArray


START_LAP_BITS = uint32(12)
NUM_ENTRIES_BITS = uint32(12)
RESERVED_BITS = uint32(8)
TIMECODE_BITS = uint32(17)
FLAG_BITS = uint32(3)


class MsgVitcToLap(object):
    def __init__(self, msg_bytes):
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self.start_idx = int(bit_buffer.get_bits(START_LAP_BITS))
        self.num_lap_entries = int(bit_buffer.get_bits(NUM_ENTRIES_BITS))

        bit_buffer.get_bits(RESERVED_BITS)

        self.timecode_indices = []
        self.flags = []

        for _ in range(self.num_lap_entries):
            self.timecode_indices.append(int(bit_buffer.get_bits(TIMECODE_BITS)))
            self.flags.append(int(bit_buffer.get_bits(FLAG_BITS)))
