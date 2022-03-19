def run():
    poblacion_pais = {
        "Perú": 12000,
        "Holanda": 35000,
        "Rusia": 95200
    }

    #Imprime el primer campo, solo población:
    #Osea la cantidad de habitantes, no menciona al país
    #print(poblacion_pais["Perú"])

    

    #Imprime los países sin sus valores
    #for pais in poblacion_pais.keys():
    #    print(pais)



    #Imprime los habitantes por país sin mencionar a los países
    #for pais in poblacion_pais.values():
    #    print(pais)



    #Imprime ambos valores
    #Dos condiciones en el for
    #Nuestro rango es poblacion_pais
    #Pasar a str(poblacion) porque es un numero
    for pais,poblacion in poblacion_pais.items():
        print(pais + " tiene " + str(poblacion) + " habitantes")



run()