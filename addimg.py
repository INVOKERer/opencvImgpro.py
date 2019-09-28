import cv2
import numpy as np


def imgAddJpg(img1, img2):
    imgC = np.asarray(img1)
    imgD = np.asarray(img2)
    pro = imgC + imgD
    return pro



if __name__ == '__main__':
    imgOr1 = 'hsv_mxt.jpg'
    imgOr2 = 'rgbMXT2.jpg'
    outputWay = 'add_mxt.jpg'
    imgA = cv2.imread(r'E:\HE+CAM5\roi1\{a}'.format(a=imgOr1))
    imgB = cv2.imread(r'E:\HE+CAM5\roi1\{b}'.format(b=imgOr2))
    proc = imgAddJpg(imgOr1, imgOr2)
    output = r'E:\HE+CAM5\roi1\{c}'.format(c=outputWay)
    cv2.imwrite(output, proc)