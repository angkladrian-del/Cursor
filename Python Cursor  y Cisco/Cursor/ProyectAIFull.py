"""
Calculadora Científica
Operaciones: básicas, raíces, cuadráticas y trigonométricas
"""

import math


def leer_numero(mensaje="Ingrese un número: "):
    """Solicita un número válido al usuario."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  ⚠ Por favor, ingrese un número válido.\n")


def leer_numero_positivo(mensaje="Ingrese un número positivo: "):
    """Solicita un número positivo."""
    while True:
        n = leer_numero(mensaje)
        if n > 0:
            return n
        print("  ⚠ El número debe ser positivo.\n")


def suma():
    """Operación de suma."""
    a = leer_numero("Primer sumando: ")
    b = leer_numero("Segundo sumando: ")
    resultado = a + b
    print(f"\n  → {a} + {b} = {resultado}\n")


def resta():
    """Operación de resta."""
    a = leer_numero("Minuendo: ")
    b = leer_numero("Sustraendo: ")
    resultado = a - b
    print(f"\n  → {a} - {b} = {resultado}\n")


def multiplicacion():
    """Operación de multiplicación."""
    a = leer_numero("Primer factor: ")
    b = leer_numero("Segundo factor: ")
    resultado = a * b
    print(f"\n  → {a} × {b} = {resultado}\n")


def division():
    """Operación de división."""
    a = leer_numero("Dividendo: ")
    b = leer_numero("Divisor: ")
    if b == 0:
        print("\n  ⚠ Error: no se puede dividir entre cero.\n")
        return
    resultado = a / b
    print(f"\n  → {a} ÷ {b} = {resultado}\n")


def raiz_cuadrada():
    """Raíz cuadrada de un número."""
    n = leer_numero_positivo("Número para calcular √x: ")
    resultado = math.sqrt(n)
    print(f"\n  → √{n} = {resultado}\n")


def raiz_enesima():
    """Raíz n-ésima de un número (ⁿ√x)."""
    n = leer_numero_positivo("Índice de la raíz (n): ")
    x = leer_numero("Radicando (x): ")
    if n % 2 == 0 and x < 0:
        print("\n  ⚠ No existe raíz real par de un número negativo.\n")
        return
    resultado = x ** (1 / n)
    print(f"\n  → {int(n)}√{x} = {resultado}\n")


def ecuacion_cuadratica():
    """Resuelve ax² + bx + c = 0."""
    print("  Ecuación: ax² + bx + c = 0")
    a = leer_numero("Coeficiente a: ")
    if a == 0:
        print("\n  ⚠ Si a = 0 no es una ecuación cuadrática.\n")
        return
    b = leer_numero("Coeficiente b: ")
    c = leer_numero("Coeficiente c: ")
    discriminante = b * b - 4 * a * c
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print(f"\n  → Dos soluciones reales:")
        print(f"     x₁ = {x1}")
        print(f"     x₂ = {x2}\n")
    elif discriminante == 0:
        x = -b / (2 * a)
        print(f"\n  → Una solución real (raíz doble): x = {x}\n")
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-discriminante) / (2 * a)
        print(f"\n  → Dos soluciones complejas:")
        print(f"     x₁ = {real} + {imag}i")
        print(f"     x₂ = {real} - {imag}i\n")


def trig_grados():
    """Pregunta si el ángulo está en grados (por defecto) o radianes."""
    resp = input("  ¿Ángulo en grados? (s/n, por defecto s): ").strip().lower()
    return resp != "n"


def seno():
    """Seno del ángulo."""
    en_grados = trig_grados()
    ang = leer_numero("Ángulo: ")
    mostrar = ang
    if en_grados:
        ang = math.radians(ang)
    resultado = math.sin(ang)
    unidad = "°" if en_grados else " rad"
    print(f"\n  → sin({mostrar}{unidad}) = {resultado}\n")


def coseno():
    """Coseno del ángulo."""
    en_grados = trig_grados()
    ang = leer_numero("Ángulo: ")
    mostrar = ang
    if en_grados:
        ang = math.radians(ang)
    resultado = math.cos(ang)
    unidad = "°" if en_grados else " rad"
    print(f"\n  → cos({mostrar}{unidad}) = {resultado}\n")


def tangente():
    """Tangente del ángulo."""
    en_grados = trig_grados()
    ang = leer_numero("Ángulo: ")
    mostrar = ang
    if en_grados:
        ang = math.radians(ang)
    if math.cos(ang) == 0:
        print("\n  ⚠ La tangente no está definida para este ángulo (cos = 0).\n")
        return
    resultado = math.tan(ang)
    unidad = "°" if en_grados else " rad"
    print(f"\n  → tan({mostrar}{unidad}) = {resultado}\n")


def arcoseno():
    """Arcoseno (inversa del seno). Resultado en grados o radianes."""
    en_grados = trig_grados()
    x = leer_numero("Valor entre -1 y 1: ")
    if not -1 <= x <= 1:
        print("\n  ⚠ El dominio de arcsin es [-1, 1].\n")
        return
    resultado = math.asin(x)
    if en_grados:
        resultado = math.degrees(resultado)
        print(f"\n  → arcsin({x}) = {resultado}°\n")
    else:
        print(f"\n  → arcsin({x}) = {resultado} rad\n")


def arcocoseno():
    """Arcocoseno (inversa del coseno)."""
    en_grados = trig_grados()
    x = leer_numero("Valor entre -1 y 1: ")
    if not -1 <= x <= 1:
        print("\n  ⚠ El dominio de arccos es [-1, 1].\n")
        return
    resultado = math.acos(x)
    if en_grados:
        resultado = math.degrees(resultado)
        print(f"\n  → arccos({x}) = {resultado}°\n")
    else:
        print(f"\n  → arccos({x}) = {resultado} rad\n")


def arcotangente():
    """Arcotangente (inversa de la tangente)."""
    en_grados = trig_grados()
    x = leer_numero("Valor: ")
    resultado = math.atan(x)
    if en_grados:
        resultado = math.degrees(resultado)
        print(f"\n  → arctan({x}) = {resultado}°\n")
    else:
        print(f"\n  → arctan({x}) = {resultado} rad\n")


def mostrar_menu():
    """Muestra el menú principal."""
    print()
    print("  ═══════════════════════════════════════════")
    print("           CALCULADORA CIENTÍFICA")
    print("  ═══════════════════════════════════════════")
    print("  Operaciones básicas:")
    print("    1. Suma")
    print("    2. Resta")
    print("    3. Multiplicación")
    print("    4. División")
    print("  Raíces:")
    print("    5. Raíz cuadrada (√x)")
    print("    6. Raíz n-ésima (ⁿ√x)")
    print("  Cuadráticas:")
    print("    7. Ecuación cuadrática (ax² + bx + c = 0)")
    print("  Trigonometría:")
    print("    8. Seno (sin)")
    print("    9. Coseno (cos)")
    print("   10. Tangente (tan)")
    print("   11. Arcoseno (arcsin)")
    print("   12. Arcocoseno (arccos)")
    print("   13. Arcotangente (arctan)")
    print("  ───────────────────────────────────────────")
    print("    0. Salir")
    print("  ═══════════════════════════════════════════")
    print()


def main():
    """Bucle principal de la calculadora."""
    opciones = {
        "1": ("Suma", suma),
        "2": ("Resta", resta),
        "3": ("Multiplicación", multiplicacion),
        "4": ("División", division),
        "5": ("Raíz cuadrada", raiz_cuadrada),
        "6": ("Raíz n-ésima", raiz_enesima),
        "7": ("Ecuación cuadrática", ecuacion_cuadratica),
        "8": ("Seno", seno),
        "9": ("Coseno", coseno),
        "10": ("Tangente", tangente),
        "11": ("Arcoseno", arcoseno),
        "12": ("Arcocoseno", arcocoseno),
        "13": ("Arcotangente", arcotangente),
    }
    while True:
        mostrar_menu()
        opcion = input("  Elija una opción: ").strip()
        if opcion == "0":
            print("\n  Hasta luego.\n")
            break
        if opcion in opciones:
            nombre, funcion = opciones[opcion]
            print(f"\n  --- {nombre} ---")
            try:
                funcion()
            except Exception as e:
                print(f"\n  ⚠ Error: {e}\n")
        else:
            print("\n  ⚠ Opción no válida. Elija un número del menú.\n")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1].lower() in ("--gui", "-g", "gui"):
        from ProyectAIFull_GUI import CalculadoraCientificaGUI
        app = CalculadoraCientificaGUI()
        app.ejecutar()
    else:
        main()
