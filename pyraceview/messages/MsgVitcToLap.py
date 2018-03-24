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
        _loc3_ = BitBuffer(byte_array)
        _loc3_.set_position(7)
        self._start_idx = _loc3_.get_bits(self.VITCLAP_START_LAP_BITS)
        self._num_lap_entries = _loc3_.get_bits(self.VITCLAP_NUM_ENTRIES_BITS)
        _loc3_.get_bits(self.VITCLAP_RESERVED)
        _loc4_ = 0

        while _loc4_ < self._num_lap_entries:
            self._vitc_indices.append(_loc3_.get_bits(self.VITCLAP_VITC_BITS))
            self._flags.append(_loc3_.get_bits(self.VITCLAP_FLAG_BITS))
            _loc4_ += 1

    @property
    def flags(self):
        return self._flags

    @property
    def start_idx(self):
        return self._start_idx

    @property
    def vitc_indices(self):
        return self._vitc_indices
