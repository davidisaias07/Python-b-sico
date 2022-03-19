#def run():
#    contador = 1
#    print(contador)
#    while contador < 1000:
#        contador += 1
#        print(contador)
#run()

#def run():
#    for numero in range (0,1001):
#        print(numero)
#run()



#for multiplicador in range (0,11):
#    print(11*multiplicador)
   

#Se coloca un número entre entre 1 al 100
#El número ingresado será multiplicado por 11, en el rango de (1,2), osea sólo se mostrará una vez
#La última condicion es colocar el número nuevo a ingresar
#En la última condicion se colocan 




def run():
    numero = int(input("Escribe un número entre el 1 al 100: "))
    for multiplicador in range(1,2):
        if numero == 6:
            break
        elif numero < 49:
            print(11*numero)
            continue
        elif numero > 50:
            print("Elije un número distinto a 6, menor a 49 y mayor a 50")
        numero = int(input("Escribe un número entre el 1 al 100: "))
        if numero == 6:
            break
        elif numero < 49:
            print(11*numero)
            continue
        elif numero > 50:
            print(11*numero)

      
run()




#Mientras el número sea menor a 5 que no se ejecute lo que está bajo el continue
#Si el número es mayor a 5 que se multiplique la tabla del 11 por el número ingresado
#Si la multiplicacion excede a 55, no se imprime y se corta el ciclo

#def run():
#    numero = float(input("Escribe un número entre 1 al 100: "))
#    while numero > 5:
#        numero = float(input("Escribe un número menor a 5: "))
#        continue 
#    if numero < 5:
#        for multiplicador in range (1,2):
#            print(11*numero)
#            if numero < 55:
#                break   

#run()

#def run():
#    contador = 0
#    LIMITE = 50
#    suma_contador = contador + 1

#    while suma_contador < LIMITE:
#        print(suma_contador)
#        contador = contador + 1
#        suma_contador = contador + 1
#        if suma_contador == 30:
#            break
#        
#run()