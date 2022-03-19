#Brinda números del 0 al 99

#a = list(range(100))
#print(a)




#Rango de 1 a 1000, si el contador es igual a 550, se corta el conteo

#for contador in range (1,1001):
#    print(contador)
#    if contador == 550:
#        break




#La tabla del 11*0 hasta el 11*9
#in range es desde el primer rango hasta un número antes del segundo rango

#for numero in range (0,10):
#   print(11*numero)



#Brinda letra por letra lo que se coloca en el input
#Despues del for puede ir cualquier variable, luego de la variable va lo que se analizará
#Si en nombre hay una letra que contiene una "d", se corta el nombre antes de la "d"

def run():
    nombre = input("Escribe un nombre: ")
    for letra in nombre:
        if letra == "d":
            break
        print(letra)
run()