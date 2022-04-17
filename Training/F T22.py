N = int(input())
Ni = list(map(int, input().split()))
M = int(input())
Mi = list(map(int, input().split()))

pares = 0
impares = 0

for m in Mi:
    for n in Ni:
        if (m+n)%2 == 0:
            pares += 1
        else:
            impares += 1

print(pares, impares)