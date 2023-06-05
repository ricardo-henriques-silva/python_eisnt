# 2. Exercício de Variáveis e Operações Matemáticas
from multiprocessing.sharedctypes import Value
input = input("Introduza um número inteiro:\n")
erro = False

# Conversão para inteiro
try:
    int=int(input)
except ValueError: # Resultado caso o utilizador tenha introduzido um valor não inteiro
    erro = True

if erro:
    print ("O valor introduzido não é um número inteiro.\n") # Mensagem ao utilizado em caso de valores não inteiros
elif (int%2==0):
    print ("O número " + input + " é par.")
else:
    print ("O número " + input + " é ímpar.")
print("\n")