a, b = input().split()
a = float(a)
b = float(b)

if a > b:
    c = a - b
else:
    c = b - a

print("%.2f"%c)