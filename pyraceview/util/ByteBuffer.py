class ByteBuffer(object):
    
    def __init__(self, source=b""):
        self._buffer = bytearray(source)
        
    def read(self, size=-1):
        if size == -1:
            result = self._buffer[:]
            del self._buffer[:]
        else:
            result = self._buffer[:size]
            del self._buffer[:size]
            
        return result
    
    def peek(self, size):
        return self._buffer[:size]
    
    def write(self, b):
        self._buffer += b
        
    def size(self):
        return len(self._buffer)