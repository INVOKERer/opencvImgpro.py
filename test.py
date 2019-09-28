import cv2

# 读取图片并缩放方便显示
img = cv2.imread(r'E:\HE+CAM5\roi1\roi1_RGB_pro.jpg')
height, width = img.shape[:2]
size = (int(width * 0.7), int(height * 0.7))
# 缩放
img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)

# BGR转化为HSV
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
HLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
Luv = cv2.cvtColor(img, cv2.COLOR_BGR2Luv)
YUV = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)


# 鼠标点击响应事件

def getposBgr(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print("Bgr is", img[y, x])
        # print("HSV is", HSV[y, x])
        # print("HLS is", HLS[y, x])
        print("Bgr:{a}, Luv:{b}, HSV:{c}, HLS:{d}, YUV:{e}".format(a=img[y, x], b=Luv[y, x], c=HSV[y, x], d=HLS[y, x], e=YUV[y, x]))


if __name__ == '__main__':
    # cv2.imshow("imageHSV", HSV)
    cv2.imshow('image', img)
    # cv2.setMouseCallback("imageHSV", getposHsv)
    cv2.setMouseCallback("image", getposBgr)
    cv2.waitKey(0)
