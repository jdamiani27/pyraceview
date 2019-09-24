from numpy import uint32
from ..messages import MsgBase
from ..util import BitBuffer, ByteArray


START_LAP_BITS = uint32(12)
NUM_LAP_ENTRIES_BITS = uint32(12)
RESERVED_BITS = uint32(8)
TIMECODE_INDICES_BITS = uint32(17)
FLAGS_BITS = uint32(3)


class MsgVitcToLap(MsgBase):
    def __init__(self, msg_bytes):
        super().__init__(msg_bytes)
        
        bit_buffer = BitBuffer(ByteArray(msg_bytes))
        bit_buffer.set_position(7)

        self._start_idx = int(bit_buffer.get_bits(START_LAP_BITS))
        self._num_lap_entries = int(bit_buffer.get_bits(NUM_LAP_ENTRIES_BITS))

        bit_buffer.get_bits(RESERVED_BITS)

        self._timecode_indices = []
        self._flags = []

        for _ in range(self._num_lap_entries):
            self._timecode_indices.append(
                int(bit_buffer.get_bits(TIMECODE_INDICES_BITS))
            )
            self._flags.append(int(bit_buffer.get_bits(FLAGS_BITS)))

    @property
    def flags(self):
        return self._flags

    @property
    def start_idx(self):
        return self._start_idx

    @property
    def timecode_indices(self):
        return self._timecode_indices

    @property
    def num_lap_entries(self):
        return self._num_lap_entries
