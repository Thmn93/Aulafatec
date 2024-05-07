from math import pi,pow
def esfera(raio):
    return (4/3*pi*pow(raio, 3))

r = float(input("Digite o raio: "))

print(f"O Volume da esfera de raio {r} é {esfera(r)}!")