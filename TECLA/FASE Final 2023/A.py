# Leitura dos Dados
p1, p2 = map(int, input().split())
c1, c2 = map(int, input().split())

nota = c1 * (p1 / 100) + c2 * (p2 / 100) # Soma do peso das notas

print("%.2f"%nota) # Arredondamento a duas casas decimais