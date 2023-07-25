# P4E - Chapter 10, Exercise 1
# Programa que contabiliza mensagem de emails recebidas em cada conta de email
# e ordena de forma decrescente

emails = open('mbox-short.txt')

lista = []
contador = {}
max = 0

print("\nQuantidade de emails recebidos e ordenados de forma reversa:\n")

for linha in emails:
    linha = linha.rstrip()
    if linha.startswith('From:'):
        linha = linha.split()
        lista.append(linha[1])

for email in lista:
    contador[email] = contador.get(email, 0) + 1

l = list()

for k, v in contador.items():
    l.append((v, k))

l.sort(reverse=True)

for v, k in l:
    print(k, v)

print()