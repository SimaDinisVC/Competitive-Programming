def datasparaTotalDias(ano, mes, dia):
    countDiasTotais = 0
    diasEMmeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # dias em meses
    for i in range (1900, ano):
        if i % 4 == 0 and i % 100 != 0 or i % 4 == 0 and i % 400 == 0:
            countDiasTotais += 366
        else:
            countDiasTotais += 365
    if ano % 4 == 0 and ano % 100 != 0 or ano % 4 == 0 and ano % 400 == 0:
        diasEMmeses[1] = 29
    countDiasTotais += sum(diasEMmeses[0:mes-1])
    countDiasTotais += dia
    return countDiasTotais
    

d1 = int(input())
m1 = int(input())
a1 = int(input())

d2 = int(input())
m2 = int(input())
a2 = int(input())

idade = a2 - a1
if m1 > m2:
    idade-=1
elif d1 > d2:
    idade-=1

dias_anos = [0,0,0,0,0,0,0] # Contagem de anos nos dias semanais (domin, seg, etc...)

# seg - 0,14 ; ter - 0,28 ; quar - 0.42 ; qui - 0,57 ; sex - 0,71 ; sab - 0,85 ; dom - 1,0;

for i in range(1,idade+1):
    semanas = datasparaTotalDias(a1+i, m1, d1) / 7
    diadaSemana = float(str(semanas - int(semanas))[:4])
    if diadaSemana == 0.0:
        dias_anos[0] += 1
    elif diadaSemana == 0.14:
        dias_anos[1] += 1
    elif diadaSemana == 0.28:
        dias_anos[2] += 1
    elif diadaSemana == 0.42:
        dias_anos[3] += 1
    elif diadaSemana == 0.57:
        dias_anos[4] += 1
    elif diadaSemana == 0.71:
        dias_anos[5] += 1
    elif diadaSemana == 0.85:
        dias_anos[6] += 1

for i in dias_anos:
    print(i)

print(idade)