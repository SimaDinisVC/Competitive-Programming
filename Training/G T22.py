def rm(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l
N, M = map(int, input().split())
c = list(map(int, input().split()))
c = rm(c)
print(N-len(c))