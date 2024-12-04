from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

image_path = r'test11.png'
image = Image.open(image_path).convert('L')

# 直方图均衡化
image_eq = ImageOps.equalize(image)

# 获取两个图像的直方图数据
histogram = image.histogram()
histogram_eq = image_eq.histogram()

# 创建一个2x2的子图布局
fig, ax = plt.subplots(2, 2, figsize=(10, 10))

# 显示原图
ax[0, 0].imshow(image, cmap='gray')
ax[0, 0].set_title('原始图像')
ax[0, 0].axis('off')  # 不显示坐标轴

# 显示均衡化后的图像
ax[0, 1].imshow(image_eq, cmap='gray')
ax[0, 1].set_title('均衡化后的图像')
ax[0, 1].axis('off')  # 不显示坐标轴

# 显示原图直方图
ax[1, 0].bar(range(256), histogram, width=1)
ax[1, 0].set_title('原始图像的直方图')
ax[1, 0].set_xlim([0, 255])  # 设置x轴的范围

# 显示均衡化后的直方图
ax[1, 1].bar(range(256), histogram_eq, width=1)
ax[1, 1].set_title('均衡化后的直方图')
ax[1, 1].set_xlim([0, 255])  # 设置x轴的范围

# 调整子图间距
plt.tight_layout()
plt.show()