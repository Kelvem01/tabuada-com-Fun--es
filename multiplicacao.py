def multiplicacao():
    global opcao
    numero = float(input("digite um numero : "))
    numero1 = float(input("Digite outro numero: "))

    valor = numero * numero1

    print(f"o valor da multiplicação é {valor}")
    print()
    opcao2 = int(input("deseja continuar? 1) sim 2) não :"))

    while True:
        if opcao2 == 1:
            numero = float(input("digite um numero : "))
            numero1 = float(input("Digite outro numero: "))
            
            valor = numero * numero1
            
            print(f"o valor da multiplicação é {valor}")
            print()
            opcao2 = int(input("(função) deseja continuar? 1) sim 2) não :"))
            
        elif opcao2 == 2:
            print("Tabuada de Multiplicação finalizado agradeço a preferencia , até logo")
            print ()
            break

        else:
            print("opção invalida !, até logo ")
            break
