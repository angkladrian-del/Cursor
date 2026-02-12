import random

# Genera el número secreto entre 1 y 200
secreto = random.randint(1, 200)

intentos = 0
while True:
    try:
        a = int(input("Ingrese un valor entre 1 y 200: "))
    except ValueError:
        print("Entrada no válida — escribe un entero.")
        continue

    if not (1 <= a <= 200):
        print("El número debe estar entre 1 y 200.")
        continue

    intentos += 1

    if a == secreto:
        print(f"¡Adivinaste! El número era {secreto}. Intentos: {intentos}.")
        break
    else:
        diferencia = abs(a - secreto)
        porcentaje = diferencia / 200 * 100
        print(f"No acertaste. Estás a {diferencia} unidades ({porcentaje:.2f}% del rango). Sigue intentando.")
