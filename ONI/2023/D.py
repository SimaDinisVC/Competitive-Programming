def eImpar(numero):
    if numero % 2 == 0:
        return False
    else:
        return True

def parte1(T, Ncores, Mcores): # N numero de cenários, Ncores para T=2 [[A,V,A],[A,V,]], Mcores para T=2 [[A,V,A],[A]]
    for t in range(T): # itera por cada teste
        posicoes = (len(Ncores[t])-len(Mcores[t]))+1 
        vitorias = 0 # Vitorias do Bruno
        for p in range(posicoes):
            if p != 0: # O primeiro index testa o normal
                Mcores[t].insert(0, 0)
            capturas = 0
            for i in range(len(Ncores[t])):
                if (i <= len(Mcores[t])):
                    if (Ncores[t][i] == "V" and Mcores[t][i] == "A") or (Ncores[t][i] == "A" and Mcores[t][i] == "V"):
                        capturas += 1
            if eImpar(capturas):
                vitorias += 1
        print(vitorias)

def parte2(T, Ncores, Mcores):
    for t in range(T): # itera por cada teste
        nminimo = -1
        posicoes = (len(Ncores[t])-len(Mcores[t]))+1
        for i in range(len(Ncores[t])):
            ladroes = list(Ncores[t])
            policias = list(Mcores[t])
            if ladroes[i-1] == "V":
                ladroes[i-1] = "A"
            else:
                ladroes[i-1] = "V"
            vitorias = 0 # Vitorias do Bruno
            for p in range(posicoes):
                if p != 0: # O primeiro index testa o normal
                    policias.insert(0, 0)
                capturas = 0
                for a in range(len(Ncores[t])):
                    if (i <= len(Mcores[t])):
                        if (ladroes[a] == "V" and policias[a] == "A") or (ladroes[a] == "A" and policias[a] == "V"):
                            capturas += 1
                if eImpar(capturas):
                    vitorias += 1
            if nminimo == -1:
                nminimo = vitorias
            elif vitorias < nminimo:
                nminimo = vitorias
        print(nminimo)

P = int(input())
T = int(input()) # Nº de cenários ou testes

#Sequência de cores
Ncores = []
Mcores = []

for i in range(T):
    N, M = map(int, input().split()) # Nº de ladrões e policias
    Ncores.append(list(input()))
    Mcores.append(list(input()))

if P == 1:
    parte1(T, Ncores, Mcores)
else:
    parte2(T, Ncores, Mcores)