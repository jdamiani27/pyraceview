![pyraceview](pyraceview_logo.png)

PyRaceview is a package for parsing messages used to power [NASCAR Raceview](https://www.nascar.com/raceview).  From these messages, detailed data such as GPS position, throttle, and steering input can be extracted.

Currently, PyRaceview does not provide client code to retrieve raw data from the Raceview websocket, but may in a future release.

## Requirements

Python 3.7+

## Installation

```
pip install pyraceview
```

## Example


Each Raceview message starts with a 7-byte header containing some metadata


```python
>>> from pyraceview.messages import MsgHeader
>>> msg_raw = (b'\xab\xcd\x00\x00\x01\xe5W(\x03\x1e\x9e\xb4\x01\xf9L\x83h\xc0\xcc\xf0\x12\xff\x00\x00\x02\xf8\x83\xc3#\xf0\xcd\x10\x0e\xff`'
               b'\x00\x04\xf9\xa8\x03\x86P\xcc\xf0\x14\xff\x00\x00\x06\xf8\x0f\xc2\xfc0\xcd\x10\x0c\xff@\x00\x08\xf7Z\xc2\xbeP\xcd0\x12\xff'
               b'\x00\x00\x0c\xf8m\xc3\x1c \xcd\x10\x0c\xff@\x00\x0e\xf9d\x03pP\xcc\xf0\x12\xff\x00\x00\x12\xf7.B\xaf \xcd0\x14\xff\x00\x00'
               b'\x14\xfaV\x03\xaa\xf0\xcd\xb0\n\xff@\x00\x16\xf7\x03B\xa0@\xcd0\x12\xff\x00\x00\x18\xf7\x18\x82\xa7\xa0\xcd0\x14\xff\x00\x00'
               b'\x1a\xf8\xf3\x83J\x00\xcc\xf0\x10\xff \x00\x1c\xf7\xb6\x02\xdd0\xcd0\x0e\xff \x00"\xf7\x9e\x82\xd5\x00\xcd0\x10\xff \x00$\xf7'
               b'\xe4\xc2\xed\x00\xcd\x10\x0e\xff \x00&\xf8V\x83\x14\x10\xcd\x10\x0c\xff@\x00(\xf7\x87B\xcc\xf0\xcd0\x10\xff \x00*\xf8>\x83\x0c@'
               b'\xcd\x10\x0c\xff@\x00,\xf7D\xc2\xb6\xb0\xcd0\x12\xff\x00\x00.\xf9\xfb\x83\x9b\xa0\xcd\x10\x14\xfe\xe0\x000\xf9\xdc\x03\x95\x10'
               b'\xcc\xf0\x14\xfe\xe0\x00>\xf7\xf9\xc2\xf4\xf0\xcd\x10\x0c\xff@\x00@\xfa7C\xa5\xf0\xcd\x90\x1b\x00\x00\x00D\xf8\xdd\x83BP\xcc'
               b'\xf0\x10\xff \x00J\xf8\xc6\x03;\x10\xcc\xf0\x10\xff \x00L\xf8(C\x04`\xcd\x10\x0c\xff@\x00R\xf7\xcdB\xe50\xcd\x10\x0e\xff \x00T'
               b'\xfaw\x83\xaf\xa0\xcd\xb0\x0c\xff`\x00V\xf7r\x02\xc6\x10\xcd0\x12\xff\x00\x00^\xf8\x9a\xc3+0\xcd\x10\x0e\xff \x00`\xfa\x1b\x03\xa1@'
               b'\xcd0\x1b\x00\x00\x00f\xf9yCw\x80\xcc\xf0\x12\xff\x00\x00|\xf9\x1e\x83X\xb0\xcc\xf0\x10\xff \x00\x84\xfa\xb8\xc3\xb9\xc0\xcd\xd0\x08'
               b'\xfe\xe0\x00\x90\xf9\xc1C\x8d\xb0\xcc\xf0\x14\xff\x00\x00\x9c\xf9\x08\x83Qp\xcc\xf0\x10\xff \x00\xb0\xf6\xed\x82\x98\xc0\xcd0\x12'
               b'\xff\x00\x00\xb8\xfa\x97C\xb4P\xcd\xd0\x0e\xff@\x00\xbe\xf95C`p\xcc\xf0\x12\xff\x00\x00\xc0\xf9\x91C\x7f`\xcc\xf0\x14\xff\x00\x00')
>>> hdr = MsgHeader(msg_raw)
>>> print(hdr)
Sync: 43981, Clock: 0, Size: 485, Type: W
```

In order to parse the entire message, we must use the header to lookup the correct message parser

```python
>>> from pyraceview.messages import _parsers
>>> _parsers
{'a': pyraceview.messages.MsgCarStats.MsgCarStats,
 'b': pyraceview.messages.MsgPitLaneExtended.MsgPitLaneExtended,
 'd': pyraceview.messages.MsgPitLaneExtended.MsgPitLaneExtended,
 'C': pyraceview.messages.MsgCupInfo.MsgCupInfo,
 'F': pyraceview.messages.MsgPitWindow.MsgPitWindow,
 'l': pyraceview.messages.MsgLapInfo.MsgLapInfo,
 'O': pyraceview.messages.MsgTrackConfig.MsgTrackConfig,
 'P': pyraceview.messages.MsgPitLaneEvent.MsgPitLaneEvent,
 's': pyraceview.messages.MsgRaceStatus.MsgRaceStatus,
 'V': pyraceview.messages.MsgVitcToLap.MsgVitcToLap,
 'W': pyraceview.messages.MsgCarPosition.MsgCarPosition}
