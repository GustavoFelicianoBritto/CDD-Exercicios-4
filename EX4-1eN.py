# n=-1
# while n <0:
n = int(input("Digite um valor: "))
if n<=0:
    print("Valor incorreto (Número precisa ser maior que 0)")
else:
    for i in range (1,n+1,1):
        print(i, end=" ")