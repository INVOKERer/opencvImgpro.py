import cv2
import numpy as np


def imgAnti(inputImg):
    one = np.ones(inputImg.shape)
    outputImg = one - inputImg
    return outputImg


def imgMultiJpg(inputImg, imgOri, outputImg):
    img01 = cv2.imread(r'E:\HE+CAM5\roi1\{a}'.format(a=inputImg))
    bgr = cv2.imread(r'E:\HE+CAM5\roi1\{b}'.format(b=imgOri))
    BGR = np.asarray(bgr)
    ret, thresh1 = cv2.threshold(img01, 127, 255, cv2.THRESH_BINARY)
    Img01 = thresh1 / 255
    # pro = RGB.copy()
    Img01 = imgAnti(Img01)
    pro = np.multiply(BGR, Img01)
    '''
    pro[:, :, 0] = np.multiply(RGB[:, :, 0], Img01)
    pro[:, :, 1] = np.multiply(RGB[:, :, 1], Img01)
    pro[:, :, 2] = np.multiply(RGB[:, :, 2], Img01)
    '''
    output = r'E:\HE+CAM5\roi1\{c}'.format(c=outputImg)
    cv2.imwrite(output, pro)


if __name__ == '__main__':
    imgOr1 = 'roi1_SVM.jpg'
    imgOr2 = 'roi1_RGB.jpg'
    outputWay = 'hsv_mxt.jpg'
    imgMultiJpg(imgOr1, imgOr2, outputWay)
