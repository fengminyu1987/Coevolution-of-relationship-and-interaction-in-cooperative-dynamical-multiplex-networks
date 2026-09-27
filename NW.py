import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 参数设置
b = 1.5  # 背叛诱惑
p = 0.9  # 第一层有边的条件下第二层连边概率
m = 0 # 适应度公式参数

d = 0.05  # 权值变化
K = 0.1  # 噪声参数
R = np.array([[1, 0], [b, 0]])  # 收益矩阵

edge_weights = {}  # 存储边的权值和对应的节点

# 初始化字典用于记录初始状态和最终状态下合作指数每个区间上的人数
initial_cooperation_index_counts = {}
final_cooperation_index_counts = {}


# 初始化网络
# G_coop = nx.watts_strogatz_graph(2500, k=10, p=0.5)
G_coop = nx.newman_watts_strogatz_graph(2500, k=10, p=0.5)  # 第一层：合作网络
G_game = nx.Graph()  # 第二层：博弈网络
G_game.add_nodes_from(G_coop.nodes())  # 添加与合作网络相同的节点

# 添加合作网络的边及权值
for (u, v) in G_coop.edges():
    edge_weights[(v, u)] = edge_weights[(u, v)] = np.random.uniform(0, 1)


# 添加博弈网络的边
for u in G_game.nodes():
    for v in G_game.nodes():
        if u != v:
            if G_coop.has_edge(u, v):  # 在合作层有连边
                if random.random() < p:
                    G_game.add_edge(u, v)
            else:
                if random.random() < 1 - p:  # 在合作层无连边
                    G_game.add_edge(u, v)

# 存储合作指数、玩家类型和策略的数组
cooperation_index = np.zeros(G_coop.number_of_nodes())
strategies = np.random.randint(2, size=G_coop.number_of_nodes())

# 存储历史数据
cooperator_ratios = []


# 计算各节点合作指数
def compute_cooperation_index(node):
    neighbors = list(G_coop.neighbors(node))
    cooperation_values = []
    for neighbor in neighbors:
        cooperation_values.append(edge_weights[(node, neighbor)])
    cooperation_index[node] = sum(cooperation_values)  # 当前节点在合作层的所有邻居节点的合作连边权值之和


# 策略更新
def update_strategies():
    for node in G_game.nodes():
        neighbors = list(G_coop.neighbors(node))
        if len(neighbors) > 0:
            # 节点x首先需要选择一个在合作层的邻居y，每个邻居被选中的概率等于二者连边权值
            neighbor_weights = []
            for neighbor in neighbors:
                neighbor_weights.append(edge_weights[(node, neighbor)])
            if np.sum(neighbor_weights) == 0:
                selected_neighbor = np.random.choice(neighbors)  # 随机选择邻居
            else:
                if np.any(np.isnan(neighbor_weights)):
                    neighbor_weights = np.nan_to_num(neighbor_weights)  # 将NaN值替换为0
                neighbor_weights /= np.sum(neighbor_weights)  # 归一化权重
                selected_neighbor = np.random.choice(neighbors, p=neighbor_weights)
            # 合作指数
            Ax = cooperation_index[node]
            Ay = cooperation_index[selected_neighbor]
            P_x = R[strategies[node]][strategies[selected_neighbor]]
            P_y = R[strategies[selected_neighbor]][strategies[node]]
            Fx = m * P_x + Ax
            Fy = m * P_y + Ay
            prob = 1 / (1 + np.exp((Fx - Fy) / K))
            strategies[node] = np.random.choice([strategies[node], strategies[selected_neighbor]],
                                                p=[1 - prob, prob])


# 更新合作层权值
def update_network():
    for edge in G_game.edges():
        node1, node2 = edge
        # 双方都合作
        if strategies[node1] == 0 and strategies[node2] == 0:
            if G_coop.has_edge(node1, node2):
                if edge_weights[(node1, node2)] + d <= 1:
                    edge_weights[(node1, node2)] += d  # 权值增加，但不超过1
                else:
                    edge_weights[(node1, node2)] = 1
        # 双方都背叛
        elif strategies[node1] == 1 and strategies[node2] == 1:
            if G_coop.has_edge(node1, node2):
                if edge_weights[(node1, node2)] - d >= 0:
                    edge_weights[(node1, node2)] -= d
                else:
                    edge_weights[(node1, node2)] = 0  # 权值减少，但不小于0


# 计算初始合作指数
for node in G_coop.nodes():
    compute_cooperation_index(node)
initial_cooperation_index = np.copy(cooperation_index)

for _ in range(400):
    # 计算合作指数和更新玩家类型
    for node in G_coop.nodes():
        compute_cooperation_index(node)
     

    # 计算合作者比例
    cooperator_count = np.sum(strategies == 0)
    print(cooperator_count)
    cooperator_ratio = cooperator_count / G_coop.number_of_nodes()
    cooperator_ratios.append(cooperator_ratio)

    # 更新策略和网络
    update_strategies()
    update_network()

# 绘制合作者比例变化曲线
plt.plot(cooperator_ratios, label='b=1.5, m=1')
plt.xlabel('Time Step')
plt.ylabel('Cooperator Ratio')
plt.title('3')
plt.legend()
plt.show()

import csv

# 在模拟循环的最后，输出 cooperation_index 到 CSV 文件
with open('cooperation_index.csv', 'w', newline='') as csvfile:
    # 创建 CSV 文件写入对象
    csv_writer = csv.writer(csvfile)

    # 写入 CSV 文件的标题行
    csv_writer.writerow(['Node', 'Cooperation Index'])

    # 遍历每个节点，写入节点和对应的 cooperation_index
    for node in G_coop.nodes():
        compute_cooperation_index(node)
        csv_writer.writerow([node, cooperation_index[node]])


from scipy.stats import skew, kurtosis

# 在模拟循环的最后，计算 cooperation_index 的分布偏度和峰度
cooperation_indices = []

for node in G_coop.nodes():
    compute_cooperation_index(node)
    cooperation_indices.append(cooperation_index[node])

# 计算偏度和峰度
skewness = skew(cooperation_indices)
kurt = kurtosis(cooperation_indices)

# 打印结果
print("Cooperation Index Distribution Skewness:", skewness)
print("Cooperation Index Distribution Kurtosis:", kurt)




