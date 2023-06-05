# 4. Exercício de Funções
import random 
def calcula_area_retangulo(comprimento,largura):
    area=comprimento*largura
    return area

for i in range(5): # 5 testes da função
    parametros=[random.randint(0, 20), random.randint(0, 10)] # Teste da função com valores aleatórios
    print("A área de um rectângulo com lados " + str(parametros[0]) + " e " + str(parametros[1]) + " é " + str(calcula_area_retangulo(parametros[0],parametros[1])))

print("fim\n")