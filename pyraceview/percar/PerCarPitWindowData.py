class PerCarPitWindowData(object):

    def __init__(self, param1:int, param2:int, param3:int):
        self._id = param1
        self._low = param2
        self._high = param3

    @property
    def id(self):
        return self._id

    @property
    def low(self):
        return self._low

    @property
    def high(self):
        return self._high
