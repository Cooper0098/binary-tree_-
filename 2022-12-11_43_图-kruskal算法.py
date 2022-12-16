m = 12#边数
n = 7 #顶点数
ti = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G'}
lian = [[0, 1, 2], [0, 3, 5], [0, 5, 8],
        [1, 2, 7], [1, 3, 7], [1, 4, 2],
        [2, 4, 3],
        [3, 4, 6], [3, 5, 7],[3, 6, 3],
        [4, 6, 4],
        [5, 6, 4]]
fa = [_ for _ in range(n)]
def found(node):
    if fa[node] == node:
        return node
    else:
        fa[node] = found(fa[node])
        return fa[node]

def unite(node1,node2):
    node1 = found(node1)
    node2 = found(node2)
    if node1 == node2:
        return False
    else:
        fa[node1] = node2
        return True

def kruskal(m,n,lian):
    lian.sort(key=lambda lian:int(lian[2]))

    lian_num = 0
    res = []

    for i in range(m):
        if unite(lian[i][0],lian[i][1]):
            res.append(lian[i])
        lian_num += 1

        if lian_num == n - 1:
            break
    return res

res = kruskal(m , n, lian)
s = 0

for l in res:
    print(f'{ti[l[0]]}<-->{ti[l[1]]}:{l[2]}')
    s = s + l[2]
print(f'最小树权值之和:{s}')
print(res)
print(fa)







