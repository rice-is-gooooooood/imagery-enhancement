import cv2

# 读取灰度图像
img = cv2.imread('test10.png', 0)
# 中值滤波
img_median = cv2.medianBlur(img, 11)
# 显示原图和中值滤波后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Median Filtered Image', img_median)
cv2.waitKey(0)
cv2.destroyAllWindows()
