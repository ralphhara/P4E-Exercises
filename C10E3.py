# P4E - Chapter 10, Exercise 3
# Programa que contabiliza letras do alfabeto

arquivo = open('mbox-short.txt')

print("\nContador de letras no arquivo mbox-short.txt\n")

letras = list()

for linha in arquivo:
    linha = linha.rstrip().lower()
    for letra in linha:
        if letra.isalpha():
            letras.append(letra)

cont = dict()

for letra in letras:
    cont[letra] = cont.get(letra, 0) + 1

chaves = list(cont.keys())
chaves.sort(reverse=True)

print("Letras mostradas em ordem reversa:\n")

for k in chaves:
    print(f"{k}: {cont[k]}")

print()