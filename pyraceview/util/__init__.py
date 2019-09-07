from .BitBuffer import BitBuffer
from .ByteArray import ByteArray
from .ByteBuffer import ByteBuffer
from .Vector3D import Vector3D
from .Endian import Endian


_coordinate_mapping = {
    'daytona': 'epsg:2236',
}


def get_coord_system(track_name):
    return _coordinate_mapping[track_name]


def id_to_num(car_id):
    if car_id % 2 == 1:
        return "0" + str(int((car_id - 1) / 2))
    else:
        return str(int(car_id / 2))
