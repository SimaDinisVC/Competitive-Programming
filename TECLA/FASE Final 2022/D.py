N = int(input())

matriz = [[] for _ in range(N)]

ordem = True # true = andar para baixo ; false = andar para cima

# cordenadas da rastreamento
l = 0
c = 0

i = 0 # contador dos numeros

while ((c == N-1) and (l == N-1)) == False:
    if c == 0 and l == 0:
        matriz[l].append(i) # regista o 0
        i += 1
        c += 1 # anda para a frente
        matriz[l].append(i) # regista o 1
        i += 1
    if ordem == True:
        while c != 0 and l != N-1:
            c -= 1
            l += 1
            matriz[l].append(i)
            i += 1
        if l != N-1:
            l += 1
        else:
            c += 1
        matriz[l].append(i)
        i += 1
        ordem = False
    else:
        while l != 0 and c != N-1:
            l -= 1
            c += 1
            matriz[l].append(i)
            i += 1
        if c != N-1:
            c += 1
        else:
            l += 1
        matriz[l].append(i)
        i += 1
        ordem = True

for i in matriz:
    print(" ".join(str(ii) for ii in i))