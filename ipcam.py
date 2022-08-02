import cv2
import numpy as np
import urllib
url="http://192.168.52.38:8080/shot.jpg?rnd=477276"
while(True):
    imgResp=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    cv2.imshow('test',img)
    if ord('q')==cv2.waitKey(10):
        exit(0)
