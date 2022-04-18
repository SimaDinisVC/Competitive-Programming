# THIS CODE IS AN EXPERIMENT AND IT IS NOT ALREADY
def add(planes, pairs):
    coord = []
    for i in planes:
        coord.append(list([planes[i][0], planes[i][1]]))
    for i in coord:
        if coord.count(i)>1:
            indexs = list([o+1 for o, item in enumerate(coord) if item == i])
            print(indexs)
            for o in indexs:
                    for l in indexs:
                        if (o,l) not in pairs and (l,o) not in pairs and (o,o) not in pairs and (l,l) not in pairs:
                            pairs.append((o,l))
            print(pairs)
            indexs.clear()
    return pairs   

n, m, k = map(int, input().split())
planes = {}
clouds = []
pairs = []
for c in range(n):
    x, y = map(int, input().split())
    planes[len(planes)+1] = [x,y,'E']
for c in range(m):
    x, y = map(int, input().split())
    clouds.append([x,y])

for i in range(k):
    for key in planes:
        facing = planes[key][2]
        if facing == 'E':
            if list([planes[key][0]+1,planes[key][1]]) in clouds:
                planes[key][2] = 'S'
            else:
                planes[key][0] += 1
            pairs = add(planes,pairs)
        elif facing == 'S':
            if list([planes[key][0],planes[key][1]-1]) in clouds:
                planes[key][2] = 'O'
            else:
                planes[key][1] -= 1
            pairs = add(planes,pairs)
        elif facing == 'O':
            if list([planes[key][0]-1,planes[key][1]]) in clouds:
                planes[key][2] = 'S'
            else:
                planes[key][0] -= 1
            pairs = add(planes,pairs)
        elif facing == 'N':
            if list([planes[key][0],planes[key][1]+1]) in clouds:
                planes[key][2] = 'S'
            else:
                planes[key][1] += 1
            pairs = add(planes,pairs)
print(len(pairs))

# THIS CODE IS AN EXPERIMENT AND IT IS NOT ALREADY