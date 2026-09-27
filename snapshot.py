import matplotlib.pyplot as plt
import numpy as np

# 创建合作者和背叛者的热力图数据
heatmap_data = np.array([[0, 0, 0, 1, 0],
                        [0, 0, 1, 1, 1],
                        [0, 0, 0, 1, 0],
                        [1, 1, 1, 1, 1],
                        [0, 0, 0, 1, 0]])


# 创建一个自定义颜色映射，0对应深蓝色，1对应白色
cmap = plt.cm.colors.ListedColormap(['navy', 'white'])


# 创建一个热力图
plt.imshow(heatmap_data, cmap=cmap, interpolation='none', aspect='equal')

# 显示坐标轴，但不显示刻度
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())

# 显示热力图
plt.show()
