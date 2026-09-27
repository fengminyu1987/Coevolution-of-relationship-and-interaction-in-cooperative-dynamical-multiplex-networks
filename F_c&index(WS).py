import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

# 参数设置
b = 1.3  # 背叛诱惑
p = 0.9  # 第一层有边的条件下第二层连边概率
m = 0.3 # 适应度公式参数

d = 0.05  # 权值变化
K = 0.1  # 噪声参数
R = np.array([[1, 0], [b, 0]])  # 收益矩阵

edge_weights = {}  # 存储边的权值和对应的节点


# 初始化网络
G_coop = nx.watts_strogatz_graph(2500, k=10, p=0.5)  # 第一层：合作网络
G_game = nx.Graph()  # 第二层：博弈网络
G_game.add_nodes_from(G_coop.nodes())  # 添加与合作网络相同的节点

# 添加合作网络的边及权值
for (u, v) in G_coop.edges():
    edge_weights[(v, u)] = edge_weights[(u, v)] = np.random.uniform(0, 1)
    # edge_weights[(v, u)] = edge_weights[(u, v)] = np.random.normal(0, 1)

# 添加博弈网络的边
for u in G_game.nodes():
    for v in G_game.nodes():
        if u != v:
            if G_coop.has_edge(u, v):  # 在合作层有连边，0.6的概率进行博弈
                if random.random() < p:
                    G_game.add_edge(u, v)
            else:
                if random.random() < 1 - p:  # 在合作层无连边，0.4的概率进行博弈
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
            # if np.sum(neighbor_weights) == 0:
            #     selected_neighbor = np.random.choice(neighbors)  # 随机选择邻居
            # else:
            #     if np.any(np.isnan(neighbor_weights)):
            #         neighbor_weights = np.nan_to_num(neighbor_weights)  # 将NaN值替换为0
            #     neighbor_weights /= np.sum(neighbor_weights)  # 归一化权重
            #     selected_neighbor = np.random.choice(neighbors, p=neighbor_weights)
            # 合作指数
            selected_neighbor = np.random.choice(neighbors)  # 随机选择邻居
            neighbor_neighbor_indices = list(G_coop.neighbors(selected_neighbor))
            Ax = cooperation_index[node]
            Ay = cooperation_index[selected_neighbor]
            P_x = np.sum([R[strategies[node]][strategies[k]] for k in neighbors])
            P_y = np.sum([R[strategies[selected_neighbor]][strategies[k]] for k in neighbor_neighbor_indices])
            
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


for _ in range(600):
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
plt.title('WS')
plt.legend()
plt.show()


# 计算平稳后合作者比例的均值
stable_cooperator_ratios = cooperator_ratios[400:]  # 提取平稳波动状态下的合作者比例数据
mean_stable_cooperator_ratio = np.mean(stable_cooperator_ratios)
print("Mean Cooperator Ratio in Stable State:", mean_stable_cooperator_ratio)

# 初始和最终状态 cooperation_index 分布
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(initial_cooperation_index, bins=20, color='blue', alpha=0.5)
plt.xlabel('Cooperation Index')
plt.ylabel('Frequency')
plt.title('Initial State')

# 计算并打印初始状态合作指数区间上的频数
initial_hist, initial_bins = np.histogram(initial_cooperation_index, bins=10)
print("Initial State Cooperation Index Histogram:")
for i, freq in enumerate(initial_hist):
    print(f"{initial_bins[i]:.2f}: {freq}")

plt.subplot(1, 2, 2)
plt.hist(cooperation_index, bins=20, color='red', alpha=0.5)
plt.xlabel('Cooperation Index')
plt.ylabel('Frequency')
plt.title('Final State')
plt.tight_layout()

# 计算并打印最终状态合作指数区间上的频数
final_hist, final_bins = np.histogram(cooperation_index, bins=10)
print("\nFinal State Cooperation Index Histogram:")
for i, freq in enumerate(final_hist):
    print(f"{final_bins[i]:.2f}: {freq}")

plt.show()


initial_mean = np.mean(initial_cooperation_index)
final_mean = np.mean(cooperation_index)
print(initial_mean,final_mean)

