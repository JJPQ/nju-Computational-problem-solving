class Node:
    def __init__(self, name, height, excess):
        self.name = name
        self.height = height
        self.excess = excess

    def __str__(self):
        return f"node[name:{self.name}, height:{self.height}, excess:{self.excess}]"


adjacencyMatrix = [[0, 5, 0, 4, 0, 0], [0, 0, 3, 2, 2, 0], [0, 0, 0, 0, 0, 3],
                   [0, 0, 0, 0, 3, 0], [0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 0]]

s = Node('s', 0, 0)
a = Node('a', 0, 0)
b = Node('b', 0, 0)
c = Node('c', 0, 0)
d = Node('d', 0, 0)
t = Node('t', 0, 0)
nodes_list = [s, a, b, c, d, t]


def initial(nodes, graph):
    nodes[0].height = len(graph)
    for i in range(len(graph)):
        if graph[0][i] > 0:
            graph[i][0] = graph[0][i]
            nodes[i].excess += graph[0][i]
            graph[0][i] = 0


def show(nodes, graph):
    for line in graph:
        print(line)
    for n in nodes:
        print(n)
    print()


def push(nodes, graph):
    for i in range(0, len(graph)):
        while nodes[i].excess > 0:
            if_relabel = 1
            for j in range(0, len(graph)):
                if graph[i][j] > 0:
                    if nodes[i].excess > 0 and nodes[j].height < nodes[i].height:
                        if_relabel = 0
                        delta = min(nodes[i].excess, graph[i][j])
                        graph[i][j] -= delta
                        graph[j][i] += delta
                        if i != 0 and i != len(graph) - 1:
                            nodes[i].excess -= delta
                        if j != 0 and j != len(graph) - 1:
                            nodes[j].excess += delta
            if if_relabel:
                nodes[i].height += 1


def push_relabel(nodes, graph):
    initial(nodes, graph)
    while sum([n.excess for n in nodes]):
        push(nodes, graph)
    maxflow = sum([graph[i][0] for i in range(len(graph))])
    return maxflow


print("原始图邻接矩阵为：")
show(nodes_list, adjacencyMatrix)
maxFlow = push_relabel(nodes_list, adjacencyMatrix)
print("执行算法后图邻接矩阵为：")
show(nodes_list, adjacencyMatrix)
print(f"最大流为{maxFlow}")
