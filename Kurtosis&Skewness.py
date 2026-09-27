import pandas as pd
from scipy.stats import skew, kurtosis

# 读取CSV文件
data = pd.read_csv(r'E:\data.csv')

# 提取列名
columns = data.columns

# 计算每一列数据的偏度和峰度
for column in columns:
    column_data = data[column]
    skewness = skew(column_data)
    kurt = kurtosis(column_data)
    
    print(f"列 {column} 的偏度为: {skewness}")
    print(f"列 {column} 的峰度为: {kurt}")
    print()
