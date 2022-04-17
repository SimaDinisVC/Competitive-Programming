N, M = map(int, input().split())
P = list(map(int, input().split()))
O = list(map(int, input().split()))
P.sort()
print(P)
d = 0
for o in O:
    for i in range(len(P)):
        if d+P[i] <= o:
            d += P[i]
        else:
            print(d)
            break