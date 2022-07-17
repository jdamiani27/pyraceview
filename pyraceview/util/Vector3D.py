import math


class Vector3D(object):
    X_POS = 0
    Y_POS = 1
    Z_POS = 2

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self._v = [x, y, z]

    @staticmethod
    def norm(vector):
        return math.sqrt(sum(i**2 for i in vector))

    def normalize(self):
        magnitude = self.norm(self._v)
        self._v = [i / magnitude for i in self._v]

    @property
    def x(self):
        return self._v[self.X_POS]

    @x.setter
    def x(self, value):
        self._v[self.X_POS] = value

    @property
    def y(self):
        return self._v[self.Y_POS]

    @y.setter
    def y(self, value):
        self._v[self.Y_POS] = value

    @property
    def z(self):
        return self._v[self.Z_POS]

    @z.setter
    def z(self, value):
        self._v[self.Z_POS] = value
