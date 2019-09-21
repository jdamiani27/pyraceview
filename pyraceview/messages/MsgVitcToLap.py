from numpy import uint32
from ..util import BitBuffer, ByteArray


VITCLAP_START_LAP_BITS = uint32(12)
VITCLAP_NUM_ENTRIES_BITS = uint32(12)
VITCLAP_RESERVED = uint32(8)
VITCLAP_VITC_BITS = uint32(17)
VITCLAP_FLAG_BITS = uint32(3)


class MsgVitcToLap(object):
    def __init__(self, msg_bytes):
        self._vitc_indices = []
        self._flags = []

        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)
        self._start_idx = int(bit_buffer.get_bits(VITCLAP_START_LAP_BITS))
        self._num_lap_entries = int(bit_buffer.get_bits(VITCLAP_NUM_ENTRIES_BITS))
        bit_buffer.get_bits(VITCLAP_RESERVED)

        for _ in range(self._num_lap_entries):
            self._vitc_indices.append(int(bit_buffer.get_bits(VITCLAP_VITC_BITS)))
            self._flags.append(int(bit_buffer.get_bits(VITCLAP_FLAG_BITS)))

    @property
    def flags(self):
        return self._flags

    @property
    def start_idx(self):
        return self._start_idx

    @property
    def vitc_indices(self):
        return self._vitc_indices
