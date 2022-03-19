def run():
    texto = """
Encuentra el error en el texto, David tiene 24 años,
estudia psicología y vive en Ate,
Encuentra los errores en la frase: """

    respuesta = input(texto)

    intentos = 0
    
    while intentos < 3:
        intentos +=1
        if respuesta == "Tiene 25 años, vive en miraflores":   
            print("Acertaste, bien hecho")      
            break
        else:
            print("Tienes otros 4 intentos más, no te rindas")
            respuesta = input("Respuesta incorrecta: ")
    if intentos == 3:
        print("Se terminaron los intentos, vuelve a intentarlos en 5 minutos")
run()