>>> parser = _parsers[hdr.byte_type]
>>> msg = parser(msg_raw)
>>> msg
<pyraceview.messages.MsgCarPosition.MsgCarPosition at 0x117763550>
```

Messages, such as `MsgCarPosition`, have attributes with metadata about the message

```python
>>> msg.num_cars
40
>>> msg.timecode
52338356
```

Additionally, some messages contain a list of data per car

```python
>>> len(msg.car_data)
40
>>> type(msg.car_data[0])
pyraceview.percar.PerCarPositionData.PerCarPositionData
```

Classes containing data per car, such as `PerCarPositionData`, will have an integer `car_id` attribute

```python
>>> car_0 = msg.car_data[0]
>>> car_0.car_id
1
```

To properly identify a car by "number", Raceview uses an algorithm to convert the integer `car_id` to a string value.  In this case, id of value 1 is the '00', a valid NASCAR car number

```python
>>> from pyraceview.util import id_to_num
>>> id_to_num(car_0.car_id)
'00'
```

`PerCarPositionData` also contains the GPS position of the car

```python
>>> car_0.pos_x, car_0.pos_y, car_0.pos_z
(-686.2, 1396.4, 81.95)
```

To automatically parse many messages (e.g. as read from a websocket or from a file), PyRaceview provides the `MsgFactory` class which contains an internal buffer

```python
>>> from pyraceview.messages import MsgFactory
>>> msg_raw = (b'\xab\xcd\x00\x00\x01\x95a\x03\x1egH(\xb0\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x16\x00\x0e\x00\x00\x00\x00\x00\x00\x00'
               b'\x18\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x12\x00\x0e\x00\x00\x00\x00\x00\x00\x00,\x00\x0e\x00\x00\x00\x00\x00\x00\x00'
               b'\x08\x00\x15\x00\x00\x00\x00\x00\x00\x00V\x00\x07\x00\x00\x00\x00\x00\x00\x00(\x00\x0e\x00\x00\x00\x00\x00\x00\x00"\x00'
               b'\x07\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x15\x00\x00\x00\x00\x00\x00\x00R\x00\x0e\x00\x00\x00\x00\x00\x00\x00$\x00\x0e'
               b'\x00\x00\x00\x00\x00\x00\x00>\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x06\x00\x0e\x00\x00\x00\x00\x00\x00\x00L\x00\x0e\x00'
               b'\x00\x00\x00\x00\x00\x00*\x00\x0e\x00\x00\x00\x00\x00\x00\x00&\x00\x15\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x07\x00\x00'
               b'\x00\x00\x00\x00\x00\x02\x00\x07\x00\x00\x00\x00\x00\x00\x00^\x00\x0e\x00\x00\x00\x00\x00\x00\x00J\x00\x0e\x00\x00\x00'
               b'\x00\x00\x00\x00D\x00\x07\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x9c\x00\x0e\x00\x00\x00'
               b'\x00\x00\x00\x00|\x00\x0e\x00\x00\x00\x00\x00\x00\x00\xbe\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x01\x00\x15\x00\x00\x00'
               b'\x00\x00\x00\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00f\x00\x1b\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x15\x00\x00\x00'
               b'\x00\x00\x00\x00\x04\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x90\x00\x07\x00\x00\x00\x00\x00\x00\x000\x00\x0e\x00\x00\x00'
               b'\x00\x00\x00\x00.\x00\x0e\x00\x00\x00\x00\x00\x00\x00`\x00\x0e\x00\x00\x00\x00\x00\x00\x00@\x00\x0e\x00\x00\x00\x00\x00'
               b'\x00\x00\x14\x00\x15\x00\x00\x00\x00\x00\x00\x00T\x00\x1b\x00\x00\x00\x00\x00\x00\x00\xb8\x00\x0e\x00\x00\x00\x00\x00'
               b'\x00\x00\x84\x00\x0e\x00\x00\x00\x00\x00\x00\x00\xab\xcd\x00\x00\x00zC2(\x01\x00\x00\x02\x00\x00\x04\x00\x00\x06\x00'
               b'\x00\x08\x00\x00\x0c\x00\x00\x0e\x00\x00\x12\x00\x00\x14\x00\x00\x16\x00\x00\x18\x00\x00\x1a\x00\x00\x1c\x00\x00"\x00'
               b'\x00$\x00\x00&\x00\x00(\x00\x00*\x00\x00,\x00\x00.\x00\x000\x00\x00>\x00\x00@\x00\x00D\x00\x00J\x00\x00L\x00\x00R\x00'
               b'\x00T\x00\x00V\x00\x00^\x00\x00`\x00\x00f\x00\x00|\x00\x00\x84\x00\x00\x90\x00\x00\x9c\x00\x00\xb0\x00\x00\xb8\x00\x00'
               b'\xbe\x00\x00\xc0\x00\x00\xab\xcd\x00\x02\x00\x14O\x00\t\xad~\x00\x1a\xe9\x08\xff\xff\xff\xcadaytona\x00')
