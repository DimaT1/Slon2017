from sys import setrecursionlimit
setrecursionlimit(200000)
INF = int(1e8)


def MST_Prim():
    min_e[0] = 0
    for i in range(n):
        v = -1
        for j in range(n):
            if (not used[j]) and (v == -1 or min_e[j] < min_e[v]):
                v = j

        used[v] = True
        if sel_e != -1 and sel_e[v] != INF:
            MST[v].append(sel_e[v])
            MST[sel_e[v]].append(v)

        for to in range(n):
            if g[v][to] < min_e[to]:
                min_e[to] = g[v][to]
                sel_e[to] = v


n = int(input())
g = [[0 for _ in range(n)] for _ in range(n)]
used = [False for _ in range(n)]
min_e = [INF for _ in range(n)]
sel_e = [INF for _ in range(n)]
cities = []
MST = [[] for _ in range(n)]

for i in range(n):
    cities.append(tuple(map(int, input().split())))

for i in range(n - 1):
    for j in range(i + 1, n):
        g[i][j] = g[j][i] = abs(cities[i][0] - cities[j][0]) + abs(cities[i][1] - cities[j][1])

MST_Prim()
print(MST)
