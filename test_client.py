from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import PicSim
import cv2
import numpy as np
import struct

transport = TSocket.TSocket("127.0.0.1", 9090)
transport = TTransport.TBufferedTransport(transport)

transport.open()

protocol = TBinaryProtocol.TBinaryProtocol(transport)

service = PicSim.Client(protocol)

raw_img = np.ones(900, dtype=np.uint8)

str = ""

for i in raw_img:
    print i
    str += struct.pack("B", i)

print len(str)
try:
    ret_imgs = service.get_sim_pics(str)
except Exception, e:
    print e.message

print len(ret_imgs)
ret_img = ret_imgs[0]

test_img = np.frombuffer(ret_img, dtype=np.uint8)
test_img.reshape((30, 30))
cv2.imshow("return", test_img)

cv2.waitKey(5000)

transport.close()
