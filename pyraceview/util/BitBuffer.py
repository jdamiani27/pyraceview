from numpy import uint32, int32


class BitBuffer(object):

    def __init__(self, byte_array):
        self.buffer = byte_array
        self.bit_position = uint32(0)

    def extract_bits_from_byte(self, param1, param2, param3):
        _loc4_ = 255 >> 8 - param3
        _loc5_ = param1
        _loc5_ = _loc5_ >> 8 - param2 - param3
        _loc5_ = _loc5_ & _loc4_
        return _loc5_

    @staticmethod
    def make_bits_signed(param1, param2):
        _loc3_ = int32(param1 << 32 - param2) >> 32 - param2
        return _loc3_

    def set_position(self, position):
        self.buffer.position = position

    def get_bits(self, param1):
        _loc3_ = 0
        _loc4_ = 0
        _loc5_ = 0
        _loc2_ = 0

        if self.bit_position != 0:
            _loc3_ = uint32(min(8 - self.bit_position, param1))
            _loc4_ = uint32(self.extract_bits_from_byte(self.current_byte, self.bit_position, _loc3_))
            _loc2_ = uint32(_loc2_ | _loc4_)
            self.bit_position = self.bit_position + _loc3_
            self.bit_position = self.bit_position % 8
            param1 = param1 - _loc3_

        while param1 >= 8:
            self.current_byte = 255 & self.buffer.read_unsigned_byte()

            _loc2_ = uint32(_loc2_ << 8 | self.current_byte)
            param1 = param1 - 8

        if param1 > 0:
            self.current_byte = 255 & self.buffer.read_unsigned_byte()

            _loc5_ = uint32(self.extract_bits_from_byte(self.current_byte, 0, param1))
            _loc2_ = uint32(_loc2_ << param1 | _loc5_)
            self.bit_position = self.bit_position + param1
            param1 = 0

        return _loc2_
