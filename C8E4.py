# P4E - Chapter 8, Exercise 4
# Programa para verificar palavras únicas em um poema.

poema = open('romeo.txt')
lista = list()

numPalavras = 0

for linha in poema:
    numPalavras += len(linha.split())
    for palavra in linha.split():
        if palavra not in lista:
            lista.append(palavra)

print("\nTotal de palavras: ", numPalavras)
print("Número de palavras únicas: ", len(lista))
print("Lista de palavras únicas encontradas:\n", sorted(lista))
print()