import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("Ingresa un número del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Elije un número más grande")
        else:
            print("Elije un número más pequeño")
        numero_elegido = int(input("Ingresa otro número: "))

    print("Ganaste")


run()