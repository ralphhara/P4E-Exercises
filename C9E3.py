# P4E - Chapter 9, Exercise 3
# Programa que contabiliza mensagem de emails recebidas em cada conta de email.

emails = open('mbox-short.txt')

lista = []
contador = {}
max = 0

print("\nQuantidade de emails recebidos:\n")

for linha in emails:
    linha = linha.rstrip()
    if linha.startswith('From:'):
        linha = linha.split()
        lista.append(linha[1])

for email in lista:
    contador[email] = contador.get(email, 0) + 1

for item in contador:
    print(f"{item}: {contador[item]}")

print()