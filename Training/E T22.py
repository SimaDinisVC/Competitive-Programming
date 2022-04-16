# THIS CODE IS AN EXPERIMENT AND IT IS NOT ALREADY

n, m, k = map(int, input().split())
planes = []
clouds = []
counter = -1
pairs = 0
for c in range(n):
    x, y = map(int, input().split())
    planes.append([x,y,'E'])
for c in range(m):
    x, y = map(int, input().split())
    clouds.append([x,y])

print(planes)

for i in range(k):
    for i in planes:
        counter += 1
        if i == None:
            break
        if i[2] == 'E':
            ii = [i[0] + 1, i[1]]
            if ii in clouds:
                planes[counter][2] = 'S'
            else:
                planes[counter] = ii.append('E')
        if i[2] == 'S':
            ii = [i[0], i[1] - 1]
            if ii in clouds:
                planes[counter][2] = 'O'
            else:
                planes[counter] = ii.append('S')
        if i[2] == 'O':
            ii = [i[0] - 1, i[1]]
            if ii in clouds:
                planes[counter][2] = 'N'
            else:
                planes[counter] = ii.append('O')
        if i[2] == 'N':
            ii = [i[0], i[1] + 1]
            if ii in clouds:
                planes[counter][2] = 'E'
                ii = [i[0] + 1, i[1]]
                if ii in clouds:
                    planes[counter][2] = 'S'
                else:
                    planes[counter] = ii.append('E')
            else:
                planes[counter] = ii.append('N')
    for i in planes:
        if planes.count(i) > 1:
            pairs += planes.count(i)//2

print(pairs)

# THIS CODE IS AN EXPERIMENT AND IT IS NOT ALREADY