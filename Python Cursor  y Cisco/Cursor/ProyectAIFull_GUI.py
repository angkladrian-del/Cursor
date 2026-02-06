"""
Calculadora Científica - Interfaz gráfica
Tkinter - Sin dependencias externas
"""

import math
import tkinter as tk
from tkinter import ttk, messagebox


class CalculadoraCientificaGUI:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora Científica")
        self.ventana.minsize(420, 520)
        self.ventana.configure(bg="#1e2a38")

        # Estilo
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "TFrame", background="#1e2a38",
        )
        estilo.configure(
            "TLabel",
            background="#1e2a38",
            foreground="#e8e8e8",
            font=("Segoe UI", 10),
        )
        estilo.configure(
            "TCombobox",
            fieldbackground="#2d3e50",
            background="#2d3e50",
            foreground="#e8e8e8",
            font=("Segoe UI", 10),
        )
        estilo.configure(
            "TButton",
            font=("Segoe UI", 10),
            padding=(12, 6),
        )
        estilo.map("TCombobox", fieldbackground=[("readonly", "#2d3e50")])

        # Contenedor principal
        main = ttk.Frame(self.ventana, padding=20)
        main.pack(fill=tk.BOTH, expand=True)

        # Título
        titulo = tk.Label(
            main,
            text="Calculadora Científica",
            font=("Segoe UI", 18, "bold"),
            fg="#4fc3f7",
            bg="#1e2a38",
        )
        titulo.pack(pady=(0, 20))

        # Selector de operación
        tk.Label(main, text="Operación:", font=("Segoe UI", 10), fg="#e8e8e8", bg="#1e2a38").pack(anchor=tk.W)
        self.operaciones = [
            "Suma",
            "Resta",
            "Multiplicación",
            "División",
            "Raíz cuadrada (√x)",
            "Raíz n-ésima (ⁿ√x)",
            "Ecuación cuadrática (ax² + bx + c = 0)",
            "Seno (sin)",
            "Coseno (cos)",
            "Tangente (tan)",
            "Arcoseno (arcsin)",
            "Arcocoseno (arccos)",
            "Arcotangente (arctan)",
        ]
        self.combo = ttk.Combobox(
            main,
            values=self.operaciones,
            state="readonly",
            width=42,
            font=("Segoe UI", 10),
        )
        self.combo.set(self.operaciones[0])
        self.combo.pack(pady=(4, 16), fill=tk.X)
        self.combo.bind("<<ComboboxSelected>>", self._cambiar_campos)

        # Frame dinámico para entradas
        self.frame_entradas = ttk.Frame(main)
        self.frame_entradas.pack(fill=tk.X, pady=(0, 16))

        # Entradas (se crean según la operación)
        self.entradas = {}
        self._crear_campos()

        # Botón Calcular
        self.btn_calcular = tk.Button(
            main,
            text="Calcular",
            font=("Segoe UI", 11, "bold"),
            fg="#1e2a38",
            bg="#4fc3f7",
            activebackground="#29b6f6",
            activeforeground="#1e2a38",
            relief=tk.FLAT,
            padx=24,
            pady=10,
            cursor="hand2",
            command=self._calcular,
        )
        self.btn_calcular.pack(pady=(0, 16))

        # Resultado
        tk.Label(main, text="Resultado:", font=("Segoe UI", 10), fg="#e8e8e8", bg="#1e2a38").pack(anchor=tk.W)
        self.resultado = tk.Text(
            main,
            height=6,
            width=48,
            font=("Consolas", 10),
            bg="#2d3e50",
            fg="#a5d6a7",
            insertbackground="#e8e8e8",
            relief=tk.FLAT,
            padx=10,
            pady=10,
        )
        self.resultado.pack(pady=(4, 0), fill=tk.BOTH, expand=True)

    def _limpiar_entradas(self):
        for w in self.frame_entradas.winfo_children():
            w.destroy()
        self.entradas.clear()

    def _crear_campo(self, padre, etiqueta, clave, default=""):
        f = ttk.Frame(padre)
        f.pack(fill=tk.X, pady=4)
        ttk.Label(f, text=etiqueta, width=22, anchor=tk.W).pack(side=tk.LEFT, padx=(0, 8))
        e = tk.Entry(
            f,
            font=("Segoe UI", 10),
            bg="#2d3e50",
            fg="#e8e8e8",
            insertbackground="#e8e8e8",
            relief=tk.FLAT,
            width=20,
        )
        e.insert(0, default)
        e.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=4, ipadx=6)
        self.entradas[clave] = e

    def _crear_campos(self):
        self._limpiar_entradas()
        op = self.combo.get()
        if op == "Suma":
            self._crear_campo(self.frame_entradas, "Primer sumando (a):", "a")
            self._crear_campo(self.frame_entradas, "Segundo sumando (b):", "b")
        elif op == "Resta":
            self._crear_campo(self.frame_entradas, "Minuendo (a):", "a")
            self._crear_campo(self.frame_entradas, "Sustraendo (b):", "b")
        elif op == "Multiplicación":
            self._crear_campo(self.frame_entradas, "Primer factor (a):", "a")
            self._crear_campo(self.frame_entradas, "Segundo factor (b):", "b")
        elif op == "División":
            self._crear_campo(self.frame_entradas, "Dividendo (a):", "a")
            self._crear_campo(self.frame_entradas, "Divisor (b):", "b")
        elif op == "Raíz cuadrada (√x)":
            self._crear_campo(self.frame_entradas, "Número (x):", "x")
        elif op == "Raíz n-ésima (ⁿ√x)":
            self._crear_campo(self.frame_entradas, "Índice (n):", "n")
            self._crear_campo(self.frame_entradas, "Radicando (x):", "x")
        elif op == "Ecuación cuadrática (ax² + bx + c = 0)":
            self._crear_campo(self.frame_entradas, "Coeficiente a:", "a")
            self._crear_campo(self.frame_entradas, "Coeficiente b:", "b")
            self._crear_campo(self.frame_entradas, "Coeficiente c:", "c")
        elif op in ("Seno (sin)", "Coseno (cos)", "Tangente (tan)"):
            self._crear_campo(self.frame_entradas, "Ángulo:", "ang")
            self._crear_campo(self.frame_entradas, "¿En grados? (1=sí, 0=rad):", "grados", "1")
        elif op in ("Arcoseno (arcsin)", "Arcocoseno (arccos)", "Arcotangente (arctan)"):
            self._crear_campo(self.frame_entradas, "Valor (x):", "x")
            self._crear_campo(self.frame_entradas, "Resultado en grados? (1=sí, 0=rad):", "grados", "1")

    def _cambiar_campos(self, event=None):
        self._crear_campos()

    def _leer(self, clave):
        return float(self.entradas[clave].get().strip().replace(",", "."))

    def _leer_int(self, clave):
        return int(self.entradas[clave].get().strip())

    def _mostrar(self, texto):
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, texto)

    def _calcular(self):
        op = self.combo.get()
        try:
            if op == "Suma":
                a, b = self._leer("a"), self._leer("b")
                self._mostrar(f"{a} + {b} = {a + b}")
            elif op == "Resta":
                a, b = self._leer("a"), self._leer("b")
                self._mostrar(f"{a} - {b} = {a - b}")
            elif op == "Multiplicación":
                a, b = self._leer("a"), self._leer("b")
                self._mostrar(f"{a} × {b} = {a * b}")
            elif op == "División":
                a, b = self._leer("a"), self._leer("b")
                if b == 0:
                    messagebox.showerror("Error", "No se puede dividir entre cero.")
                    return
                self._mostrar(f"{a} ÷ {b} = {a / b}")
            elif op == "Raíz cuadrada (√x)":
                x = self._leer("x")
                if x < 0:
                    messagebox.showerror("Error", "No existe raíz cuadrada real de un número negativo.")
                    return
                r = math.sqrt(x)
                self._mostrar(f"√{x} = {r}")
            elif op == "Raíz n-ésima (ⁿ√x)":
                n = self._leer("n")
                x = self._leer("x")
                if n <= 0:
                    messagebox.showerror("Error", "El índice debe ser positivo.")
                    return
                if n % 2 == 0 and x < 0:
                    messagebox.showerror("Error", "No existe raíz real par de un número negativo.")
                    return
                r = x ** (1 / n)
                self._mostrar(f"{int(n)}√{x} = {r}")
            elif op == "Ecuación cuadrática (ax² + bx + c = 0)":
                a, b, c = self._leer("a"), self._leer("b"), self._leer("c")
                if a == 0:
                    messagebox.showerror("Error", "El coeficiente 'a' no puede ser 0.")
                    return
                d = b * b - 4 * a * c
                if d > 0:
                    x1 = (-b + math.sqrt(d)) / (2 * a)
                    x2 = (-b - math.sqrt(d)) / (2 * a)
                    self._mostrar(f"Dos soluciones reales:\nx₁ = {x1}\nx₂ = {x2}")
                elif d == 0:
                    x = -b / (2 * a)
                    self._mostrar(f"Una solución (raíz doble):\nx = {x}")
                else:
                    re = -b / (2 * a)
                    im = math.sqrt(-d) / (2 * a)
                    self._mostrar(f"Soluciones complejas:\nx₁ = {re} + {im}i\nx₂ = {re} - {im}i")
            elif op == "Seno (sin)":
                ang, grados = self._leer("ang"), self._leer_int("grados")
                rad = math.radians(ang) if grados else ang
                r = math.sin(rad)
                u = "°" if grados else " rad"
                self._mostrar(f"sin({ang}{u}) = {r}")
            elif op == "Coseno (cos)":
                ang, grados = self._leer("ang"), self._leer_int("grados")
                rad = math.radians(ang) if grados else ang
                r = math.cos(rad)
                u = "°" if grados else " rad"
                self._mostrar(f"cos({ang}{u}) = {r}")
            elif op == "Tangente (tan)":
                ang, grados = self._leer("ang"), self._leer_int("grados")
                rad = math.radians(ang) if grados else ang
                if math.cos(rad) == 0:
                    messagebox.showerror("Error", "La tangente no está definida para este ángulo.")
                    return
                r = math.tan(rad)
                u = "°" if grados else " rad"
                self._mostrar(f"tan({ang}{u}) = {r}")
            elif op == "Arcoseno (arcsin)":
                x, grados = self._leer("x"), self._leer_int("grados")
                if not -1 <= x <= 1:
                    messagebox.showerror("Error", "El valor debe estar entre -1 y 1.")
                    return
                r = math.asin(x)
                if grados:
                    r = math.degrees(r)
                    self._mostrar(f"arcsin({x}) = {r}°")
                else:
                    self._mostrar(f"arcsin({x}) = {r} rad")
            elif op == "Arcocoseno (arccos)":
                x, grados = self._leer("x"), self._leer_int("grados")
                if not -1 <= x <= 1:
                    messagebox.showerror("Error", "El valor debe estar entre -1 y 1.")
                    return
                r = math.acos(x)
                if grados:
                    r = math.degrees(r)
                    self._mostrar(f"arccos({x}) = {r}°")
                else:
                    self._mostrar(f"arccos({x}) = {r} rad")
            elif op == "Arcotangente (arctan)":
                x, grados = self._leer("x"), self._leer_int("grados")
                r = math.atan(x)
                if grados:
                    r = math.degrees(r)
                    self._mostrar(f"arctan({x}) = {r}°")
                else:
                    self._mostrar(f"arctan({x}) = {r} rad")
        except ValueError:
            messagebox.showerror("Error", "Introduce valores numéricos válidos en todos los campos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def ejecutar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    app = CalculadoraCientificaGUI()
    app.ejecutar()
