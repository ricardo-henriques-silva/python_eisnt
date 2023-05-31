import math
def calcular_area(figura,parametro1,parametro2):
    if figura=='círculo':
        area=parametro1*parametro2*math.pi
    if figura=='rectângulo':
        area=parametro1*parametro2
    if figura=='triângulo':
        area=parametro1*parametro2/2
    return area