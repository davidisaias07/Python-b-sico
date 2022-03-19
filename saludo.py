def conversacion(saludo):
    print("Hola cómo estás")
    print("Bienvenido al curso de python")
    print(saludo)
    print("Adiós")


opcion = int(input("Elije una opción entre 1, 2 y 3: "))

if opcion == 1:
    conversacion("Un gusto David")

elif opcion == 2:
    conversacion("Un gusto Isaías")   

elif opcion == 3:
    conversacion("Un gusto Jairo")

else:
    print("Elije una opción entre 1, 2 y 3: ")  