N, M = map(int, input().split())
c = list(map(int, input().split()))
c = set(c)
print(N-len(c))