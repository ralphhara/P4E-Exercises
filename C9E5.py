# P4E - Chapter 9, Exercise 5
# Programa que contabiliza domínio dos emails.

dominios = []
lista = []
contador = {}

print("\nQuantde de emails recebidos por domínio:\n")

emails = open('mbox-short.txt')

for linha in emails:
    linha = linha.rstrip()
    if linha.startswith('From: '):
        linha = linha.split()
        linha = linha[1].split('@')
        lista.append(linha[1])

for dominio in lista:
    contador[dominio] = contador.get(dominio, 0) + 1

for item in contador:
    print(f"{item}: {contador[item]}")

print()