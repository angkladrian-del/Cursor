print("Bienvenido a la Calculadora Básica")
print("Ingrese la tarea a realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potencia")
print("6. Raíz Cuadrada")

tarea = input("Ingrese la tarea a realizar:") 

match tarea:
    case "1":
        suma = 0
        print("Ingrese los números a sumar (presione Enter sin valor para terminar):")
        while True:
            entrada = input("Número: ")
            if entrada == "":
                break
            try:
                numero = float(entrada)
                suma += numero
            except ValueError:
                print("Por favor, ingrese un número válido.")
        print("El resultado de la suma es:", suma)
    case "2":
        resta = None # inicializa la variable resta en None, para que no se produzca un error de tipo NoneType
        primer_numero = True # inicializa la variable primer_numero en True, para que se pueda restar el primer número
        print("Ingrese los números a restar (presione Enter sin valor para terminar):")
        while True:
            entrada = input("Número: ")
            if entrada == "":
                break
            try:
                numero = float(entrada) # convierte el valor ingresado a un número flotante
                if primer_numero: # si es el primer número, se asigna a la variable resta
                    resta = numero
                    primer_numero = False # se cambia el valor de la variable primer_numero a False, para que no se pueda restar el primer número, es decir que no lo haga negativo desde el inicio
                else:
                    resta -= numero # se resta el número ingresado a la variable resta
            except ValueError:
                print("Por favor, ingrese un número válido.")
        if resta is None: # si la variable resta es None, se imprime un mensaje de error
            print("No se ingresaron números.")
        else:
            print("El resultado de la resta es:", resta)
    case "3":
        multiplicacion = 1 # inicializa la variable multiplicacion en 1, para que se pueda multiplicar el primer número
        print("Ingrese los números a multiplicar (presione Enter sin valor para terminar):")
        while True:
            entrada = input("Número: ")
            if entrada == "":
                break
            try:
                numero = float(entrada)
                multiplicacion *= numero
            except ValueError:
                print("Por favor, ingrese un número válido.")
        print("El resultado de la multiplicación es:", multiplicacion)
    case "4":
        division = None # inicializa la variable division en None, para que no se produzca un error de tipo NoneType
        primer_numero = True # inicializa la variable primer_numero en True, para que se pueda dividir el primer número
        print("Ingrese los números a dividir (presione Enter sin valor para terminar):")
        while True:
            entrada = input("Número: ")
            if entrada == "":
                break
            try:
                numero = float(entrada)
                if primer_numero:
                    division = numero
                    primer_numero = False
                else:
                    if numero == 0: # si el número ingresado es cero, se imprime un mensaje de error
                        print("No se puede dividir por cero. Ingrese otro número.")
                        continue
                    division /= numero
            except ValueError:
                print("Por favor, ingrese un número válido.")
            except ZeroDivisionError:
                print("No se puede dividir por cero. Ingrese otro número.")
        if division is None:
            print("No se ingresaron números.")
        else:
            print("El resultado de la división es:", division)
            