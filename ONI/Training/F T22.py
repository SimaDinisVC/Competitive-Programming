N = int(input())
Ni = list(map(int, input().split()))
M = int(input())
Mi = list(map(int, input().split()))

i1 = 0
for i in Ni:
    if i & 1:
        i1 += 1
p1 = N - i1

i2 = 0
for i in Mi:
    if i & 1:
        i2+=1
p2 = M - i2

pares = (p1*p2) + (i1*i2)

print(pares, (N*M) - pares)