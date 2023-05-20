n, k = map(int, input().split())
verifier = 0
for i in range(n):
    string = input()
    if '.'*k in string:
        verifier = 1
print(verifier)