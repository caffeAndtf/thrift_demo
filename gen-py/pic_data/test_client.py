from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import PicSim
import cv2
from ttypes import Image
import numpy as np


if __name__ == "__main__":
    transport = TSocket.TSocket("127.0.0.1", 9090)
    transport = TTransport.TBufferedTransport(transport)
    transport.open()
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    service = PicSim.Client(protocol)

    raw_img = cv2.imread("test.jpg", 1)
    w, h, c = raw_img.shape
    str = np.getbuffer(raw_img)
    try:
        ret_imgs = service.get_sim_pics(Image(data=str, width=w, height=h, channel=c))
    except Exception, e:
        print e.message

    if len(ret_imgs) > 0:
        for ret_img in ret_imgs:
            test_img = np.frombuffer(ret_img.data, dtype=np.uint8).reshape(ret_img.height, ret_img.width, ret_img.channel)
            cv2.imshow("similar_pics", test_img)
            cv2.waitKey(3000)

    transport.close()
