# Função de cálculo de áreas de figuras
"""import math
def calcular_area(figura,parametro1,parametro2):
    if figura=='círculo':
        area=parametro1*parametro2*math.pi
    if figura=='rectângulo':
        area=parametro1*parametro2
    if figura=='triângulo':
        area=parametro1*parametro2/2
    return area"""
from gr04func_externa import calcular_area

figura = input("Qual o tipo de figura (triângulo|quadrado|círculo): \n").lower()
parametro1 = float(input("Qual o valor do parâmetro1?\n"))
if (figura!="círculo"):
    parametro2 = float(input("Qual o valor do parâmetro2?\n"))
else: parametro2=parametro1
area = calcular_area(figura,parametro1,parametro2)
print ("a área do rectângulo é: "+str(area))
