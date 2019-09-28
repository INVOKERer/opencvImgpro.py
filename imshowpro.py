from PIL import Image
import numpy as np
import cv2
import math
from spectral import *


# hsv
def imgDo(imgOri):
    img_BGR = cv2.imread(r'E:\HE+CAM5\roi1\{a}'.format(a=imgOri))
    bgr = np.asarray(img_BGR)
    (m, n) = bgr.shape[:2]
    # b = bgr[..., 0]
    # g = bgr[..., 1]
    r = bgr[..., 2]
    img_hsv = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
    for i in range(m):
        for j in range(n):
            if r[i, j] >= 30 and 0 < img_hsv[i, j, 0] <= 32:
                img_hsv[i, j, 0] = img_hsv[i, j, 0] + 148  # img_hsv[i, j, 0] + 148
                img_hsv[i, j, 1] = img_hsv[i, j, 1] / 2  # img_hsv[i, j, 1]/2
                img_hsv[i, j, 2] = img_hsv[i, j, 2] / 2 + 100  # img_hsv[i, j, 2]/2 + 100

            elif r[i, j] >= 30 and 170 < img_hsv[i, j, 0] <= 190:
                img_hsv[i, j, 0] = img_hsv[i, j, 0] - 12
                img_hsv[i, j, 1] = img_hsv[i, j, 1] * 2
                img_hsv[i, j, 2] = img_hsv[i, j, 2] / 2 + 100

            else:
                img_hsv[i, j, 0] = img_hsv[i, j, 0]
                img_hsv[i, j, 1] = img_hsv[i, j, 1]
                img_hsv[i, j, 2] = img_hsv[i, j, 2]

    res = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
    imgShow(res)


def imgShow(picture):
    height, width = picture.shape[:2]
    size = (int(width * 0.6), int(height * 0.6))
    res = cv2.resize(picture, size, interpolation=cv2.INTER_AREA)
    img_HSV = cv2.cvtColor(res, cv2.COLOR_BGR2HSV)

    def getposHsv(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print("HSV is", img_HSV[y, x])
            print("Bgr is", res[y, x])

    cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('img', res)
    cv2.setMouseCallback("img", getposHsv)
    cv2.waitKey(0)


if __name__ == '__main__':
    imgOr = 'RGBMXT1.jpg'
    imgDo(imgOr)





