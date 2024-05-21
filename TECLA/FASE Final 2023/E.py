eventos = []
evento = input().split()

while evento != ["/"]:
    eventos.append(evento)
    evento = input().split()

res = []

for e in eventos:
    if e[1] == "insucesso" and eventos.count(e) >= 3 and e not in res:
        res.append(e)

res.sort(key=lambda x: (x[0], x[3].split("-")[2], x[3].split("-")[1], x[3].split("-")[0], x[4]))

for i in res:
    print(i[0]+" "+i[2]+" "+i[3]+" "+i[4])