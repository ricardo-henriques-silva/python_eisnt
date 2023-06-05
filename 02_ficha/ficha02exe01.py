# 1. Exercício de Variáveis e Operações Matemáticas
from multiprocessing.sharedctypes import Value
inputs = [input("Introduza o primeiro número inteiro:\n"),
          input("Introduza o segundo número inteiro:\n")]
erro = False

# Conversão dos valores introduzidos para inteiro
for i in inputs:
    try:
        int(i)
    except ValueError: # Resultado caso o utilizador tenha introduzido um valor não inteiro
        erro = True
if erro:
    print ("Um dos valores introduzidos não é um número inteiro.\n") # Mensagem ao utilizado em caso de valores não inteiros
else:
    print (inputs[0] + " + " + inputs[1] + " = " + str(int(inputs[0])+int(inputs[1])))
    print (inputs[0] + " - " + inputs[1] + " = " + str(int(inputs[0])-int(inputs[1])))
    print (inputs[0] + " x " + inputs[1] + " = " + str(int(inputs[0])*int(inputs[1])))
    print (inputs[0] + " : " + inputs[1] + " = " + str(int(inputs[0])/int(inputs[1])))
    print ("fim\n")
