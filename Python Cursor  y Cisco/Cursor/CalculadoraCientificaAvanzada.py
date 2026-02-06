"""
Calculadora Científica Avanzada - Interfaz Gráfica Moderna
Incluye: Trigonometría, Logaritmos, Estadísticas, Conversiones, 
         Combinatoria, Funciones Hiperbólicas, Vectores y más.
Tkinter - Sin dependencias externas
"""

import math
import tkinter as tk
from tkinter import ttk, messagebox
from fractions import Fraction
import statistics


class CalculadoraCientificaAvanzada:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("🔬 Calculadora Científica Avanzada")
        self.ventana.minsize(520, 680)
        self.ventana.configure(bg="#0d1117")
        
        # Variables de memoria y historial
        self.memoria = 0
        self.historial = []
        self.ultima_respuesta = 0

        # Configurar estilo
        self._configurar_estilo()
        
        # Contenedor principal con scroll
        self._crear_interfaz()

    def _configurar_estilo(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("TFrame", background="#0d1117")
        estilo.configure("TLabel", background="#0d1117", foreground="#c9d1d9", font=("Segoe UI", 10))
        estilo.configure("TCombobox", fieldbackground="#21262d", background="#21262d", 
                        foreground="#c9d1d9", font=("Segoe UI", 10))
        estilo.configure("TButton", font=("Segoe UI", 10), padding=(12, 6))
        estilo.configure("TNotebook", background="#0d1117")
        estilo.configure("TNotebook.Tab", background="#21262d", foreground="#c9d1d9", 
                        font=("Segoe UI", 9, "bold"), padding=(10, 5))
        estilo.map("TCombobox", fieldbackground=[("readonly", "#21262d")])
        estilo.map("TNotebook.Tab", background=[("selected", "#238636")], 
                  foreground=[("selected", "#ffffff")])

    def _crear_interfaz(self):
        # Frame principal
        main = ttk.Frame(self.ventana, padding=15)
        main.pack(fill=tk.BOTH, expand=True)

        # Título
        titulo = tk.Label(main, text="🔬 Calculadora Científica Avanzada",
                         font=("Segoe UI", 16, "bold"), fg="#58a6ff", bg="#0d1117")
        titulo.pack(pady=(0, 10))

        # Barra de memoria y ANS
        frame_memoria = ttk.Frame(main)
        frame_memoria.pack(fill=tk.X, pady=(0, 10))
        
        self.lbl_memoria = tk.Label(frame_memoria, text="M: 0", font=("Consolas", 9),
                                    fg="#8b949e", bg="#0d1117")
        self.lbl_memoria.pack(side=tk.LEFT)
        
        self.lbl_ans = tk.Label(frame_memoria, text="ANS: 0", font=("Consolas", 9),
                                fg="#8b949e", bg="#0d1117")
        self.lbl_ans.pack(side=tk.RIGHT)

        # Notebook con pestañas de categorías
        self.notebook = ttk.Notebook(main)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # Crear pestañas
        self._crear_pestana_basicas()
        self._crear_pestana_trigonometria()
        self._crear_pestana_logaritmos()
        self._crear_pestana_estadisticas()
        self._crear_pestana_combinatoria()
        self._crear_pestana_conversiones()
        self._crear_pestana_avanzadas()

        # Frame de resultado
        frame_resultado = ttk.Frame(main)
        frame_resultado.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(frame_resultado, text="📊 Resultado:", font=("Segoe UI", 10, "bold"),
                fg="#c9d1d9", bg="#0d1117").pack(anchor=tk.W)
        
        self.resultado = tk.Text(frame_resultado, height=5, font=("Consolas", 11),
                                bg="#161b22", fg="#7ee787", insertbackground="#c9d1d9",
                                relief=tk.FLAT, padx=12, pady=10)
        self.resultado.pack(fill=tk.BOTH, expand=True, pady=(5, 0))

        # Botones de memoria
        frame_btns = ttk.Frame(main)
        frame_btns.pack(fill=tk.X, pady=(10, 0))
        
        btns_memoria = [("MC", self._mem_clear), ("MR", self._mem_recall), 
                       ("M+", self._mem_add), ("M-", self._mem_sub), ("Historial", self._ver_historial)]
        
        for texto, cmd in btns_memoria:
            btn = tk.Button(frame_btns, text=texto, font=("Segoe UI", 9), 
                           fg="#c9d1d9", bg="#21262d", activebackground="#30363d",
                           relief=tk.FLAT, padx=10, pady=5, cursor="hand2", command=cmd)
            btn.pack(side=tk.LEFT, padx=2)

    def _crear_pestana(self, nombre):
        """Crea una pestaña y retorna el frame"""
        frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(frame, text=nombre)
        return frame

    def _crear_selector(self, padre, operaciones, variable):
        """Crea un selector de operaciones"""
        combo = ttk.Combobox(padre, textvariable=variable, values=operaciones,
                            state="readonly", font=("Segoe UI", 10))
        combo.set(operaciones[0])
        combo.pack(fill=tk.X, pady=(0, 10))
        return combo

    def _crear_entrada(self, padre, etiqueta, default=""):
        """Crea un campo de entrada con etiqueta"""
        frame = ttk.Frame(padre)
        frame.pack(fill=tk.X, pady=3)
        
        ttk.Label(frame, text=etiqueta, width=25, anchor=tk.W).pack(side=tk.LEFT)
        
        entrada = tk.Entry(frame, font=("Segoe UI", 10), bg="#21262d", fg="#c9d1d9",
                          insertbackground="#c9d1d9", relief=tk.FLAT, width=20)
        entrada.insert(0, default)
        entrada.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5, ipadx=8)
        return entrada

    def _crear_boton_calcular(self, padre, comando):
        """Crea botón de calcular estilizado"""
        btn = tk.Button(padre, text="⚡ Calcular", font=("Segoe UI", 11, "bold"),
                       fg="#ffffff", bg="#238636", activebackground="#2ea043",
                       relief=tk.FLAT, padx=20, pady=8, cursor="hand2", command=comando)
        btn.pack(pady=(15, 5))
        return btn

    # ==================== PESTAÑA: OPERACIONES BÁSICAS ====================
    def _crear_pestana_basicas(self):
        frame = self._crear_pestana("➕ Básicas")
        
        ops = ["Suma (a + b)", "Resta (a - b)", "Multiplicación (a × b)", "División (a ÷ b)",
               "Potencia (a^b)", "Raíz cuadrada (√x)", "Raíz n-ésima (ⁿ√x)", "Módulo (a % b)",
               "Valor absoluto |x|", "Inverso (1/x)", "Porcentaje (a% de b)",
               "Incremento porcentual", "Fracción simplificada"]
        
        self.var_basica = tk.StringVar()
        self.combo_basica = self._crear_selector(frame, ops, self.var_basica)
        self.combo_basica.bind("<<ComboboxSelected>>", self._actualizar_basicas)
        
        self.frame_basicas = ttk.Frame(frame)
        self.frame_basicas.pack(fill=tk.X)
        
        self.entradas_basicas = {}
        self._actualizar_basicas()
        
        self._crear_boton_calcular(frame, self._calcular_basica)

    def _actualizar_basicas(self, event=None):
        for w in self.frame_basicas.winfo_children():
            w.destroy()
        self.entradas_basicas.clear()
        
        op = self.var_basica.get()
        if op in ["Suma (a + b)", "Resta (a - b)", "Multiplicación (a × b)", 
                  "División (a ÷ b)", "Potencia (a^b)", "Módulo (a % b)"]:
            self.entradas_basicas["a"] = self._crear_entrada(self.frame_basicas, "Valor a:")
            self.entradas_basicas["b"] = self._crear_entrada(self.frame_basicas, "Valor b:")
        elif op in ["Raíz cuadrada (√x)", "Valor absoluto |x|", "Inverso (1/x)"]:
            self.entradas_basicas["x"] = self._crear_entrada(self.frame_basicas, "Valor x:")
        elif op == "Raíz n-ésima (ⁿ√x)":
            self.entradas_basicas["n"] = self._crear_entrada(self.frame_basicas, "Índice n:")
            self.entradas_basicas["x"] = self._crear_entrada(self.frame_basicas, "Radicando x:")
        elif op == "Porcentaje (a% de b)":
            self.entradas_basicas["a"] = self._crear_entrada(self.frame_basicas, "Porcentaje (%):")
            self.entradas_basicas["b"] = self._crear_entrada(self.frame_basicas, "Valor base:")
        elif op == "Incremento porcentual":
            self.entradas_basicas["inicial"] = self._crear_entrada(self.frame_basicas, "Valor inicial:")
            self.entradas_basicas["final"] = self._crear_entrada(self.frame_basicas, "Valor final:")
        elif op == "Fracción simplificada":
            self.entradas_basicas["num"] = self._crear_entrada(self.frame_basicas, "Numerador:")
            self.entradas_basicas["den"] = self._crear_entrada(self.frame_basicas, "Denominador:")

    def _calcular_basica(self):
        try:
            op = self.var_basica.get()
            if op == "Suma (a + b)":
                a, b = float(self.entradas_basicas["a"].get()), float(self.entradas_basicas["b"].get())
                r = a + b
                self._mostrar(f"{a} + {b} = {r}")
            elif op == "Resta (a - b)":
                a, b = float(self.entradas_basicas["a"].get()), float(self.entradas_basicas["b"].get())
                r = a - b
                self._mostrar(f"{a} - {b} = {r}")
            elif op == "Multiplicación (a × b)":
                a, b = float(self.entradas_basicas["a"].get()), float(self.entradas_basicas["b"].get())
                r = a * b
                self._mostrar(f"{a} × {b} = {r}")
            elif op == "División (a ÷ b)":
                a, b = float(self.entradas_basicas["a"].get()), float(self.entradas_basicas["b"].get())
                if b == 0:
                    raise ValueError("División por cero")
                r = a / b
                self._mostrar(f"{a} ÷ {b} = {r}")
            elif op == "Potencia (a^b)":
                a, b = float(self.entradas_basicas["a"].get()), float(self.entradas_basicas["b"].get())
                r = a ** b
                self._mostrar(f"{a}^{b} = {r}")
            elif op == "Raíz cuadrada (√x)":
                x = float(self.entradas_basicas["x"].get())
                if x < 0:
                    raise ValueError("No existe raíz real de número negativo")
                r = math.sqrt(x)
                self._mostrar(f"√{x} = {r}")
            elif op == "Raíz n-ésima (ⁿ√x)":
                n = float(self.entradas_basicas["n"].get())
                x = float(self.entradas_basicas["x"].get())
                if n == 0:
                    raise ValueError("El índice no puede ser 0")
                r = x ** (1/n)
                self._mostrar(f"ⁿ√{x} (n={n}) = {r}")
            elif op == "Módulo (a % b)":
                a, b = float(self.entradas_basicas["a"].get()), float(self.entradas_basicas["b"].get())
                if b == 0:
                    raise ValueError("División por cero")
                r = a % b
                self._mostrar(f"{a} mod {b} = {r}")
            elif op == "Valor absoluto |x|":
                x = float(self.entradas_basicas["x"].get())
                r = abs(x)
                self._mostrar(f"|{x}| = {r}")
            elif op == "Inverso (1/x)":
                x = float(self.entradas_basicas["x"].get())
                if x == 0:
                    raise ValueError("División por cero")
                r = 1 / x
                self._mostrar(f"1/{x} = {r}")
            elif op == "Porcentaje (a% de b)":
                a = float(self.entradas_basicas["a"].get())
                b = float(self.entradas_basicas["b"].get())
                r = (a / 100) * b
                self._mostrar(f"{a}% de {b} = {r}")
            elif op == "Incremento porcentual":
                inicial = float(self.entradas_basicas["inicial"].get())
                final = float(self.entradas_basicas["final"].get())
                if inicial == 0:
                    raise ValueError("El valor inicial no puede ser 0")
                r = ((final - inicial) / inicial) * 100
                self._mostrar(f"Incremento: {r:.4f}%\nDe {inicial} a {final}")
            elif op == "Fracción simplificada":
                num = int(self.entradas_basicas["num"].get())
                den = int(self.entradas_basicas["den"].get())
                if den == 0:
                    raise ValueError("El denominador no puede ser 0")
                frac = Fraction(num, den)
                r = float(frac)
                self._mostrar(f"{num}/{den} = {frac.numerator}/{frac.denominator}\nDecimal: {r}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # ==================== PESTAÑA: TRIGONOMETRÍA ====================
    def _crear_pestana_trigonometria(self):
        frame = self._crear_pestana("📐 Trigonometría")
        
        ops = ["Seno (sin)", "Coseno (cos)", "Tangente (tan)",
               "Cosecante (csc)", "Secante (sec)", "Cotangente (cot)",
               "Arcoseno (asin)", "Arcocoseno (acos)", "Arcotangente (atan)",
               "Arcotangente 2 (atan2)", "Hipotenusa (a² + b² = c²)",
               "Seno hiperbólico (sinh)", "Coseno hiperbólico (cosh)", 
               "Tangente hiperbólica (tanh)",
               "Arcoseno hiperbólico (asinh)", "Arcocoseno hiperbólico (acosh)",
               "Arcotangente hiperbólica (atanh)"]
        
        self.var_trig = tk.StringVar()
        self.combo_trig = self._crear_selector(frame, ops, self.var_trig)
        self.combo_trig.bind("<<ComboboxSelected>>", self._actualizar_trig)
        
        self.frame_trig = ttk.Frame(frame)
        self.frame_trig.pack(fill=tk.X)
        
        self.entradas_trig = {}
        self._actualizar_trig()
        
        self._crear_boton_calcular(frame, self._calcular_trig)

    def _actualizar_trig(self, event=None):
        for w in self.frame_trig.winfo_children():
            w.destroy()
        self.entradas_trig.clear()
        
        op = self.var_trig.get()
        if op in ["Seno (sin)", "Coseno (cos)", "Tangente (tan)",
                  "Cosecante (csc)", "Secante (sec)", "Cotangente (cot)"]:
            self.entradas_trig["ang"] = self._crear_entrada(self.frame_trig, "Ángulo:")
            self.entradas_trig["grados"] = self._crear_entrada(self.frame_trig, "¿Grados? (1=sí, 0=rad):", "1")
        elif op in ["Arcoseno (asin)", "Arcocoseno (acos)", "Arcotangente (atan)"]:
            self.entradas_trig["x"] = self._crear_entrada(self.frame_trig, "Valor x:")
            self.entradas_trig["grados"] = self._crear_entrada(self.frame_trig, "Resultado en grados? (1/0):", "1")
        elif op == "Arcotangente 2 (atan2)":
            self.entradas_trig["y"] = self._crear_entrada(self.frame_trig, "Valor y:")
            self.entradas_trig["x"] = self._crear_entrada(self.frame_trig, "Valor x:")
            self.entradas_trig["grados"] = self._crear_entrada(self.frame_trig, "Resultado en grados? (1/0):", "1")
        elif op == "Hipotenusa (a² + b² = c²)":
            self.entradas_trig["a"] = self._crear_entrada(self.frame_trig, "Cateto a:")
            self.entradas_trig["b"] = self._crear_entrada(self.frame_trig, "Cateto b:")
        elif op in ["Seno hiperbólico (sinh)", "Coseno hiperbólico (cosh)", 
                    "Tangente hiperbólica (tanh)", "Arcoseno hiperbólico (asinh)",
                    "Arcocoseno hiperbólico (acosh)", "Arcotangente hiperbólica (atanh)"]:
            self.entradas_trig["x"] = self._crear_entrada(self.frame_trig, "Valor x:")

    def _calcular_trig(self):
        try:
            op = self.var_trig.get()
            
            if op in ["Seno (sin)", "Coseno (cos)", "Tangente (tan)",
                      "Cosecante (csc)", "Secante (sec)", "Cotangente (cot)"]:
                ang = float(self.entradas_trig["ang"].get())
                grados = int(self.entradas_trig["grados"].get())
                rad = math.radians(ang) if grados else ang
                u = "°" if grados else " rad"
                
                if op == "Seno (sin)":
                    r = math.sin(rad)
                    self._mostrar(f"sin({ang}{u}) = {r}")
                elif op == "Coseno (cos)":
                    r = math.cos(rad)
                    self._mostrar(f"cos({ang}{u}) = {r}")
                elif op == "Tangente (tan)":
                    r = math.tan(rad)
                    self._mostrar(f"tan({ang}{u}) = {r}")
                elif op == "Cosecante (csc)":
                    s = math.sin(rad)
                    if s == 0:
                        raise ValueError("Cosecante no definida")
                    r = 1 / s
                    self._mostrar(f"csc({ang}{u}) = {r}")
                elif op == "Secante (sec)":
                    c = math.cos(rad)
                    if c == 0:
                        raise ValueError("Secante no definida")
                    r = 1 / c
                    self._mostrar(f"sec({ang}{u}) = {r}")
                elif op == "Cotangente (cot)":
                    t = math.tan(rad)
                    if t == 0:
                        raise ValueError("Cotangente no definida")
                    r = 1 / t
                    self._mostrar(f"cot({ang}{u}) = {r}")
                    
            elif op in ["Arcoseno (asin)", "Arcocoseno (acos)", "Arcotangente (atan)"]:
                x = float(self.entradas_trig["x"].get())
                grados = int(self.entradas_trig["grados"].get())
                
                if op == "Arcoseno (asin)":
                    if not -1 <= x <= 1:
                        raise ValueError("x debe estar entre -1 y 1")
                    r = math.asin(x)
                elif op == "Arcocoseno (acos)":
                    if not -1 <= x <= 1:
                        raise ValueError("x debe estar entre -1 y 1")
                    r = math.acos(x)
                else:
                    r = math.atan(x)
                
                if grados:
                    r = math.degrees(r)
                    self._mostrar(f"{op.split()[0]}({x}) = {r}°")
                else:
                    self._mostrar(f"{op.split()[0]}({x}) = {r} rad")
                    
            elif op == "Arcotangente 2 (atan2)":
                y = float(self.entradas_trig["y"].get())
                x = float(self.entradas_trig["x"].get())
                grados = int(self.entradas_trig["grados"].get())
                r = math.atan2(y, x)
                if grados:
                    r = math.degrees(r)
                    self._mostrar(f"atan2({y}, {x}) = {r}°")
                else:
                    self._mostrar(f"atan2({y}, {x}) = {r} rad")
                    
            elif op == "Hipotenusa (a² + b² = c²)":
                a = float(self.entradas_trig["a"].get())
                b = float(self.entradas_trig["b"].get())
                r = math.hypot(a, b)
                self._mostrar(f"√({a}² + {b}²) = {r}")
                
            elif op == "Seno hiperbólico (sinh)":
                x = float(self.entradas_trig["x"].get())
                r = math.sinh(x)
                self._mostrar(f"sinh({x}) = {r}")
            elif op == "Coseno hiperbólico (cosh)":
                x = float(self.entradas_trig["x"].get())
                r = math.cosh(x)
                self._mostrar(f"cosh({x}) = {r}")
            elif op == "Tangente hiperbólica (tanh)":
                x = float(self.entradas_trig["x"].get())
                r = math.tanh(x)
                self._mostrar(f"tanh({x}) = {r}")
            elif op == "Arcoseno hiperbólico (asinh)":
                x = float(self.entradas_trig["x"].get())
                r = math.asinh(x)
                self._mostrar(f"asinh({x}) = {r}")
            elif op == "Arcocoseno hiperbólico (acosh)":
                x = float(self.entradas_trig["x"].get())
                if x < 1:
                    raise ValueError("x debe ser >= 1")
                r = math.acosh(x)
                self._mostrar(f"acosh({x}) = {r}")
            elif op == "Arcotangente hiperbólica (atanh)":
                x = float(self.entradas_trig["x"].get())
                if not -1 < x < 1:
                    raise ValueError("x debe estar entre -1 y 1 (exclusivo)")
                r = math.atanh(x)
                self._mostrar(f"atanh({x}) = {r}")
                
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # ==================== PESTAÑA: LOGARITMOS ====================
    def _crear_pestana_logaritmos(self):
        frame = self._crear_pestana("📈 Logaritmos")
        
        ops = ["Logaritmo natural (ln)", "Logaritmo base 10 (log₁₀)", 
               "Logaritmo base 2 (log₂)", "Logaritmo base n",
               "Exponencial (e^x)", "Potencia de 10 (10^x)", "Potencia de 2 (2^x)",
               "Logaritmo 1+x (log1p)", "Exponencial -1 (expm1)"]
        
        self.var_log = tk.StringVar()
        self.combo_log = self._crear_selector(frame, ops, self.var_log)
        self.combo_log.bind("<<ComboboxSelected>>", self._actualizar_log)
        
        self.frame_log = ttk.Frame(frame)
        self.frame_log.pack(fill=tk.X)
        
        self.entradas_log = {}
        self._actualizar_log()
        
        self._crear_boton_calcular(frame, self._calcular_log)

    def _actualizar_log(self, event=None):
        for w in self.frame_log.winfo_children():
            w.destroy()
        self.entradas_log.clear()
        
        op = self.var_log.get()
        if op == "Logaritmo base n":
            self.entradas_log["x"] = self._crear_entrada(self.frame_log, "Valor x:")
            self.entradas_log["base"] = self._crear_entrada(self.frame_log, "Base:")
        else:
            self.entradas_log["x"] = self._crear_entrada(self.frame_log, "Valor x:")

    def _calcular_log(self):
        try:
            op = self.var_log.get()
            x = float(self.entradas_log["x"].get())
            
            if op == "Logaritmo natural (ln)":
                if x <= 0:
                    raise ValueError("x debe ser positivo")
                r = math.log(x)
                self._mostrar(f"ln({x}) = {r}")
            elif op == "Logaritmo base 10 (log₁₀)":
                if x <= 0:
                    raise ValueError("x debe ser positivo")
                r = math.log10(x)
                self._mostrar(f"log₁₀({x}) = {r}")
            elif op == "Logaritmo base 2 (log₂)":
                if x <= 0:
                    raise ValueError("x debe ser positivo")
                r = math.log2(x)
                self._mostrar(f"log₂({x}) = {r}")
            elif op == "Logaritmo base n":
                base = float(self.entradas_log["base"].get())
                if x <= 0 or base <= 0 or base == 1:
                    raise ValueError("x y base deben ser positivos, base ≠ 1")
                r = math.log(x, base)
                self._mostrar(f"log_{base}({x}) = {r}")
            elif op == "Exponencial (e^x)":
                r = math.exp(x)
                self._mostrar(f"e^{x} = {r}")
            elif op == "Potencia de 10 (10^x)":
                r = 10 ** x
                self._mostrar(f"10^{x} = {r}")
            elif op == "Potencia de 2 (2^x)":
                r = 2 ** x
                self._mostrar(f"2^{x} = {r}")
            elif op == "Logaritmo 1+x (log1p)":
                if x <= -1:
                    raise ValueError("x debe ser > -1")
                r = math.log1p(x)
                self._mostrar(f"ln(1+{x}) = {r}")
            elif op == "Exponencial -1 (expm1)":
                r = math.expm1(x)
                self._mostrar(f"e^{x} - 1 = {r}")
                
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # ==================== PESTAÑA: ESTADÍSTICAS ====================
    def _crear_pestana_estadisticas(self):
        frame = self._crear_pestana("📊 Estadísticas")
        
        ops = ["Media aritmética", "Mediana", "Moda", "Desviación estándar (población)",
               "Desviación estándar (muestra)", "Varianza (población)", "Varianza (muestra)",
               "Rango", "Suma total", "Mínimo y Máximo", "Media geométrica", "Media armónica"]
        
        self.var_stats = tk.StringVar()
        self.combo_stats = self._crear_selector(frame, ops, self.var_stats)
        
        tk.Label(frame, text="Ingrese datos separados por comas:", 
                font=("Segoe UI", 9), fg="#8b949e", bg="#0d1117").pack(anchor=tk.W, pady=(5, 0))
        
        self.entrada_stats = tk.Text(frame, height=3, font=("Consolas", 10),
                                    bg="#21262d", fg="#c9d1d9", insertbackground="#c9d1d9",
                                    relief=tk.FLAT, padx=10, pady=8)
        self.entrada_stats.pack(fill=tk.X, pady=(5, 0))
        self.entrada_stats.insert("1.0", "1, 2, 3, 4, 5")
        
        self._crear_boton_calcular(frame, self._calcular_stats)

    def _calcular_stats(self):
        try:
            texto = self.entrada_stats.get("1.0", tk.END).strip()
            datos = [float(x.strip()) for x in texto.split(",") if x.strip()]
            
            if len(datos) == 0:
                raise ValueError("Ingrese al menos un dato")
            
            op = self.var_stats.get()
            
            if op == "Media aritmética":
                r = statistics.mean(datos)
                self._mostrar(f"Media de {datos}\n= {r}")
            elif op == "Mediana":
                r = statistics.median(datos)
                self._mostrar(f"Mediana de {datos}\n= {r}")
            elif op == "Moda":
                try:
                    r = statistics.mode(datos)
                    self._mostrar(f"Moda de {datos}\n= {r}")
                except statistics.StatisticsError:
                    self._mostrar("No hay moda única")
            elif op == "Desviación estándar (población)":
                if len(datos) < 1:
                    raise ValueError("Se necesitan al menos 1 dato")
                r = statistics.pstdev(datos)
                self._mostrar(f"σ (población) = {r}")
            elif op == "Desviación estándar (muestra)":
                if len(datos) < 2:
                    raise ValueError("Se necesitan al menos 2 datos")
                r = statistics.stdev(datos)
                self._mostrar(f"s (muestra) = {r}")
            elif op == "Varianza (población)":
                r = statistics.pvariance(datos)
                self._mostrar(f"σ² (población) = {r}")
            elif op == "Varianza (muestra)":
                if len(datos) < 2:
                    raise ValueError("Se necesitan al menos 2 datos")
                r = statistics.variance(datos)
                self._mostrar(f"s² (muestra) = {r}")
            elif op == "Rango":
                r = max(datos) - min(datos)
                self._mostrar(f"Rango = {max(datos)} - {min(datos)} = {r}")
            elif op == "Suma total":
                r = sum(datos)
                self._mostrar(f"Σ = {r}\nCantidad: {len(datos)}")
            elif op == "Mínimo y Máximo":
                self._mostrar(f"Mínimo: {min(datos)}\nMáximo: {max(datos)}")
            elif op == "Media geométrica":
                if any(x <= 0 for x in datos):
                    raise ValueError("Todos los valores deben ser positivos")
                r = statistics.geometric_mean(datos)
                self._mostrar(f"Media geométrica = {r}")
            elif op == "Media armónica":
                if any(x <= 0 for x in datos):
                    raise ValueError("Todos los valores deben ser positivos")
                r = statistics.harmonic_mean(datos)
                self._mostrar(f"Media armónica = {r}")
                
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # ==================== PESTAÑA: COMBINATORIA ====================
    def _crear_pestana_combinatoria(self):
        frame = self._crear_pestana("🎲 Combinatoria")
        
        ops = ["Factorial (n!)", "Permutaciones (nPr)", "Combinaciones (nCr)",
               "MCD (máximo común divisor)", "MCM (mínimo común múltiplo)",
               "Números primos hasta n", "¿Es primo?", "Factorización prima",
               "Fibonacci (n-ésimo término)", "Secuencia Fibonacci"]
        
        self.var_comb = tk.StringVar()
        self.combo_comb = self._crear_selector(frame, ops, self.var_comb)
        self.combo_comb.bind("<<ComboboxSelected>>", self._actualizar_comb)
        
        self.frame_comb = ttk.Frame(frame)
        self.frame_comb.pack(fill=tk.X)
        
        self.entradas_comb = {}
        self._actualizar_comb()
        
        self._crear_boton_calcular(frame, self._calcular_comb)

    def _actualizar_comb(self, event=None):
        for w in self.frame_comb.winfo_children():
            w.destroy()
        self.entradas_comb.clear()
        
        op = self.var_comb.get()
        if op in ["Factorial (n!)", "Números primos hasta n", "¿Es primo?", 
                  "Factorización prima", "Fibonacci (n-ésimo término)", "Secuencia Fibonacci"]:
            self.entradas_comb["n"] = self._crear_entrada(self.frame_comb, "Valor n:")
        elif op in ["Permutaciones (nPr)", "Combinaciones (nCr)"]:
            self.entradas_comb["n"] = self._crear_entrada(self.frame_comb, "Total n:")
            self.entradas_comb["r"] = self._crear_entrada(self.frame_comb, "Elegir r:")
        elif op in ["MCD (máximo común divisor)", "MCM (mínimo común múltiplo)"]:
            self.entradas_comb["a"] = self._crear_entrada(self.frame_comb, "Valor a:")
            self.entradas_comb["b"] = self._crear_entrada(self.frame_comb, "Valor b:")

    def _es_primo(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def _factorizar(self, n):
        factores = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factores.append(d)
                n //= d
            d += 1
        if n > 1:
            factores.append(n)
        return factores

    def _fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def _calcular_comb(self):
        try:
            op = self.var_comb.get()
            
            if op == "Factorial (n!)":
                n = int(self.entradas_comb["n"].get())
                if n < 0:
                    raise ValueError("n debe ser >= 0")
                r = math.factorial(n)
                self._mostrar(f"{n}! = {r}")
            elif op == "Permutaciones (nPr)":
                n = int(self.entradas_comb["n"].get())
                r_val = int(self.entradas_comb["r"].get())
                if n < 0 or r_val < 0 or r_val > n:
                    raise ValueError("Valores inválidos")
                r = math.perm(n, r_val)
                self._mostrar(f"P({n},{r_val}) = {r}")
            elif op == "Combinaciones (nCr)":
                n = int(self.entradas_comb["n"].get())
                r_val = int(self.entradas_comb["r"].get())
                if n < 0 or r_val < 0 or r_val > n:
                    raise ValueError("Valores inválidos")
                r = math.comb(n, r_val)
                self._mostrar(f"C({n},{r_val}) = {r}")
            elif op == "MCD (máximo común divisor)":
                a = int(self.entradas_comb["a"].get())
                b = int(self.entradas_comb["b"].get())
                r = math.gcd(a, b)
                self._mostrar(f"MCD({a}, {b}) = {r}")
            elif op == "MCM (mínimo común múltiplo)":
                a = int(self.entradas_comb["a"].get())
                b = int(self.entradas_comb["b"].get())
                r = abs(a * b) // math.gcd(a, b) if a and b else 0
                self._mostrar(f"MCM({a}, {b}) = {r}")
            elif op == "Números primos hasta n":
                n = int(self.entradas_comb["n"].get())
                if n < 2:
                    self._mostrar("No hay primos menores que 2")
                else:
                    primos = [i for i in range(2, n + 1) if self._es_primo(i)]
                    self._mostrar(f"Primos hasta {n}:\n{primos}\nTotal: {len(primos)}")
            elif op == "¿Es primo?":
                n = int(self.entradas_comb["n"].get())
                if self._es_primo(n):
                    self._mostrar(f"✓ {n} ES primo")
                else:
                    self._mostrar(f"✗ {n} NO es primo")
            elif op == "Factorización prima":
                n = int(self.entradas_comb["n"].get())
                if n < 2:
                    raise ValueError("n debe ser >= 2")
                factores = self._factorizar(n)
                self._mostrar(f"{n} = {' × '.join(map(str, factores))}")
            elif op == "Fibonacci (n-ésimo término)":
                n = int(self.entradas_comb["n"].get())
                if n < 0:
                    raise ValueError("n debe ser >= 0")
                r = self._fibonacci(n)
                self._mostrar(f"F({n}) = {r}")
            elif op == "Secuencia Fibonacci":
                n = int(self.entradas_comb["n"].get())
                if n < 1:
                    raise ValueError("n debe ser >= 1")
                seq = [self._fibonacci(i) for i in range(n)]
                self._mostrar(f"Fibonacci (primeros {n}):\n{seq}")
                
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # ==================== PESTAÑA: CONVERSIONES ====================
    def _crear_pestana_conversiones(self):
        frame = self._crear_pestana("🔄 Conversiones")
        
        ops = ["Grados → Radianes", "Radianes → Grados",
               "Decimal → Binario", "Binario → Decimal",
               "Decimal → Hexadecimal", "Hexadecimal → Decimal",
               "Decimal → Octal", "Octal → Decimal",
               "Celsius → Fahrenheit", "Fahrenheit → Celsius",
               "Celsius → Kelvin", "Kelvin → Celsius",
               "Kilómetros → Millas", "Millas → Kilómetros",
               "Metros → Pies", "Pies → Metros",
               "Kilogramos → Libras", "Libras → Kilogramos"]
        
        self.var_conv = tk.StringVar()
        self.combo_conv = self._crear_selector(frame, ops, self.var_conv)
        
        self.frame_conv = ttk.Frame(frame)
        self.frame_conv.pack(fill=tk.X)
        
        self.entrada_conv = self._crear_entrada(self.frame_conv, "Valor a convertir:")
        
        self._crear_boton_calcular(frame, self._calcular_conv)

    def _calcular_conv(self):
        try:
            op = self.var_conv.get()
            valor = self.entrada_conv.get().strip()
            
            if op == "Grados → Radianes":
                v = float(valor)
                r = math.radians(v)
                self._mostrar(f"{v}° = {r} rad")
            elif op == "Radianes → Grados":
                v = float(valor)
                r = math.degrees(v)
                self._mostrar(f"{v} rad = {r}°")
            elif op == "Decimal → Binario":
                v = int(valor)
                self._mostrar(f"{v} (dec) = {bin(v)} (bin)")
            elif op == "Binario → Decimal":
                v = int(valor, 2)
                self._mostrar(f"{valor} (bin) = {v} (dec)")
            elif op == "Decimal → Hexadecimal":
                v = int(valor)
                self._mostrar(f"{v} (dec) = {hex(v)} (hex)")
            elif op == "Hexadecimal → Decimal":
                v = int(valor, 16)
                self._mostrar(f"{valor} (hex) = {v} (dec)")
            elif op == "Decimal → Octal":
                v = int(valor)
                self._mostrar(f"{v} (dec) = {oct(v)} (oct)")
            elif op == "Octal → Decimal":
                v = int(valor, 8)
                self._mostrar(f"{valor} (oct) = {v} (dec)")
            elif op == "Celsius → Fahrenheit":
                v = float(valor)
                r = (v * 9/5) + 32
                self._mostrar(f"{v}°C = {r}°F")
            elif op == "Fahrenheit → Celsius":
                v = float(valor)
                r = (v - 32) * 5/9
                self._mostrar(f"{v}°F = {r}°C")
            elif op == "Celsius → Kelvin":
                v = float(valor)
                r = v + 273.15
                self._mostrar(f"{v}°C = {r} K")
            elif op == "Kelvin → Celsius":
                v = float(valor)
                r = v - 273.15
                self._mostrar(f"{v} K = {r}°C")
            elif op == "Kilómetros → Millas":
                v = float(valor)
                r = v * 0.621371
                self._mostrar(f"{v} km = {r} mi")
            elif op == "Millas → Kilómetros":
                v = float(valor)
                r = v * 1.60934
                self._mostrar(f"{v} mi = {r} km")
            elif op == "Metros → Pies":
                v = float(valor)
                r = v * 3.28084
                self._mostrar(f"{v} m = {r} ft")
            elif op == "Pies → Metros":
                v = float(valor)
                r = v * 0.3048
                self._mostrar(f"{v} ft = {r} m")
            elif op == "Kilogramos → Libras":
                v = float(valor)
                r = v * 2.20462
                self._mostrar(f"{v} kg = {r} lb")
            elif op == "Libras → Kilogramos":
                v = float(valor)
                r = v * 0.453592
                self._mostrar(f"{v} lb = {r} kg")
                
        except ValueError as e:
            messagebox.showerror("Error", f"Valor inválido: {e}")

    # ==================== PESTAÑA: AVANZADAS ====================
    def _crear_pestana_avanzadas(self):
        frame = self._crear_pestana("🚀 Avanzadas")
        
        ops = ["Ecuación cuadrática (ax² + bx + c = 0)", 
               "Distancia entre puntos 2D",
               "Punto medio 2D", "Pendiente de recta",
               "Área del círculo", "Perímetro del círculo",
               "Área del triángulo (base × altura)",
               "Área del triángulo (Herón)",
               "Volumen esfera", "Volumen cilindro", "Volumen cono",
               "Interés simple", "Interés compuesto",
               "Constantes matemáticas"]
        
        self.var_avanz = tk.StringVar()
        self.combo_avanz = self._crear_selector(frame, ops, self.var_avanz)
        self.combo_avanz.bind("<<ComboboxSelected>>", self._actualizar_avanz)
        
        self.frame_avanz = ttk.Frame(frame)
        self.frame_avanz.pack(fill=tk.X)
        
        self.entradas_avanz = {}
        self._actualizar_avanz()
        
        self._crear_boton_calcular(frame, self._calcular_avanz)

    def _actualizar_avanz(self, event=None):
        for w in self.frame_avanz.winfo_children():
            w.destroy()
        self.entradas_avanz.clear()
        
        op = self.var_avanz.get()
        
        if op == "Ecuación cuadrática (ax² + bx + c = 0)":
            self.entradas_avanz["a"] = self._crear_entrada(self.frame_avanz, "Coeficiente a:")
            self.entradas_avanz["b"] = self._crear_entrada(self.frame_avanz, "Coeficiente b:")
            self.entradas_avanz["c"] = self._crear_entrada(self.frame_avanz, "Coeficiente c:")
        elif op in ["Distancia entre puntos 2D", "Punto medio 2D", "Pendiente de recta"]:
            self.entradas_avanz["x1"] = self._crear_entrada(self.frame_avanz, "x₁:")
            self.entradas_avanz["y1"] = self._crear_entrada(self.frame_avanz, "y₁:")
            self.entradas_avanz["x2"] = self._crear_entrada(self.frame_avanz, "x₂:")
            self.entradas_avanz["y2"] = self._crear_entrada(self.frame_avanz, "y₂:")
        elif op in ["Área del círculo", "Perímetro del círculo", "Volumen esfera"]:
            self.entradas_avanz["r"] = self._crear_entrada(self.frame_avanz, "Radio:")
        elif op == "Área del triángulo (base × altura)":
            self.entradas_avanz["base"] = self._crear_entrada(self.frame_avanz, "Base:")
            self.entradas_avanz["altura"] = self._crear_entrada(self.frame_avanz, "Altura:")
        elif op == "Área del triángulo (Herón)":
            self.entradas_avanz["a"] = self._crear_entrada(self.frame_avanz, "Lado a:")
            self.entradas_avanz["b"] = self._crear_entrada(self.frame_avanz, "Lado b:")
            self.entradas_avanz["c"] = self._crear_entrada(self.frame_avanz, "Lado c:")
        elif op == "Volumen cilindro":
            self.entradas_avanz["r"] = self._crear_entrada(self.frame_avanz, "Radio:")
            self.entradas_avanz["h"] = self._crear_entrada(self.frame_avanz, "Altura:")
        elif op == "Volumen cono":
            self.entradas_avanz["r"] = self._crear_entrada(self.frame_avanz, "Radio:")
            self.entradas_avanz["h"] = self._crear_entrada(self.frame_avanz, "Altura:")
        elif op == "Interés simple":
            self.entradas_avanz["capital"] = self._crear_entrada(self.frame_avanz, "Capital inicial:")
            self.entradas_avanz["tasa"] = self._crear_entrada(self.frame_avanz, "Tasa (% anual):")
            self.entradas_avanz["tiempo"] = self._crear_entrada(self.frame_avanz, "Tiempo (años):")
        elif op == "Interés compuesto":
            self.entradas_avanz["capital"] = self._crear_entrada(self.frame_avanz, "Capital inicial:")
            self.entradas_avanz["tasa"] = self._crear_entrada(self.frame_avanz, "Tasa (% anual):")
            self.entradas_avanz["tiempo"] = self._crear_entrada(self.frame_avanz, "Tiempo (años):")
            self.entradas_avanz["n"] = self._crear_entrada(self.frame_avanz, "Capitalizaciones/año:", "12")

    def _calcular_avanz(self):
        try:
            op = self.var_avanz.get()
            
            if op == "Ecuación cuadrática (ax² + bx + c = 0)":
                a = float(self.entradas_avanz["a"].get())
                b = float(self.entradas_avanz["b"].get())
                c = float(self.entradas_avanz["c"].get())
                if a == 0:
                    raise ValueError("a no puede ser 0")
                disc = b*b - 4*a*c
                if disc > 0:
                    x1 = (-b + math.sqrt(disc)) / (2*a)
                    x2 = (-b - math.sqrt(disc)) / (2*a)
                    self._mostrar(f"Discriminante: {disc}\nDos raíces reales:\nx₁ = {x1}\nx₂ = {x2}")
                elif disc == 0:
                    x = -b / (2*a)
                    self._mostrar(f"Discriminante: {disc}\nRaíz doble:\nx = {x}")
                else:
                    re = -b / (2*a)
                    im = math.sqrt(-disc) / (2*a)
                    self._mostrar(f"Discriminante: {disc}\nRaíces complejas:\nx₁ = {re} + {im}i\nx₂ = {re} - {im}i")
                    
            elif op == "Distancia entre puntos 2D":
                x1, y1 = float(self.entradas_avanz["x1"].get()), float(self.entradas_avanz["y1"].get())
                x2, y2 = float(self.entradas_avanz["x2"].get()), float(self.entradas_avanz["y2"].get())
                d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                self._mostrar(f"Distancia entre ({x1},{y1}) y ({x2},{y2})\n= {d}")
                
            elif op == "Punto medio 2D":
                x1, y1 = float(self.entradas_avanz["x1"].get()), float(self.entradas_avanz["y1"].get())
                x2, y2 = float(self.entradas_avanz["x2"].get()), float(self.entradas_avanz["y2"].get())
                mx, my = (x1+x2)/2, (y1+y2)/2
                self._mostrar(f"Punto medio de ({x1},{y1}) y ({x2},{y2})\n= ({mx}, {my})")
                
            elif op == "Pendiente de recta":
                x1, y1 = float(self.entradas_avanz["x1"].get()), float(self.entradas_avanz["y1"].get())
                x2, y2 = float(self.entradas_avanz["x2"].get()), float(self.entradas_avanz["y2"].get())
                if x2 - x1 == 0:
                    self._mostrar("Pendiente indefinida (recta vertical)")
                else:
                    m = (y2-y1)/(x2-x1)
                    self._mostrar(f"Pendiente m = {m}")
                    
            elif op == "Área del círculo":
                r = float(self.entradas_avanz["r"].get())
                area = math.pi * r**2
                self._mostrar(f"Área = πr² = {area}")
                
            elif op == "Perímetro del círculo":
                r = float(self.entradas_avanz["r"].get())
                per = 2 * math.pi * r
                self._mostrar(f"Perímetro = 2πr = {per}")
                
            elif op == "Área del triángulo (base × altura)":
                base = float(self.entradas_avanz["base"].get())
                altura = float(self.entradas_avanz["altura"].get())
                area = (base * altura) / 2
                self._mostrar(f"Área = (b×h)/2 = {area}")
                
            elif op == "Área del triángulo (Herón)":
                a = float(self.entradas_avanz["a"].get())
                b = float(self.entradas_avanz["b"].get())
                c = float(self.entradas_avanz["c"].get())
                s = (a + b + c) / 2
                if s <= a or s <= b or s <= c:
                    raise ValueError("No forman un triángulo válido")
                area = math.sqrt(s * (s-a) * (s-b) * (s-c))
                self._mostrar(f"Semiperímetro s = {s}\nÁrea = √[s(s-a)(s-b)(s-c)] = {area}")
                
            elif op == "Volumen esfera":
                r = float(self.entradas_avanz["r"].get())
                vol = (4/3) * math.pi * r**3
                self._mostrar(f"Volumen = (4/3)πr³ = {vol}")
                
            elif op == "Volumen cilindro":
                r = float(self.entradas_avanz["r"].get())
                h = float(self.entradas_avanz["h"].get())
                vol = math.pi * r**2 * h
                self._mostrar(f"Volumen = πr²h = {vol}")
                
            elif op == "Volumen cono":
                r = float(self.entradas_avanz["r"].get())
                h = float(self.entradas_avanz["h"].get())
                vol = (1/3) * math.pi * r**2 * h
                self._mostrar(f"Volumen = (1/3)πr²h = {vol}")
                
            elif op == "Interés simple":
                capital = float(self.entradas_avanz["capital"].get())
                tasa = float(self.entradas_avanz["tasa"].get()) / 100
                tiempo = float(self.entradas_avanz["tiempo"].get())
                interes = capital * tasa * tiempo
                total = capital + interes
                self._mostrar(f"Interés = {interes}\nMonto final = {total}")
                
            elif op == "Interés compuesto":
                capital = float(self.entradas_avanz["capital"].get())
                tasa = float(self.entradas_avanz["tasa"].get()) / 100
                tiempo = float(self.entradas_avanz["tiempo"].get())
                n = float(self.entradas_avanz["n"].get())
                total = capital * (1 + tasa/n)**(n*tiempo)
                interes = total - capital
                self._mostrar(f"Monto final = {total}\nInterés ganado = {interes}")
                
            elif op == "Constantes matemáticas":
                self._mostrar(f"π (pi) = {math.pi}\ne (Euler) = {math.e}\nτ (tau) = {math.tau}\n"
                             f"φ (phi) ≈ {(1 + math.sqrt(5))/2}\n√2 = {math.sqrt(2)}\n√3 = {math.sqrt(3)}")
                
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # ==================== FUNCIONES DE MEMORIA ====================
    def _mostrar(self, texto):
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, texto)
        # Extraer último número del resultado para ANS
        try:
            nums = [float(s) for s in texto.replace(",", ".").split() if self._es_numero(s)]
            if nums:
                self.ultima_respuesta = nums[-1]
                self.lbl_ans.config(text=f"ANS: {self.ultima_respuesta}")
        except:
            pass
        # Agregar al historial
        self.historial.append(texto)
        if len(self.historial) > 50:
            self.historial.pop(0)

    def _es_numero(self, s):
        try:
            float(s)
            return True
        except:
            return False

    def _mem_clear(self):
        self.memoria = 0
        self.lbl_memoria.config(text="M: 0")

    def _mem_recall(self):
        self._mostrar(f"Memoria: {self.memoria}")

    def _mem_add(self):
        self.memoria += self.ultima_respuesta
        self.lbl_memoria.config(text=f"M: {self.memoria}")

    def _mem_sub(self):
        self.memoria -= self.ultima_respuesta
        self.lbl_memoria.config(text=f"M: {self.memoria}")

    def _ver_historial(self):
        if not self.historial:
            messagebox.showinfo("Historial", "No hay operaciones en el historial.")
            return
        
        ventana_hist = tk.Toplevel(self.ventana)
        ventana_hist.title("📜 Historial de Operaciones")
        ventana_hist.configure(bg="#0d1117")
        ventana_hist.geometry("400x400")
        
        texto = tk.Text(ventana_hist, font=("Consolas", 10), bg="#161b22", fg="#c9d1d9",
                       relief=tk.FLAT, padx=10, pady=10)
        texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for i, op in enumerate(reversed(self.historial[-20:]), 1):
            texto.insert(tk.END, f"[{i}] {op}\n{'─'*40}\n")
        texto.config(state=tk.DISABLED)

    def ejecutar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    app = CalculadoraCientificaAvanzada()
    app.ejecutar()
