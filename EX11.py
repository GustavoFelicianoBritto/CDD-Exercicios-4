option = 0
oper=""
while option != 6:
    num = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado=0
    option = int(input(f"1 - soma\n2 - Subtração\n3 - multiplicação\n"
                   f"4 - Divisão\n5 - Novos números\n6 - Sair\nDigite a opção que deseja seguir: "))

    if option== 6:
        print("Saindo")
        break
    elif option==5:
        print("Escolha novos números")
    elif option == 1:
        oper ="soma"
        resultado= num+num2
        print(f"O resultado da {oper} entre {num} e {num2} foi: {resultado}\n")
    elif option == 2:
        oper = "subtração"
        resultado = num - num2
        print(f"O resultado da {oper} entre {num} e {num2} foi: {resultado}\n")
    elif option == 3:
        oper = "multiplicação"
        resultado = num * num2
        print(f"O resultado da {oper} entre {num} e {num2} foi: {resultado}\n")
    elif option == 4:
        oper = "divisão"
        resultado = (num / num2)
        print(f"O resultado da {oper} entre {num} e {num2} foi: {resultado}\n")