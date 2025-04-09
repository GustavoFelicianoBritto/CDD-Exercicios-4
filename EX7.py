soma=0
for i in range (1,6):
    valores=float(input(f"Digite o {i} º valor: ").replace(',','.'))
    soma= soma+valores

media = soma /5

print(f"A média é: {media:.1f}")
