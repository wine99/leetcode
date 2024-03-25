# 多多快递站共有n个快递点，n个快递点之间通过m条单向车道连接。快递员从任何一个快递站点出发，都无法通过单向车道回到该站点。 也就是说，n个快递点组成一张有向无环图。对于快递点u，如果对于所有的快递点v (v \neq u)， 快递员都可以从u走到v，或者从v走到u，那么则评定站点u为超级快递点。请你帮忙算一算，一共有多少个超级快递点。

# 第一行 2个数字n ( 2 \leq n \leq 3 * 10^{5} ) , m (1 \leq m \leq 3 * 10^{5}), n为快递点个数，m为单向车道个数。
# 接下来的m行每行两个数字 u,v （1 \leq u,v \leq n, u \neq v），表示有一条站点u指向v的单向车道。

# n, m = map(int, input().split())
# graph = [[False] * (n + 1) for _ in range(n + 1)]

# queue = []
# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u][v] = True
#     queue.append((u, v))

# while queue:
#     u, v = queue.pop(0)
#     for i in range(1, n + 1):
#         if graph[i][u] and not graph[i][v]:
#             graph[i][v] = True
#             queue.append((i, v))
#         if graph[v][i] and not graph[u][i]:
#             graph[u][i] = True
#             queue.append((u, i))

# ans = 0
# for x in range(1, n + 1):
#     count = 0
#     for y in range(1, n + 1):
#         if graph[x][y] or graph[y][x]:
#             count += 1
#     if count == n - 1:
#         ans += 1
# print(ans)

# 超时，通过4%

# 7 7
# 1 2
# 2 3
# 2 5
# 3 4
# 5 4
# 6 4
# 4 7

# 2


import random

n, m = map(int, input().split())
graph = {}
graphT = {}

for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)
    if v not in graphT:
        graphT[v] = [u]
    else:
        graphT[v].append(u)


def dfs(graph, node, path: set):
    path.add(node)
    if node not in graph:
        return
    dfs(graph, random.sample(graph[node], 1)[0], path)


node_route = {}
working = set(range(1, n + 1))
while working:
    node = working.pop()
    path = set()
    dfs(graph, node, path)
    dfs(graphT, node, path)
    node_route[node] = path
    working -= path

ans = set(range(1, n + 1))
for node in node_route:
    ans &= node_route[node]
print(ans)
