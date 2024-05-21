m, n = map(int, input().split()) # m - linhas, n - colunas
Namigos = int(input())
amigos = []
for i in range(Namigos):
    amigos.append(int(input()))

matriz = []
c = 0
for i in range(m):
    matriz.append([])
    for ii in range(1, n+1):
        matriz[i].append(ii+c*n)
    c += 1

mesasDistancias = {}

for i in range(1, m*n+1):
    if (i not in amigos):
        if ( i % n == 0):
            y = (i / n) - 1
        else:
            y = i // n
        y = int(y)
        cordenadaI = (matriz[y].index(i), y) # coordenadas da mesa teste
        distanciaAmigos = [] # [1, 1, 1, 1, 2]
        for ii in amigos:
            if ( ii % n == 0):
                y = (ii / n) - 1
            else:
                y = ii // n
            y = int(y)
            cordenadaA = (matriz[y].index(ii), y) # coordenadas dos amigos
            manhatan = abs(cordenadaI[0]-cordenadaA[0]) + abs(cordenadaI[1]-cordenadaA[1])
            distanciaAmigos.append(manhatan)
            if len(distanciaAmigos) != 0 and manhatan not in distanciaAmigos:
                break
        if len(set(distanciaAmigos)) == 1:
            mesasDistancias[i] = distanciaAmigos[0]

if len(mesasDistancias.keys()) == 0:
    print(-1)
else:
    dist = min(mesasDistancias.values()) # distancia 
    for chave, valor in mesasDistancias.items():
        if dist == valor:
            print(chave)

