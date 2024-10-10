import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def metodo_grafico(funcion, a, b, n):
    x = np.linspace(a, b, n)
    y = eval(funcion)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.axhline(y=0, color='r', linestyle='-')
    plt.grid(True)
    plt.title(f'Método Gráfico: {funcion}')
    plt.show()

def biseccion(funcion, a, b, tolerancia, max_iter):
    def f(x):
        return eval(funcion)
    
    if f(a) * f(b) >= 0:
        print("El método de bisección no puede ser aplicado.")
        return None
    
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
    
    return (a + b) / 2

def punto_fijo(funcion_g, x0, tolerancia, max_iter):
    def g(x):
        return eval(funcion_g)
    
    x_ant = x0
    iteracion = 0
    
    while iteracion < max_iter:
        x_nuevo = g(x_ant)
        if abs(x_nuevo - x_ant) < tolerancia:
            return x_nuevo
        x_ant = x_nuevo
        iteracion += 1
    
    return None

def newton_raphson(funcion, derivada, x0, tolerancia, max_iter):
    def f(x):
        return eval(funcion)
    def f_prima(x):
        return eval(derivada)
    
    x_ant = x0
    iteracion = 0
    
    while iteracion < max_iter:
        if f_prima(x_ant) == 0:
            print("División por cero.")
            return None
        
        x_nuevo = x_ant - f(x_ant) / f_prima(x_ant)
        if abs(x_nuevo - x_ant) < tolerancia:
            return x_nuevo
        x_ant = x_nuevo
        iteracion += 1
    
    return None

def menu():
    while True:
        print("\n=== Menú de Métodos Numéricos ===")
        print("1. Método Gráfico")
        print("2. Método de Bisección")
        print("3. Método de Punto Fijo")
        print("4. Método de Newton-Raphson")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '5':
            print("¡Hasta luego!")
            break
        
        if opcion in ['1', '2', '3', '4']:
            if opcion == '1':
                funcion = input("Ingrese la función (use 'x' como variable): ")
                a = float(input("Ingrese el límite inferior del intervalo: "))
                b = float(input("Ingrese el límite superior del intervalo: "))
                n = int(input("Ingrese el número de puntos: "))
                metodo_grafico(funcion, a, b, n)
            
            elif opcion == '2':
                funcion = input("Ingrese la función (use 'x' como variable): ")
                a = float(input("Ingrese el límite inferior del intervalo: "))
                b = float(input("Ingrese el límite superior del intervalo: "))
                tolerancia = float(input("Ingrese la tolerancia: "))
                max_iter = int(input("Ingrese el máximo de iteraciones: "))
                raiz = biseccion(funcion, a, b, tolerancia, max_iter)
                if raiz is not None:
                    print(f"La raíz encontrada es: {raiz}")
            
            elif opcion == '3':
                funcion_g = input("Ingrese la función g(x) (use 'x' como variable): ")
                x0 = float(input("Ingrese el punto inicial: "))
                tolerancia = float(input("Ingrese la tolerancia: "))
                max_iter = int(input("Ingrese el máximo de iteraciones: "))
                raiz = punto_fijo(funcion_g, x0, tolerancia, max_iter)
                if raiz is not None:
                    print(f"La raíz encontrada es: {raiz}")
                else:
                    print("El método no convergió.")
            
            elif opcion == '4':
                funcion = input("Ingrese la función (use 'x' como variable): ")
                derivada = input("Ingrese la derivada de la función: ")
                x0 = float(input("Ingrese el punto inicial: "))
                tolerancia = float(input("Ingrese la tolerancia: "))
                max_iter = int(input("Ingrese el máximo de iteraciones: "))
                raiz = newton_raphson(funcion, derivada, x0, tolerancia, max_iter)
                if raiz is not None:
                    print(f"La raíz encontrada es: {raiz}")
                else:
                    print("El método no convergió.")
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    menu()
