from PIL import Image
import numpy as np
import cv2
import math
from spectral import *


# hsv
def imgDo(imgOri, outputImg):
    img_BGR = cv2.imread(r'E:\HE+CAM5\roi1\{a}'.format(a=imgOri))
    bgr = np.asarray(img_BGR)
    (m, n) = bgr.shape[:2]
    b = bgr[..., 0]
    g = bgr[..., 1]
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

    output = r'E:\HE+CAM5\roi1\{b}'.format(b=outputImg)
    cv2.imwrite(output, res)


if __name__ == '__main__':
    imgOr = 'RGBMXT1.jpg'
    outputWay = 'hsv_mxt.jpg'
    imgDo(imgOr, outputWay)



