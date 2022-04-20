N = int(input())
Ni = list(map(int, input().split()))
M = int(input())
Mi = list(map(int, input().split()))

pares = 0
impares = 0

for n in Ni:
    for m in Mi:
        if (n%2 == m%2):
            pares += 1
        else:
            impares += 1

print(pares, impares)