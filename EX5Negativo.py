qtd=0
for i in range (1,5,1):
    num = int(input(f"Insira o {i}º valor:"))
    if num<0:
        qtd+=1
        #print(f"O número {i} é negativo")

print(f"{qtd} dos valores foram negativos")