>>> factory = MsgFactory(msg_raw)
>>> factory.has_message()
True
```

Read all the messages that were pushed to the factory

```python
>>> while factory.has_message():
>>>     print(factory.get_message())
<pyraceview.messages.MsgCarStats.MsgCarStats object at 0x11777f400>
<pyraceview.messages.MsgCupInfo.MsgCupInfo object at 0x11777f4a8>
<pyraceview.messages.MsgTrackConfig.MsgTrackConfig object at 0x11777f550>
```

Push more data

```python
>>> factory.push_data(b'\xab\xcd\x00\x00\x01\xd9W\'\x03\x1ejg\x01\xf9L\x83h\xc0\xcc\xf0\x12\xff\x00\x00\x02\xf8\x83\xc3#\xf0\xcd\x10'
                      b'\x0e\xff`\x00\x04\xf9\xa8\x03\x86P\xcc\xf0\x14\xff\x00\x00\x08\xf7Z\xc2\xbeP\xcd0\x12\xff\x00\x00\x0c\xf8m\xc3'
                      b'\x1c \xcd\x10\x0c\xff@\x00\x0e\xf9d\x03pP\xcc\xf0\x12\xff\x00\x00\x12\xf7.B\xaf \xcd0\x14\xff\x00\x00\x14\xfaV'
                      b'\x03\xaa\xf0\xcd\xb0\n\xff@\x00\x16\xf7\x03B\xa0@\xcd0\x12\xff\x00\x00\x18\xf7\x18\x82\xa7\xa0\xcd0\x14\xff\x00'
                      b'\x00\x1a\xf8\xf3\x83J\x00\xcc\xf0\x10\xff \x00\x1c\xf7\xb6\x02\xdd0\xcd0\x0e\xff \x00"\xf7\x9e\x82\xd5\x00\xcd0'
                      b'\x10\xff \x00$\xf7\xe4\xc2\xed\x00\xcd\x10\x0e\xff \x00&\xf8V\x83\x14\x10\xcd\x10\x0c\xff@\x00(\xf7\x87B\xcc\xf0'
                      b'\xcd0\x10\xff \x00*\xf8>\x83\x0c@\xcd\x10\x0c\xff@\x00,\xf7D\xc2\xb6\xb0\xcd0\x12\xff\x00\x00.\xf9\xfb\x83\x9b'
                      b'\xa0\xcd\x10\x14\xfe\xe0\x000\xf9\xdc\x03\x95\x10\xcc\xf0\x14\xfe\xe0\x00>\xf7\xf9\x82\xf4\xe0\xcd\x10\x0c\xff@'
                      b'\x00@\xfa7C\xa5\xf0\xcd\x90\x1b\x00\x00\x00D\xf8\xdd\x83BP\xcc\xf0\x10\xff \x00J\xf8\xc6\x03;\x10\xcc\xf0\x10'
                      b'\xff \x00L\xf8(C\x04`\xcd\x10\x0c\xff@\x00R\xf7\xcdB\xe50\xcd\x10\x0e\xff \x00T\xfaw\x83\xaf\xa0\xcd\xb0\x0c\xff`'
                      b'\x00V\xf7r\x02\xc6\x10\xcd0\x12\xff\x00\x00^\xf8\x9a\xc3+0\xcd\x10\x0e\xff \x00`\xfa\x1b\x03\xa1@\xcd0\x1b\x00'
                      b'\x00\x00f\xf9y\x03w\x80\xcc\xf0\x12\xff\x00\x00|\xf9\x1e\x83X\xb0\xcc\xf0\x10\xff \x00\x84\xfa\xb8\xc3\xb9\xc0'
                      b'\xcd\xd0\x08\xfe\xe0\x00\x90\xf9\xc1C\x8d\xb0\xcc\xf0\x14\xff\x00\x00\x9c\xf9\x08\x83Qp\xcc\xf0\x10\xff \x00\xb0'
                      b'\xf6\xed\x82\x98\xc0\xcd0\x12\xff\x00\x00\xb8\xfa\x97C\xb4P\xcd\xd0\x0e\xff@\x00\xbe\xf95C`p\xcc\xf0\x12\xff\x00'
                      b'\x00\xc0\xf9\x91C\x7f`\xcc\xf0\x14\xff\x00\x00')
>>> factory.get_message()
<pyraceview.messages.MsgCarPosition.MsgCarPosition at 0x11777f6a0>
```
