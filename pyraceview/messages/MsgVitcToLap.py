from numpy import uint32
from ..util import BitBuffer


class MsgVitcToLap(object):
    VITCLAP_START_LAP_BITS = uint32(12)
    VITCLAP_NUM_ENTRIES_BITS = uint32(12)
    VITCLAP_RESERVED = uint32(8)
    VITCLAP_VITC_BITS = uint32(17)
    VITCLAP_FLAG_BITS = uint32(3)

    def __init__(self, msg_header, byte_array):
        self._vitc_indices = []
        self._flags = []

        bit_buffer = BitBuffer(byte_array)
        bit_buffer.set_position(7)
        self._start_idx = bit_buffer.get_bits(self.VITCLAP_START_LAP_BITS)
        self._num_lap_entries = bit_buffer.get_bits(self.VITCLAP_NUM_ENTRIES_BITS)
        bit_buffer.get_bits(self.VITCLAP_RESERVED)

        i = 0

        while i < self._num_lap_entries:
            self._vitc_indices.append(bit_buffer.get_bits(self.VITCLAP_VITC_BITS))
            self._flags.append(bit_buffer.get_bits(self.VITCLAP_FLAG_BITS))
            i += 1

    @property
    def flags(self):
        return self._flags

    @property
    def start_idx(self):
        return self._start_idx

    @property
    def vitc_indices(self):
        return self._vitc_indices
