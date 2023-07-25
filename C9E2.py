# P4E - Chapter 9, Exercise 2
# Programa que categoriza mensagem de emails de acordo com o dia em que foi enviada.

arquivo = open('mbox-short.txt')
lista = list()
contador = {}

for linha in arquivo:
    linha = linha.rstrip()
    if linha.startswith('From '):
        linha = linha.split()
        lista.append(linha[2])
                    
for i in lista:
    contador[i] = contador.get(i, 0) + 1

print("\nTotal de mensagens envidas: ", len(lista))
print("Quantidade de mensagens enviadas por dia da semana:")

for item in contador:
    print(f"{item}: {contador[item]}")

print()

