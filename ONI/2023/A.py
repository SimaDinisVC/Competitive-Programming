def verificaCordenadasNoEspaco(N,M, linha, coluna):
    flag = True
    if linha < 1 or linha > N:
        flag = False
    if coluna < 1 or coluna > M:
        flag = False
    return flag

def parte1(N, M, grelha, conjuntos):
    for conjunto in conjuntos:
        cordenadas = [1,1] # linha, coluna
        instrucoes = list(conjunto)
        for inst in instrucoes:
            if inst == "D":
                if verificaCordenadasNoEspaco(N, M, cordenadas[0], cordenadas[1]+1):
                    nextCelula = grelha[cordenadas[0]-1][cordenadas[1]]
                    if nextCelula == ".":
                        cordenadas[1] += 1
            elif inst == "E":
                if verificaCordenadasNoEspaco(N, M, cordenadas[0], cordenadas[1]-1):
                    nextCelula = grelha[cordenadas[0]-1][cordenadas[1]-2]
                    if nextCelula == ".":
                        cordenadas[1] -= 1
            elif inst == "B":
                if verificaCordenadasNoEspaco(N, M, cordenadas[0]+1, cordenadas[1]):
                    nextCelula = grelha[cordenadas[0]][cordenadas[1]-1]
                    if nextCelula == ".":
                        cordenadas[0] += 1
            else:
                if verificaCordenadasNoEspaco(N, M, cordenadas[0]-1, cordenadas[1]):
                    nextCelula = grelha[cordenadas[0]-2][cordenadas[1]-1]
                    if nextCelula == ".":
                        cordenadas[0] -= 1
        print(cordenadas[0], cordenadas[1])

def parte2(N, M, grelha, conjuntos):
    for conjunto in conjuntos:
        cordenadas = [1,1] # linha, coluna
        instrucoes = list(conjunto)
        automatico = False
        autoLetter = ""
        brekou = False
        
        for inst in instrucoes:
            cordenadasRepetidas = {}
            breakar = False
            while automatico:
                if 3 in cordenadasRepetidas.values(): # 3 é um nº considerável
                    print("ciclo")
                    breakar = True
                    break

                if tuple(cordenadas) not in cordenadasRepetidas.keys():
                    cordenadasRepetidas[tuple(cordenadas)] = 1
                else:
                    cordenadasRepetidas[tuple(cordenadas)] += 1

                if autoLetter == "D":
                    if verificaCordenadasNoEspaco(N, M, cordenadas[0], cordenadas[1]+1):
                        nextCelula = grelha[cordenadas[0]-1][cordenadas[1]]
                        if nextCelula == ".":
                            cordenadas[1] += 1
                        elif nextCelula in ["D","E","B","C"]:
                            cordenadas[1] += 1
                            automatico = True
                            autoLetter = nextCelula
                        else:
                            automatico = False
                            autoLetter = ""
                    else:
                        automatico = False
                        autoLetter = ""
                if autoLetter == "E":
                    if verificaCordenadasNoEspaco(N, M, cordenadas[0], cordenadas[1]-1):
                        nextCelula = grelha[cordenadas[0]-1][cordenadas[1]-2]
                        if nextCelula == ".":
                            cordenadas[1] -= 1
                        elif nextCelula in ["D","E","B","C"]:
                            cordenadas[1] -= 1
                            automatico = True
                            autoLetter = nextCelula
                        else:
                            automatico = False
                            autoLetter = ""
                    else:
                        automatico = False
                        autoLetter = ""
                if autoLetter == "B":
                    if verificaCordenadasNoEspaco(N, M, cordenadas[0]+1, cordenadas[1]):
                        nextCelula = grelha[cordenadas[0]][cordenadas[1]-1]
                        if nextCelula == ".":
                            cordenadas[0] += 1
                        elif nextCelula in ["D","E","B","C"]:
                            cordenadas[0] += 1
                            automatico = True
                            autoLetter = nextCelula
                        else:
                            automatico = False
                            autoLetter = ""
                    else:
                        automatico = False
                        autoLetter = ""
                if autoLetter == "C":
                    if verificaCordenadasNoEspaco(N, M, cordenadas[0]-1, cordenadas[1]):
                        nextCelula = grelha[cordenadas[0]-2][cordenadas[1]-1]
                        if nextCelula == ".":
                            cordenadas[0] -= 1
                        elif nextCelula in ["D","E","B","C"]:
                            cordenadas[0] -= 1
                            automatico = True
                            autoLetter = nextCelula
                        else:
                            automatico = False
                            autoLetter = ""
                    else:
                        automatico = False
                        autoLetter = ""

            if breakar:
                brekou = True
                break

            if inst == "D":
                if verificaCordenadasNoEspaco(N, M, cordenadas[0], cordenadas[1]+1): 
                    nextCelula = grelha[cordenadas[0]-1][cordenadas[1]]
                    if nextCelula == ".":
                        cordenadas[1] += 1
                    elif nextCelula in ["D","E","B","C"]:
                        automatico = True
                        autoLetter = nextCelula
            elif inst == "E":
                if verificaCordenadasNoEspaco(N, M, cordenadas[0], cordenadas[1]-1):
                    nextCelula = grelha[cordenadas[0]-1][cordenadas[1]-2]
                    if nextCelula == ".":
                        cordenadas[1] -= 1
                    elif nextCelula in ["D","E","B","C"]:
                        automatico = True
                        autoLetter = nextCelula
            elif inst == "B":
                if verificaCordenadasNoEspaco(N, M, cordenadas[0]+1, cordenadas[1]):
                    nextCelula = grelha[cordenadas[0]][cordenadas[1]-1]
                    if nextCelula == ".":
                        cordenadas[0] += 1
                    elif nextCelula in ["D","E","B","C"]:
                        automatico = True
                        autoLetter = nextCelula
            else: # C
                if verificaCordenadasNoEspaco(N, M, cordenadas[0]-1, cordenadas[1]):
                    nextCelula = grelha[cordenadas[0]-2][cordenadas[1]-1]
                    if nextCelula == ".":
                        cordenadas[0] -= 1
                    elif nextCelula in ["D","E","B","C"]:
                        automatico = True
                        autoLetter = nextCelula
        
        if not brekou:
            print(cordenadas[0], cordenadas[1])

P = int(input()) # parte do programa

N, M = map(int, input().split()) # N <=> Nº de linhas; M <=> Nº de colunas.

# Seguem-se N linhas, cada uma com M caracteres, representando a grelha.
# Sendo "." desocupado e "#" ocupado.

grelha = [] # Uma matriz que representa a grelha.

for i in range(N):
    linha = list(input())
    grelha.append(linha)

T = int(input()) # representa o nº de conjuntos de instruções.
conjuntos = [] # inst

for i in range(T):
    K = input();
    conjuntos.append(input())

if P == 1:
    parte1(N, M, grelha, conjuntos)
else:
    parte2(N, M, grelha, conjuntos)