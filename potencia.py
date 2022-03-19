
#Lo que está después del while se sigue ejecutando hasta que el LIMITE sea mayor que 1000
#El contador represta al número elevado del 2
# ** significa potencia
#No importa el orden de las 3 primeras variables

def run():

    LIMITE = 1000
    
    contador = 0

    potencia_dos = 2 ** contador

    while potencia_dos < LIMITE:
        print("2 elevado a " + str(contador) + "es igual a : " + str(potencia_dos))
        contador = contador + 1
        potencia_dos = 2 ** contador

run()
    