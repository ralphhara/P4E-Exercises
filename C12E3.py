# P4E - Chapter 12, Exercise 3
# Navegador web simple desenvolvido em Python com contagem de caracteres usando urllib

import urllib.request

print("\nBem-vindo ao Navegador Web Python\n")

print("Digite o endereço completo do site (URL) que deseja visitar incluindo o http:// or https:// e o nome do arquivo.\n")
print("Exemplo:")
print("http://data.pr4e.org/romeo.txt\n")

while True:
    link = input("URL: ")
    try:
        pagina = urllib.request.urlopen(f'{link}')
        break
    except:
         print("Por favor digite o endereço do site (URL).")
         continue

print("\nInicio do conteudo do site:\n")

cont = 0

for linha in pagina:
    cont += len(linha.decode().strip())
    if cont <= 3000:
        print(linha.decode().strip())

print(f"\nMostrando apenas os primeiros 3000 caracteres de {cont}\n")