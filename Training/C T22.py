n = int(input())
h = input().split()
for i in range(n):
    h[i] = int(h[i])
counter = 0
alt = 0

for a in h:
    if a > alt:
        counter += 1
        alt = a

print(counter)