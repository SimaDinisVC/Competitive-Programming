K = int(input()) # km da pista
V = int(input()) # nº de voltas
C = int(input()) # Consumo por 100 Km
M = int(input()) # margem de segurança

print("%.1f"%(((((K*V))*C)/100)*(M/100)))