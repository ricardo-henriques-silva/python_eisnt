#imprimir números até 100 que são múltiplos de 5
for i in range(1,101):
    if i%5==0:
        print(str(i) + " é um múltiplo de 5") 

#outra versão, com step
for i in range(0,101,4):
    print(str(i) + " é um múltiplo de 4") 