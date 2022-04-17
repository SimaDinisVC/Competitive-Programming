# THIS CODE IS AN EXPERIMENT AND IT IS NOT ALREADY

n, m, k = map(int, input().split())
planes = []
clouds = []
pairs = 0
for c in range(n):
    x, y = map(int, input().split())
    planes.append([x,y,'E'])
for c in range(m):
    x, y = map(int, input().split())
    clouds.append([x,y])

print(planes)
print(clouds)

for i in range(k):
    counter = -1
    for i in planes:
        counter += 1
        if i[2] == 'E':
            ii = [i[0] + 1, i[1]]
            if ii in clouds:
                ii = [i[0], i[1] - 1]
                ii.append('S')
                planes[counter] = ii
            else:
                ii.append('E')
                planes[counter] = ii
        elif i[2] == 'S':
            ii = [i[0], i[1] - 1]
            if ii in clouds:
                ii = [i[0] - 1, i[1]]
                ii.append('O')
                planes[counter] = ii
            else:
                ii.append('S')
                planes[counter] = ii
        elif i[2] == 'O':
            ii = [i[0] - 1, i[1]]
            if ii in clouds:
                ii = [i[0], i[1] + 1]
                ii.append('N')
                planes[counter] = ii
            else:
                ii.append('O')
                planes[counter] = ii
        elif i[2] == 'N':
            ii = [i[0], i[1] + 1]
            if ii in clouds:
                ii = [i[0] + 1, i[1]]
                ii.append('E')
                planes[counter] = ii
            else:
                ii.append('N')
                planes[counter] = ii
for i in planes:
    if planes.count(i) > 1:
        pairs += planes.count(i)//2

print(pairs)

# THIS CODE IS AN EXPERIMENT AND IT IS NOT ALREADY