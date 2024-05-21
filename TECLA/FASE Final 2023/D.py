c = input()
t = input()

if len(''.join(set(c))) < len(c):
    print("chave incorreta")
    exit()

pF = ""

for i in range((len(t) // len(c))+1):
    p = t[i*len(c):i*len(c)+len(c)] # dividi a string por parte
    pr = ""
    for ct in c:
        if len(p) > len(pr):
            try:
                pr += p[int(ct)-1]
            except:
                continue
        else:
            break
    pF += pr

print(pF)