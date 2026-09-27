import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data_file = r'E:\data.csv'
df = pd.read_csv(data_file)


# 使用Seaborn绘制Ridge Plot

plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")

# 绘制Ridge Plot
sns.kdeplot(data=df['6_0'], label='m = 0.0', shade=True, clip=(0, None))
sns.kdeplot(data=df['6_0.5'], label='m = 0.5', shade=True, clip=(0, None))
sns.kdeplot(data=df['6_1'], label='m = 1.0', shade=True, clip=(0, None))
sns.kdeplot(data=df['6'],  label=' initial', shade=True, lw=2, bw_method=0.2, linestyle='--', clip=(0, None))

# 添加标题和标签

plt.xlabel('A',fontsize=26)
plt.ylabel('Density',fontsize=26)

# 调整刻度字体大小
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
# 显示图例
legend = plt.legend()
legend = plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1))    
for text in legend.get_texts():
    text.set_fontfamily('Times New Roman')  # 设置字体为Times New Roman
    text.set_fontsize(28)  # 设置字体大小

    
# 添加标题
plt.show()
