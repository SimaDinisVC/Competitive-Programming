cb, st, env = input().split()

cbs = {"normal": 65, "frequente": 120 }
sts = {"normal": 0, "expresso": 20, "urgente": 30, "aeroporto": 35}
envs = {"normal": 0, "Portugal": 10, "estrangeiro": 30}

print(f"{cbs[cb] + sts[st] + envs[env]} Euros")