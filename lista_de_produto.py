import os
import time

lista = []

while True:
    print("Selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]istar: ").lower()

    if opcao == "i":
        valor = input("Valor: ")
        lista.append(valor)
        time.sleep(0.5)
        os.system("cls")
    elif opcao == "a":
        try:
            valor = int(input("Escolha o índice para apagar: "))
            del lista[valor - 1]
            time.sleep(0.5)
            os.system("cls")
        except IndexError:
            print("Índice inexistente")
            time.sleep(0.5)
            os.system("cls")
            continue
    elif opcao == "l":
        if not lista:
            print("Lista vazia")
        else:
            for indice, valor in enumerate(lista):
                print(indice + 1, valor)
