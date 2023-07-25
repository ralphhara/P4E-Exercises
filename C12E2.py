# P4E - Chapter 12, Exercise 2
# Navegador web simple desenvolvido em Python com contagem de caracteres

import socket

print("\nBem-vindo ao Navegador Web Python\n")

print("Digite o endereço completo do site (URL) que deseja visitar incluindo o http:// or https:// e o nome do arquivo.\n")
print("Exemplo:")
print("http://data.pr4e.org/romeo.txt\n")

while True:
    link = input("URL: ")
    try:
        # Coletando apenas dominio do web site
        dominio = link.split('/')
        dominio = dominio[2].removeprefix('www.')
        break
    except:
         print("Por favor digite o endereço do site (URL).")
         continue

print("\nInicio do conteudo do site:\n")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((dominio, 80))
cmd = f'GET {link} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

texto = ''

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    texto = texto + data.decode()

mysock.close()

novoTexto = ''
cont = 3000

for i in texto:
    if cont >= 0:
        novoTexto = novoTexto + i
        cont -= 1

print(novoTexto)
print(f"\nTotal de caracteres: {len(texto)}\n")