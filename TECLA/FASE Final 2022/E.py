T = int(input()) # n de tarefas totais

t = [] # [ [IDtarefa, tempo, RH, NTarefasProcedentes, ...tarefas],  ...]
for i in range(T):
    t.append(list(map(int, input().split())))

tarefasExecutadas = [] # tarefas que já foram executadas

rhativos = [] # rh em cada instante

timer = -1
tarefasexe = { 1 : 0 } # id : tempoocorrido
while len(tarefasExecutadas) != T:
    timer += 1

    tarefasexecutadas = []
    rh = 0
    for i in t:
        if i[0] not in tarefasExecutadas and i[0] not in tarefasexe:
            z = True
            for ii in range(4, 4+i[3]): # verifica se a tarefa i[0] tem todas as tarefas pendentes executadas
                if i[ii] not in tarefasExecutadas: 
                    z = False
            if (z):
                tarefasexe[i[0]] = 1
                rh += i[2]
        elif i[0] in tarefasexe and tarefasexe[i[0]] == i[1]:
            del tarefasexe[i[0]] # remove a tarefa concluida das tarefas executadas
            tarefasExecutadas.append(i[0]) # tarefa marcada como concluida
        elif i[0] in tarefasexe:
            tarefasexe[i[0]] += 1
            rh += i[2]
    rhativos.append(rh)
    
        
    


print(max(rhativos))
print(timer)