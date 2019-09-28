import cv2
import numpy as np


def imgAnti(inputImg):
    one = np.ones(inputImg.shape)
    outputImg = one - inputImg
    return outputImg


def imgMultiJpg(img01, bgr):
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
    return pro


if __name__ == '__main__':
    imgOr1 = 'roi1_SVM.jpg'
    imgOr2 = 'roi1_RGB.jpg'
    outputName = 'hsv_mxt.jpg'
    img011 = cv2.imread(r'E:\HE+CAM5\roi1\{a}'.format(a=imgOr1))
    bgr1 = cv2.imread(r'E:\HE+CAM5\roi1\{b}'.format(b=imgOr2))
    proImg = imgMultiJpg(img011, bgr1)
    output = r'E:\HE+CAM5\roi1\{c}'.format(c=outputName)
    cv2.imwrite(output, proImg)
