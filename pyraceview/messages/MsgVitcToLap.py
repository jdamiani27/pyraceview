from numpy import uint32
from ..util import BitBuffer, ByteArray


VITCLAP_START_LAP_BITS = uint32(12)
VITCLAP_NUM_ENTRIES_BITS = uint32(12)
VITCLAP_RESERVED = uint32(8)
VITCLAP_VITC_BITS = uint32(17)
VITCLAP_FLAG_BITS = uint32(3)


class MsgVitcToLap(object):
    def __init__(self, msg_bytes):
        self.vitc_indices = []
        self.flags = []

        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)
        self.start_idx = int(bit_buffer.get_bits(VITCLAP_START_LAP_BITS))
        self.num_lap_entries = int(bit_buffer.get_bits(VITCLAP_NUM_ENTRIES_BITS))
        bit_buffer.get_bits(VITCLAP_RESERVED)

        for _ in range(self.num_lap_entries):
            self.vitc_indices.append(int(bit_buffer.get_bits(VITCLAP_VITC_BITS)))
            self.flags.append(int(bit_buffer.get_bits(VITCLAP_FLAG_BITS)))
