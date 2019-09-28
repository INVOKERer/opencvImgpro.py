import numpy as np
import cv2


# hsv
def imgDo(img_BGR):
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
    return res


if __name__ == '__main__':
    imgOri = 'RGBMXT1.jpg'
    outputName = 'hsv_mxt.jpg'
    img_BGR1 = cv2.imread(r'E:\HE+CAM5\roi1\{a}'.format(a=imgOri))
    resImg = imgDo(img_BGR1)
    outputWay = r'E:\HE+CAM5\roi1\{b}'.format(b=outputName)
    cv2.imwrite(outputWay, resImg)



