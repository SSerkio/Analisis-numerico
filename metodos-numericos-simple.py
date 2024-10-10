1 import tkinter as tk
from tkinter import ttk, messagebox
import math

class AplicacionMetodosNumericos:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Raíces - Métodos Numéricos")
        self.root.geometry("600x500")
        
        # Variables
        self.funcion_var = tk.StringVar()
        self.a_var = tk.StringVar(value="0")
        self.b_var = tk.StringVar(value="10")
        self.tolerancia_var = tk.StringVar(value="0.0001")
        self.max_iter_var = tk.StringVar(value="100")
        self.x0_var = tk.StringVar(value="0")
        self.derivada_var = tk.StringVar()
        
        # Ejemplos predefinidos
        self.ejemplos = {
            "Seleccione un ejemplo": {"funcion": "", "derivada": ""},
            "Función cuadrática": {"funcion": "x**2 - 4", "derivada": "2*x"},
            "Función trigonométrica": {"funcion": "math.sin(x)", "derivada": "math.cos(x)"},
            "Función exponencial": {"funcion": "math.exp(x) - 3", "derivada": "math.exp(x)"}
        }
        
        self.crear_widgets()

    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        ttk.Label(main_frame, text="Calculadora de Raíces", font=('Arial', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Frame de ejemplos
        ejemplo_frame = ttk.LabelFrame(main_frame, text="Ejemplos Predefinidos", padding="5")
        ejemplo_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.ejemplo_combo = ttk.Combobox(ejemplo_frame, values=list(self.ejemplos.keys()), width=30)
        self.ejemplo_combo.set("Seleccione un ejemplo")
        self.ejemplo_combo.grid(row=0, column=0, padx=5)
        ttk.Button(ejemplo_frame, text="Cargar Ejemplo", command=self.cargar_ejemplo).grid(row=0, column=1, padx=5)
        
        # Frame de entrada
        input_frame = ttk.LabelFrame(main_frame, text="Entrada de Datos", padding="5")
        input_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(input_frame, text="Función f(x):").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(input_frame, textvariable=self.funcion_var, width=40).grid(row=0, column=1, sticky=(tk.W, tk.E))
        
        ttk.Label(input_frame, text="Intervalo [a, b]:").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(input_frame, textvariable=self.a_var, width=10).grid(row=1, column=1, sticky=tk.W)
        ttk.Entry(input_frame, textvariable=self.b_var, width=10).grid(row=1, column=1, sticky=tk.E)
        
        ttk.Label(input_frame, text="Tolerancia:").grid(row=2, column=0, sticky=tk.W)
        ttk.Entry(input_frame, textvariable=self.tolerancia_var, width=15).grid(row=2, column=1, sticky=tk.W)
        
        ttk.Label(input_frame, text="Punto inicial x0:").grid(row=3, column=0, sticky=tk.W)
        ttk.Entry(input_frame, textvariable=self.x0_var, width=15).grid(row=3, column=1, sticky=tk.W)
        
        ttk.Label(input_frame, text="f'(x) (para Newton):").grid(row=4, column=0, sticky=tk.W)
        ttk.Entry(input_frame, textvariable=self.derivada_var, width=40).grid(row=4, column=1, sticky=(tk.W, tk.E))
        
        # Botones de métodos
        button_frame = ttk.LabelFrame(main_frame, text="Métodos de Cálculo", padding="5")
        button_frame.grid(row=3, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        ttk.Button(button_frame, text="Bisección", command=self.biseccion).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(button_frame, text="Punto Fijo", command=self.punto_fijo).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(button_frame, text="Newton-Raphson", command=self.newton_raphson).grid(row=0, column=2, padx=5, pady=5)
        
        # Área de resultados
        result_frame = ttk.LabelFrame(main_frame, text="Resultados", padding="5")
        result_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        self.resultado_text = tk.Text(result_frame, height=10, width=50)
        self.resultado_text.grid(row=0, column=0, pady=5)
        
        # Botones inferiores
        ttk.Button(main_frame, text="Limpiar", command=self.limpiar_todo).grid(row=5, column=0, pady=5)
        ttk.Button(main_frame, text="Salir", command=self.root.quit).grid(row=5, column=1, pady=5)

    def cargar_ejemplo(self):
        ejemplo = self.ejemplos[self.ejemplo_combo.get()]
        self.funcion_var.set(ejemplo["funcion"])
        self.derivada_var.set(ejemplo["derivada"])

    def limpiar_todo(self):
        self.funcion_var.set("")
        self.derivada_var.set("")
        self.resultado_text.delete(1.0, tk.END)

    def biseccion(self):
        try:
            funcion = self.funcion_var.get()
            a = float(self.a_var.get())
            b = float(self.b_var.get())
            tolerancia = float(self.tolerancia_var.get())
            max_iter = int(self.max_iter_var.get())
            
            def f(x):
                return eval(funcion, {"x": x, "math": math})
            
            if f(a) * f(b) >= 0:
                messagebox.showerror("Error", "El método de bisección no puede ser aplicado en este intervalo.")
                return
            
            iteracion = 0
            while (b - a) / 2 > tolerancia and iteracion < max_iter:
                c = (a + b) / 2
                if f(c) == 0:
                    break
                if f(c) * f(a) < 0:
                    b = c
                else:
                    a = c
                iteracion += 1
            
            raiz = (a + b) / 2
            resultado = f"Método de Bisección:\n"
            resultado += f"Raíz encontrada: {raiz:.6f}\n"
            resultado += f"f({raiz:.6f}) = {f(raiz):.6f}\n"
            resultado += f"Iteraciones: {iteracion}"
            self.resultado_text.delete(1.0, tk.END)
            self.resultado_text.insert(tk.END, resultado)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def punto_fijo(self):
        try:
            funcion_g = self.funcion_var.get()
            x0 = float(self.x0_var.get())
            tolerancia = float(self.tolerancia_var.get())
            max_iter = int(self.max_iter_var.get())
            
            def g(x):
                return eval(funcion_g, {"x": x, "math": math})
            
            x_ant = x0
            iteracion = 0
            resultado = "Método de Punto Fijo:\n"
            
            while iteracion < max_iter:
                x_nuevo = g(x_ant)
                if abs(x_nuevo - x_ant) < tolerancia:
                    resultado += f"Raíz encontrada: {x_nuevo:.6f}\n"
                    resultado += f"g({x_nuevo:.6f}) = {g(x_nuevo):.6f}\n"
                    resultado += f"Iteraciones: {iteracion}"
                    self.resultado_text.delete(1.0, tk.END)
                    self.resultado_text.insert(tk.END, resultado)
                    return
                x_ant = x_nuevo
                iteracion += 1
            
            messagebox.showwarning("Advertencia", "El método no convergió")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def newton_raphson(self):
        try:
            funcion = self.funcion_var.get()
            derivada = self.derivada_var.get()
            x0 = float(self.x0_var.get())
            tolerancia = float(self.tolerancia_var.get())
            max_iter = int(self.max_iter_var.get())
            
            def f(x):
                return eval(funcion, {"x": x, "math": math})
            def f_prima(x):
                return eval(derivada, {"x": x, "math": math})
            
            x_ant = x0
            iteracion = 0
            resultado = "Método de Newton-Raphson:\n"
            
            while iteracion < max_iter:
                if f_prima(x_ant) == 0:
                    messagebox.showerror("Error", "División por cero.")
                    return
                
                x_nuevo = x_ant - f(x_ant) / f_prima(x_ant)
                if abs(x_nuevo - x_ant) < tolerancia:
                    resultado += f"Raíz encontrada: {x_nuevo:.6f}\n"
                    resultado += f"f({x_nuevo:.6f}) = {f(x_nuevo):.6f}\n"
                    resultado += f"Iteraciones: {iteracion}"
                    self.resultado_text.delete(1.0, tk.END)
                    self.resultado_text.insert(tk.END, resultado)
                    return
                x_ant = x_nuevo
                iteracion += 1
            
            messagebox.showwarning("Advertencia", "El método no convergió")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionMetodosNumericos(root)
    root.mainloop()
