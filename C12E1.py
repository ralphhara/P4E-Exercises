# P4E - Chapter 12, Exercise 1
# Navegador web simple desenvolvido em Python

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

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

print()