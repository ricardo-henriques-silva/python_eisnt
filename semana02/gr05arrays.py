# array, list
frase = input ("Escreva aqui uma frase\n")
palavras = frase.split()                      # parte frase em palavras
frase_invertida=""
for i in range(len(palavras)):              
    palavra_invertida = palavras[i][::-1]     # inverte a palavra
    frase_invertida += palavra_invertida + " "
print(frase_invertida) 