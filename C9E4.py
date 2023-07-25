# P4E - Chapter 9, Exercise 4
# Programa que contabiliza a conta de emails que mais recebeu mensagens.

emails = open('mbox-short.txt')

lista = []
contador = {}
max = 0
maior = {}

print("\nConta de email que mais recebeu mensagens:\n")

for linha in emails:
    linha = linha.rstrip()
    if linha.startswith('From:'):
        linha = linha.split()
        lista.append(linha[1])

for email in lista:
    contador[email] = contador.get(email, 0) + 1
    if contador[email] > max:
        max = contador[email]
        maior = {}
        maior[email] = contador[email]

for key in maior:
    print(f"{key}: {maior[key]}")

print()