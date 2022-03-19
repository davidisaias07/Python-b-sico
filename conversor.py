#Primero siempre va la función 
#Se asigno valores a la funcion: tipo_peso y valor_dolar 
#tipo_moneda va después de la función 
#Importante poner dos puntos después de caca condicional 
#Elif se usa como segunda negación, else como última condición 
#Los == significan igualidad 
#No se coloca run() porque la función es calculo y se está ejecutando en cada condicional


def calculo(tipo_peso, valor_dolar):
    pesos = float(input("Cuántos " + tipo_peso + " tienes?: "))
    conversion = str(round((pesos/valor_dolar),2))
    print("Tienes $ " + conversion + " dólares")



tipo_moneda = input("Escribe una opción entre 1, 2 y 3: ")



if tipo_moneda == "1":
    calculo("colombianos", 4.11)

elif tipo_moneda == "2":
    calculo("mexicanos", 5.11)

elif tipo_moneda == "3":
    calculo("argentinos", 6.11)

else:
    print("Elige una opción entre 1, 2 y 3: ")

