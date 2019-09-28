import cv2
import numpy as np


def imgAddJpg(inputImg, imgOri, outputImg):
    img1 = cv2.imread(r'E:\HE+CAM5\roi1\{a}'.format(a=inputImg))
    img2 = cv2.imread(r'E:\HE+CAM5\roi1\{b}'.format(b=imgOri))
    img1 = np.asarray(img1)
    img2 = np.asarray(img2)
    pro = img1 + img2

    output = r'E:\HE+CAM5\roi1\{c}'.format(c=outputImg)
    cv2.imwrite(output, pro)


if __name__ == '__main__':
    imgOr1 = 'hsv_mxt.jpg'
    imgOr2 = 'rgbMXT2.jpg'
    outputWay = 'add_mxt.jpg'
    imgAddJpg(imgOr1, imgOr2, outputWay)
