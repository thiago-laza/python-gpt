def quadrado(l):
    area = l**2
    perimetro = 4 * l
    return f'A area de um quadrado de lado {l} e {area} m² e o perimetro e {perimetro} m'


def retangulo(l,c):
    area = l * c
    perimetro = 2 * (l + c)
    return f'A area de um retangulo com largura {l} m e comprimento {c} m e de {area} m² e o perimetro e {perimetro} m.'


def circunferencia(r):
    import math
    area = math.pi * (r**2)
    perimetro = 2 * math.pi * r
    return f'Uma circunferencia com raio de {r} m possui a area do circulo de {area:.2f} m² e o comprimento da circunferencia de {perimetro:.2f} m'


