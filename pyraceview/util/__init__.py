from .BitBuffer import BitBuffer
from .ByteArray import ByteArray
from .Vector3D import Vector3D
from .Endian import Endian


_coordinate_mapping = {
    'daytona': 'epsg:2236',
}


def get_coord_system(track_name):
    return _coordinate_mapping[track_name]
