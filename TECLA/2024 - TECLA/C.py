normal = ["a",	"b",	"c",	"d",	"e",	"f",	"g",	"h",	"i",	"j",	"k",	"l",	"m",	"n",	"o",	"p",	"q",	"r",	"s",	"t",	"u",	"v",	"w",	"x",	"y",	"z"]
cifrado = ["z",	"y",	"x",	"w",	"v",	"u",	"t",	"s",	"r",	"q",	"p",	"o",	"n",	"m",	"l",	"k",	"j",	"i",	"h",	"g",	"f",	"e",	"d",	"c",	"b",	"a"]

msg = input()

msgcifrada = []
a = 0

for l in msg:
    if l not in normal and l != " ":
        print("Mensagem invalida! Use apenas letras minusculas e espacos.")
        a = 1
        break
    elif l != " ":
        msgcifrada.append(cifrado[normal.index(l)])
    elif l == " ":
        msgcifrada.append(" ")

if a == 0:
    print("".join(map(str, msgcifrada)))