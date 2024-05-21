estadoglobal = "Aprovado"
estadoambiente = "Aprovado"
estadosaude = "Aprovado"
estadoseguranca = "Aprovado"

inp = list(input().split(" "))

while inp != ["/"]:
    if inp[1] == "saude":
        if inp[2] == "-" and estadosaude == "Aprovado":
            estadosaude = "Pendente"
        elif inp[2] == "rep" and estadosaude in ["Aprovado", "Pendente"]:
            estadosaude = "Reprovado"
    elif inp[1] == "seguranca":
        if inp[2] == "-" and estadoseguranca == "Aprovado":
            estadoseguranca = "Pendente"
        elif inp[2] == "rep" and estadoseguranca in ["Aprovado", "Pendente"]:
            estadoseguranca = "Reprovado"
    elif inp[1] == "ambiente":
        if inp[2] == "-" and estadoambiente == "Aprovado":
            estadoambiente = "Pendente"
        elif inp[2] == "rep" and estadoambiente in ["Aprovado", "Pendente"]:
            estadoambiente = "Reprovado"
    inp = list(input().split(" "))

l = [estadoambiente, estadosaude, estadoseguranca]
        
if "Pendente" in l:
    estadoglobal = "Pendente"
if "Reprovado" in l:
    estadoglobal = "Reprovado"

print(estadoglobal+" "+estadoambiente+" "+estadosaude+" "+estadoseguranca)