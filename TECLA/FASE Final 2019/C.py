K = int(input())
msg = input()
alpha = list(map(chr, range(97, 123))) # 97 - a e 123 - z NO codigo ASCII

msgcripto = []

for l in msg:
    msgcripto.append(alpha[alpha.index(l.lower())+K].upper())

print("".join(msgcripto))