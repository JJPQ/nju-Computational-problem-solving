def bubbleSort(l):
    n = len(l)
    if n <= 1:
        return l
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if l[j][0] / l[j][1] < l[j + 1][0] / l[j + 1][1]:
                l[j], l[j + 1] = l[j + 1], l[j]


def KP(packages, capacity):
    Y = []
    p = 0
    b = capacity
    for i in range(len(packages)):
        if b >= packages[i][1]:
            Y.append(packages[i])
            p += packages[i][0]
            b -= packages[i][1]
    return max(max([packages[i][0] for i in range(len(packages))]), p)


X = [[3, 2], [4, 1], [2, 2], [1, 6], [2, 5], [11, 8]]  # X[i][0]代表价值，X[i][1]代表重量
print(f"物品集为{X}，其中X[i][0]代表价值，X[i][1]代表重量\n")
bubbleSort(X)
capacity = 8
sum_value = KP(X, capacity)
print(f"容量为{capacity}的背包所能存放物品的最大价值为：{sum_value}\n")