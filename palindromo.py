#Crear primero la función para entenderla mejor 
#Lleva como parámetro a palabra que es la que se asignará en el input 
#Para crear un palíndromo, se debe eliminar espacios en blanco y debe estar en minúsculas 
#Importante colocar el ejecutor run() al final del código 
#Igualar la palabra == palabra invertida 
#Se crea la variable texto y se iguala a la verificar_palindromo(palabra) 
#Se iguala la variable texto a TRUE para comprobar si la palabra enviada por el input es palíndromo 
#La línea 30 es opcional y el run puede ir al mismo nivel que el def
#if texto == true significa que se ejecutará la función y retornará un true o un false
#por esa razon el texto se iguala a true o false

def verificacion_pindromo(palabra):
    palabra = palabra.replace(" ","").lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra = input("Ingresa una palabra: ")
    texto = verificacion_pindromo(palabra)
    if texto == True:
        print("Es palindromo")
    else:
        print("No es palindromo")    

run()





    
