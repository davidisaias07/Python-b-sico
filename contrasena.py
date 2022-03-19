import random

def generar_contrasena():
    minusculas = ["a","b","c","d"]
    mayusculas = ["A","B","C","D"]
    simbolos = ["!","*","-","+"]
    numeros = ["1","2","3","4"]

    caracteres = minusculas + mayusculas + simbolos + numeros
    
    contrasena = []

    for i in range (15):
        eleccion_aleatoria = random.choice(caracteres)
        contrasena.append(eleccion_aleatoria)

    contrasena = "".join(contrasena)
    return contrasena



def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es : " + contrasena)


run()