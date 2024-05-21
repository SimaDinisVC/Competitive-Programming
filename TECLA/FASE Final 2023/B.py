c = input()
f = input()
v = input()

if ("S" not in [c, f, v]):
    print("nenhum")
    exit()

count = 0

if ("S" == c):
    count += 1
if ("S" == f):
    count += 1
if ("S" == v):
    count += 1

if (count > 1):
    print("samarra")
    exit()

if ("S" == f):
    print("casaco")
elif ("S" == c or "S" == v):
    print("gabardina")