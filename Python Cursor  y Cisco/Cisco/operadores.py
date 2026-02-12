print(10 + 10)
print(10 - 5)
print(10 * 2)
print(10 / 2)
print(10 % 3)
print(10 ** 2)

# Operador unario +
print(+5)  # Resultado: 5
print(+(-3))  # Resultado: -3

# Nota: Los operadores unarios a la derecha del operador exponencial enlazan con mayor fuerza
print(2 ** +3)  # Se evalúa como 2**(+3) = 8
print(2 ** -2)  # Se evalúa como 2**(-2) = 0.25
print(-2 ** 2)  # Se evalúa como -(2**2) = -4 (el unario a la izquierda tiene menor precedencia)

