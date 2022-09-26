from math import sqrt
a=float(input())
b=float(input())
c=float(input())

discriminante =  b * b - 4 * a * c

if discriminante < 0:
    print(f"La ecuación no tiene soluciones reales.")
else:
    raiz = sqrt(discriminante)
    x1 = (-b + raiz) / (2 * a)
    if discriminante != 0:
        x2 = (-b - raiz) / (2 * a)
        print(f"Las soluciones son {x1} y {x2}.")
    else:
        print(f"La única solución es x = {x1}")