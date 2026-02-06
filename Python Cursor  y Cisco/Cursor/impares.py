

respuesta = "s"

while respuesta == "s":

    numero = int(input("Ingrese un numero: "))
    
    if numero %2 !=0:
        print("El numero es impar")
    else:
        print("El numero es par")

    respuesta = input("Desea continuar? (s/n): ")
