N, k, m = map(int, input().split())

l = list(range(1, N+1))

pares = []

pointerH = 0 # começa a contar apartir de l[ultimoH] no sentido Horario
pointerA = - 1 # começa a contar apartir de l[ultimoA] no sentido Horario
#while len(l) != 0:
if (pointerH + k - 1 >= len(l)):
    pointerH = pointerH + k - 1 - (len(l) -1)
else:
    pointerH += k - 1 # retira -1 por causa do index
if (abs(pointerA - m - 1) >= len(l)):
    pointerA = pointerA + m - 1 + (len(l) -1)
else:
    pointerA -= m - 1  # retira -1 por causa do index
pares.append([l[pointerH], l[pointerA]])
b = l[pointerA]
l.remove(l[pointerH])
l.remove(b)
if (pointerH + k - 1 >= len(l)):
    pointerH = pointerH + k - 1 - (len(l) -1)
else:
    pointerH += k - 1 # retira -1 por causa do index
if (abs(pointerA - m - 1) >= len(l)):
    pointerA = pointerA + m - 1 + (len(l) -1)
else:
    pointerA -= m - 1  # retira -1 por causa do index
pares.append([l[pointerH], l[pointerA]])
b = l[pointerA]
l.remove(l[pointerH])
l.remove(b)
##
if (pointerH + k - 1 >= len(l)):
    print(pointerH + k - 1 - (len(l) +1))
    #pointerH = pointerH + k - 1 - (len(l) -1)
else:
    pointerH += k - 1 # retira -1 por causa do index
if (abs(pointerA - m + 1) >= len(l)):
    print(pointerA - m - 1 + (len(l) + 1))
    #pointerA = pointerA + m - 1 + (len(l) -1)
else:
    pointerA -= m - 1  # retira -1 por causa do index

# pares.append([l[pointerH], l[pointerA]])
# l.remove(l[pointerH])
# l.remove(l[pointerA])


#print(pointerH, pointerA)
print(l)
print(pares)