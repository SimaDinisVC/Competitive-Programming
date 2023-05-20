def regraNIgual(A,B,C):
    flag = True
    if A == B == C:
        flag = False
    return flag

def regraNDiff(A,B,C):
    flag = True
    if A != B != C:
        flag = False
    return flag

def parte1(T, LinhasDeT): # V(vermelho) A(azul) B (branco)
    for t in range(T):
        formas = 0
        linha = LinhasDeT[t]
        
        for i in range(len(linha)):
            if linha[i] == "?":
                linhaTraz = [linha[i-2],linha[i-1]]
                linhaFrente = [linha[i+1],linha[i+2]]
                # Linhas de Traz
                if (regraNIgual("B",linhaTraz[0],linhaTraz[1]) and regraNIgual("B",linhaFrente[0],linhaFrente[1]) and regraNDiff("B",linhaTraz[0],linhaTraz[1]) and regraNDiff("B",linhaFrente[0],linhaFrente[1])):
                    formas += 1
                elif (regraNIgual("V",linhaTraz[0],linhaTraz[1]) and regraNIgual("V",linhaFrente[0],linhaFrente[1]) and regraNDiff("V",linhaTraz[0],linhaTraz[1]) and regraNDiff("V",linhaFrente[0],linhaFrente[1])):
                    formas += 1
                elif (regraNIgual("A",linhaTraz[0],linhaTraz[1]) and regraNIgual("A",linhaFrente[0],linhaFrente[1]) and regraNDiff("A",linhaTraz[0],linhaTraz[1]) and regraNDiff("A",linhaFrente[0],linhaFrente[1])):
                    formas += 1
        if formas > 10000000000:
            print("grande")
        else:
            print(formas)

# grande = 10000000000

def parte2(T, LinhasDeT):
    return


P = int(input())

T = int(input())

LinhasDeT = []

for i in range(T):
    N = int(input())
    linha = list(input())
    LinhasDeT.append(linha)

if P == 1:
    parte1(T, LinhasDeT)
else:
    parte2(T, LinhasDeT)