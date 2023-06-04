#3. Exercício de Listas e Laços de Repetição
lista = [] #  lista vazia

# Solicita ao utilizador que insira cinco números inteiros
lista.append(input("Introduza o primeiro número inteiro:\n"))
lista.append(input("Introduza o segundo número inteiro:\n"))
lista.append(input("Introduza o terceiro número inteiro:\n"))
lista.append(input("Introduza o quarto número inteiro:\n"))
lista.append(input("Introduza o último número inteiro:\n"))
erro = False
for i in range(len(lista)):
    try:
        lista[i]=int(lista[i])
        erro = False
    except ValueError: # Resultado caso o utilizador tenha introduzido um valor não inteiro
        erro = True
    if erro:
        print ("O " +  str(i+1) + "º valor introduzido não é um número inteiro.\n") 
    elif (int(lista[i])%2==0): # Para cada número da lista, verificação se é par
        print(str(lista[i]) + " é par") # Se for par, é exibido na consola
