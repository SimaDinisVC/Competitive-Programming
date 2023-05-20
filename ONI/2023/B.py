"""
N é o nº de pares de canos que um nível contem
cada T nivel tem N intervalos de altitudes
A cada segundo o Pássaro move-se para a direita
O jogador pode controlar a sequência de altitudes do pássaro A1, A2, . . . , An (int) ao longo do nível
a altura do cano inferior Li e a altura do cano superior Ri
"""
P = int(input()) # Parte do programa

T = int(input()) # Nº de níveis a testar

N = int(input())
L = list(map(int, input().split()))
R = list(map(int, input().split()))

if P == 1:
    for i in range(T):
        possivel = True
        altura_atual = L[0]
        sequencia = [altura_atual]
        for i in range(1, N):
            altura_seguinte = altura_atual + 1
            if altura_seguinte < L[i] or altura_seguinte > R[i]:
                possivel = False
                break
            altura_atual = altura_seguinte
            sequencia.append(altura_atual)
        if possivel:
            print(" ".join(map(str, sequencia)))
        else:
            print("-1")
else:
    for i in range(T):
        possivel = True
        altura_atual = l[0]
        sequencia = [altura_atual]
        for i in range(1, n):
            alturas = [altura_atual, altura_atual+1, altura_atual-1]
            alturas = [H for H in alturas if L[i] <= H <= R[i]]
            if not alturas:
                possivel = False
                break
            altura_atual = alturas[0]
            sequencia.append(altura_atual)
        if possivel:
            print(" ".join(map(str, sequencia)))
        else:
            print("-1")