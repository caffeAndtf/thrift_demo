#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class Image(object):
    """
    Attributes:
     - data
     - width
     - height
     - channel
    """


    def __init__(self, data=None, width=None, height=None, channel=None,):
        self.data = data
        self.width = width
        self.height = height
        self.channel = channel

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.data = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.width = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.height = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.channel = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Image')
        if self.data is not None:
            oprot.writeFieldBegin('data', TType.STRING, 1)
            oprot.writeBinary(self.data)
            oprot.writeFieldEnd()
        if self.width is not None:
            oprot.writeFieldBegin('width', TType.I32, 2)
            oprot.writeI32(self.width)
            oprot.writeFieldEnd()
        if self.height is not None:
            oprot.writeFieldBegin('height', TType.I32, 3)
            oprot.writeI32(self.height)
            oprot.writeFieldEnd()
        if self.channel is not None:
            oprot.writeFieldBegin('channel', TType.I32, 4)
            oprot.writeI32(self.channel)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Image)
Image.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'data', 'BINARY', None, ),  # 1
    (2, TType.I32, 'width', None, None, ),  # 2
    (3, TType.I32, 'height', None, None, ),  # 3
    (4, TType.I32, 'channel', None, None, ),  # 4
)
fix_spec(all_structs)
del all_structs
