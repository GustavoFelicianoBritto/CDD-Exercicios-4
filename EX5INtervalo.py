inRange=0
outRange=0
for i in range(1,11,1):
    num=int(input(f"Digite o {i}º valor: "))
    if num >=10 and num <=20:
        inRange+=1
    else:
        outRange+=1
print(f"Números dentro dos limites: {inRange}\nNúmeros fora dos limites: {outRange}")
