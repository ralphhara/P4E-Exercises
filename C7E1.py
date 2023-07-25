# P4E - Chapter 7, Exercise 1
# Program que imprimi todas as linhas de um arquivo .txt em caixa alta

nomeArquivo = input("Digite o nome do arquivo: ")

try:
    arquivo = open(nomeArquivo)
except:
    print(f"\nO arquivo {nomeArquivo} não foi encontrado. Verifique o nome e tente novamente.\n")
    exit()

for linha in arquivo:
    linha = linha.upper().rstrip()
    print(linha)