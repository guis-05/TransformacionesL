import numpy as np
import matplotlib.pyplot as plt
import math

def rotacion(puntos, angulo):
    rad = math.radians(angulo)
    R = np.array([[math.cos(rad), -math.sin(rad)],
                [math.sin(rad), math.cos(rad)]])
    return puntos @ R.T

def reflexion(puntos, eje):
    if eje =='x':
        R = np.array([[1, 0],
                     [0, -1]])
    elif eje == 'y':
        R = np.array([[-1, 0],
                     [0, 1]])
    else:
        R = np.array([[0, 1],
                     [1, 0]])
    return puntos @ R.T

def escalamiento(puntos, kx, ky):
    S = np.array([[kx, 0],
                  [0, ky]])
    return puntos @ S.T

def menu_transformaciones(puntos):
    print("\n\t\t   ----- Transformaciones -----")
    print("\t------------------------------------------------------")
    print("\t1. Rotacion | 2. Reflexion | 3. Homotacia | 4. Salir |")
    print("\t------------------------------------------------------")
    op = int(input("\tOpcion: "))
    
    if op == 1:
        angulo = float(input("\tIngrese angulo de rotación (grados): "))
        return rotacion(puntos, angulo)
    elif op == 2:
        eje = input("\tIngrese eje (x, y, d para diagonal y=x): ")
        return reflexion(puntos, eje)
    elif op == 3:
        kx = float(input("\tFactor en X: "))
        ky = float(input("\tFactor en Y: "))
        return escalamiento(puntos, kx, ky)
    else:
        print("Saliendo...")
        return None

def graficar(original, transformada):
    plt.plot(original[:,0], original[:,1], 'bo-', label="Original")
    plt.plot(transformada[:,0], transformada[:,1], 'ro-', label="Transformada")
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.legend()
    plt.title("Transformaciones Lineales")
    plt.grid(True)
    plt.show()

def main():
    print("\n\t------------------------------------------------------")
    print("\t\t   === Transformaciones Lineales ===")
    print("\t------------------------------------------------------")

    while True:
    try:
        n = int(input("\n\t¿Cuántos puntos tiene la figura?: "))
        if n < 1:
            print("\t !! Debe haber al menos 1 punto.")
            continue
        break
    except ValueError:
        print("\t !!! Ingresa un número entero válido.")

    for i in range(n):
        x = float(input(f"\tIngrese x{i+1}: "))
        y = float(input(f"\tIngrese y{i+1}: "))
        puntos.append([x, y])

    puntos.append(puntos[0])
    puntos = np.array(puntos)

    while True:
        puntos_transf = menu_transformaciones(puntos)
        if puntos_transf is None:
            break

        graficar(puntos, puntos_transf)

        seguir = input("\n¿Quieres aplicar otra transformación? (s/n): ")
        if seguir.lower() != 's':
            break

if __name__ == "__main__":
    main()
