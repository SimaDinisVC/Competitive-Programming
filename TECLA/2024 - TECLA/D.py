a = int(input())
b = int(input())
dic = {}
for i in range(b):
    c,d,e = input().split()
    dic[c] = int(e)
y = {}
soma = 0
for i in sorted(dic, key = dic.get):
    soma += dic[i]
    if soma <= a:
        y[i] = dic[i]
    else:
        break


for i in dic.keys():
    if i in list(y.keys()):
        print(i)
