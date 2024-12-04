import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
# 读取灰度图像
image = cv2.imread('test11.png', cv2.IMREAD_GRAYSCALE)
# 应用高斯模糊，核大小为5x5，标准差为1
blurred_image = cv2.GaussianBlur(image, (11,11), 3)
# 显示原图和模糊后的图像
# 显示原图直方图

fig, ax = plt.subplots(1, 2, figsize=(10, 10))
ax[0].hist(image.flatten(), 255, [0,255], color='r')
ax[0].set_title('原始图像的直方图')
ax[0].set_xlim([0, 255])  # 设置x轴的范围

# 显示均衡化后的直方图
ax[1].hist(blurred_image.flatten(), 255, [0,255], color='r')
ax[1].set_title('高斯模糊化的直方图')
ax[1].set_xlim([0, 255])  # 设置x轴的范围
plt.show()

result_eq = cv2.equalizeHist(blurred_image)

cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('result_eq', result_eq)








cv2.waitKey(0)
cv2.destroyAllWindows()
