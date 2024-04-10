import math


# 将更新后的价值存入X[i][2]
def update_p(packages, capacity, r):
    n = len(packages)
    max_p = max([packages[i][0] for i in range(n)])
    t = math.floor(math.log2((r - 1) * max_p / (r * n)))
    for i in range(n):
        packages[i].append(math.floor(packages[i][0] / 2**t))
        if packages[i][2] == 0:
            packages.pop(i)


def dp(packages, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(packages)):
        for j in range(capacity, packages[i][1] - 1, -1):
            dp[j] = max(dp[j], dp[j - packages[i][1]] + packages[i][0])
    return dp


X = [[3, 2], [4, 1], [2, 2], [1, 6], [2, 5], [11, 8]]  # X[i][0]代表价值，X[i][1]代表重量
print(f"原物品集为：{X}，其中[i][0]代表价值，X[i][1]代表重量\n")
capacity = 8
update_p(X, capacity, 2)
print(f"更新后物品集为：{X}，其中[i][0]代表价值，X[i][1]代表重量，X[i][2]代表更新后的价值\n")
dp = dp(X, capacity)
print(f"对于容量为{capacity}的背包，动态规划得出的dp数组为：{dp}，其最后一个元素即为最大价值\n")