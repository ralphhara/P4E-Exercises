# P4E - Chapter 8, Exercise 5
# Programa para verificar os endereçoes dos emails recebidos.

nomeArquivo = input("\nDigite o nome do arquivo: ")

try:
    arquivo = open(nomeArquivo)
except:
    print(f"\nO arquivo {nomeArquivo} não foi encontrado. Verifique o nome e tente novamente.\n")
    exit()

numLinhas = 0

print("\nLista de emails encontrados:\n")

for linha in arquivo:
    linha = linha.rstrip()
    if linha.startswith('From:'):
        numLinhas += 1
        email = linha.split()
        print(email[1])

print("\nNumero de linhas encontradas: ", numLinhas)
print()