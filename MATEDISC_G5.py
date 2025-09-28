import numpy as np
import matplotlib.pyplot as plt
import math
import sys

class Color:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def rotacion(puntos, angulo):
    rad = math.radians(angulo)
    R = np.array([[math.cos(rad), -math.sin(rad)],
                  [math.sin(rad),  math.cos(rad)]])
    return puntos @ R.T

def reflexion(puntos, eje):
    if eje == 'x':
        R = np.array([[1,  0],
                      [0, -1]])
    elif eje == 'y':
        R = np.array([[-1, 0],
                      [0,  1]])
    elif eje == 'd':  # diagonal y = x
        R = np.array([[0, 1],
                      [1, 0]])
    else:
        raise ValueError("Eje de reflexión inválido. Use 'x', 'y' o 'd'.")
    return puntos @ R.T

def escalamiento(puntos, kx, ky):
    if kx == 0 or ky == 0:
        raise ValueError("Los factores de escala no pueden ser cero.")
    S = np.array([[kx, 0],
                  [0, ky]])
    return puntos @ S.T

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"{Color.RED}❌ Entrada inválida. Por favor ingresa un número.{Color.END}")

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{Color.RED}❌ Entrada inválida. Por favor ingresa un número entero.{Color.END}")

def menu_transformaciones(puntos):
    print(f"\n{Color.BOLD}{Color.CYAN}   ─────────── Transformaciones ───────────{Color.END}")
    print(f"{Color.YELLOW}   1. Rotación")
    print("   2. Reflexión")
    print("   3. Homotecia (Escalamiento)")
    print("   4. Salir")
    print(f"   ────────────────────────────────────────{Color.END}")

    while True:
        op = input_int(f"{Color.BOLD}   ➤ Opción: {Color.END}")
        if op == 1:
            angulo = input_float(f"{Color.BOLD}   ➤ Ángulo de rotación (grados): {Color.END}")
            return rotacion(puntos, angulo)
        elif op == 2:
            while True:
                eje = input(f"{Color.BOLD}   ➤ Eje (x, y, d para y=x): {Color.END}").strip().lower()
                if eje in ['x', 'y', 'd']:
                    return reflexion(puntos, eje)
                else:
                    print(f"{Color.RED}❌ Opción inválida. Usa 'x', 'y' o 'd'.{Color.END}")
        elif op == 3:
            kx = input_float(f"{Color.BOLD}   ➤ Factor en X: {Color.END}")
            ky = input_float(f"{Color.BOLD}   ➤ Factor en Y: {Color.END}")
            try:
                return escalamiento(puntos, kx, ky)
            except ValueError as e:
                print(f"{Color.RED}❌ Error: {e}{Color.END}")
                continue
        elif op == 4:
            print(f"{Color.GREEN}👋 ¡Hasta luego!{Color.END}")
            return None
        else:
            print(f"{Color.RED}❌ Opción no válida. Elige entre 1 y 4.{Color.END}")

def graficar(original, transformada):
    plt.figure(figsize=(8, 6))
    plt.plot(original[:, 0], original[:, 1], 'o-', color='#1f77b4', linewidth=2, markersize=6, label="Original")
    plt.plot(transformada[:, 0], transformada[:, 1], 'o-', color='#ff7f0e', linewidth=2, markersize=6, label="Transformada")

    plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='gray', linewidth=0.8, linestyle='--')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(fontsize=12)
    plt.title("Transformaciones Lineales", fontsize=14, weight='bold')
    plt.xlabel("X", fontsize=12)
    plt.ylabel("Y", fontsize=12)
    plt.tight_layout()
    plt.show()

def main():
    print(f"\n{Color.BOLD}{Color.GREEN}   ╔══════════════════════════════════════╗")
    print(f"   ║     🌟 Transformaciones Lineales 🌟     ║")
    print(f"   ╚══════════════════════════════════════╝{Color.END}")

    while True:
        n = input_int(f"\n{Color.BOLD}   ➤ ¿Cuántos puntos tiene la figura? (mín. 3): {Color.END}")
        if n >= 3:
            break
        else:
            print(f"{Color.RED}❌ La figura debe tener al menos 3 puntos.{Color.END}")

    puntos = []
    for i in range(n):
        x = input_float(f"{Color.BOLD}   ➤ Ingrese x{i+1}: {Color.END}")
        y = input_float(f"{Color.BOLD}   ➤ Ingrese y{i+1}: {Color.END}")
        puntos.append([x, y])

    # Cerrar la figura
    puntos.append(puntos[0])
    puntos = np.array(puntos)

    while True:
        try:
            puntos_transf = menu_transformaciones(puntos)
            if puntos_transf is None:
                break

            graficar(puntos, puntos_transf)

            seguir = input(f"\n{Color.BOLD}   ➤ ¿Aplicar otra transformación? (s/n): {Color.END}").strip().lower()
            if seguir != 's':
                print(f"{Color.GREEN}✨ ¡Gracias por usar el programa! ✨{Color.END}")
                break
        except Exception as e:
            print(f"{Color.RED}❌ Error inesperado: {e}{Color.END}")
            print(f"{Color.YELLOW}💡 Por favor, inténtalo de nuevo.{Color.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Color.YELLOW}⚠️  Operación cancelada por el usuario.{Color.END}")
        sys.exit(0)
