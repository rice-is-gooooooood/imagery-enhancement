# 彩色图像均衡化
import cv2
import numpy as np
from matplotlib import pyplot as plt
# 默认值 1 彩色 0 灰度 -1 通明通道
img = cv2.imread('test3.png', 1)

# 原图像直方图
# flatten() 将数组变成一维
hist, bins = np.histogram(img.flatten(), 255)
# print(hist)
# print(bins)
# 计算累积分布图（概率分布密度） 分布函数
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()
# 作图
plt.figure(figsize=(14, 14), dpi=100)
plt.subplot(1, 2, 1)
plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 255, [0,255], color='r')
plt.xlim([0, 255])
plt.title('before')
plt.legend(('cdf', 'histogram'), loc='upper left')

(b, g, r) = cv2.split(img)  # 通道分解
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
result = cv2.merge((bH, gH, rH), )  # 通道合成

# 计算均衡化后的直方图
hist1, bins1 = np.histogram(result.flatten(), 255, [0, 255])
cdf1 = hist1.cumsum()
cdf1_normalized = cdf1 * hist1.max() / cdf1.max()

plt.subplot(1, 2, 2)
plt.plot(cdf1_normalized, color='b')
plt.hist(result.flatten(), 255, [0, 255], color='r')
plt.xlim([0, 255])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.title('after')
plt.show()

cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()



