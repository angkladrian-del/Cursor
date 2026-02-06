print(2e6)
print(1e-22)

# Por defecto, Python muestra números muy pequeños en notación científica
# Para ver la representación decimal completa, usa formato de cadena:

# Opción 1: Usando f-string con especificador de formato
print(f"{1e-22:.22f}")  # :.22f significa: 22 decimales en formato fijo

# Opción 2: Usando format() (método antiguo, antes de f-strings)
print("{:.22f}".format(1e-22))

# Opción 3: Usando notación científica con más precisión
print(f"{1e-22:.22e}")  # :.22e significa: 22 decimales en notación científica