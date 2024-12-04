import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("picture1.png", 0) # 以灰度图像格式读取图像
cv2.imshow("picture1", img)

# 基于numpy数组的reshape方法将二维数组img展开成一维数组
flattene_img = img.reshape((-1,)) # 将reshape的shape参数设置为(-1,)，代码可以自动计算img展成一维数组后的实际大小
# ---> 比如img形状为(16, 16) ---> 参数(-1,) 等价于参数(256, )
all_num = int(img.shape[0]*img.shape[1])
print(all_num)
# 对一维数组进行直方图绘制
# 显示频率 并且归一化处理
plt.hist(flattene_img, bins=256) # bins=256表示包含256个灰度级

plt.show()

cv2.waitKey(0) # 显示图像
