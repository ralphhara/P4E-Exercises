# P4E - Chapter 7, Exercise 2
# Programa procura por uma determinada string em um arquivo .txt

nomeArquivo = input("Digite o nome do arquivo: ")

try:
    arquivo = open(nomeArquivo)
except:
    print(f"\nO arquivo {nomeArquivo} não foi encontrado. Verifique o nome e tente novamente.\n")
    exit()

numLinhas = 0
totalConf = 0

for linha in arquivo:
    linha = linha.rstrip()
    if linha.startswith('X-DSPAM-Confidence:'):
        totalConf += float(linha.removeprefix('X-DSPAM-Confidence:'))
        numLinhas += 1

print("\nNumero de linhas encontradas: ", numLinhas)
print("Media de confiança de SPAM: ", round((totalConf/numLinhas), 2))