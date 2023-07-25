# P4E - Chapter 12, Exercise 4
# Navegador web simples desenvolvido em Python usando BeatifulSoup para contagem de tags
# de paragrafo <p> HTML.
#
#
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# biblioteca importada para resolver erro "collections.Callable"
import collections
collections.Callable = collections.abc.Callable

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("\nBem-vindo ao Navegador Web Python\n")

print("Digite o endereço completo do site (URL) que deseja visitar incluindo o http:// or https:// e o nome do arquivo.\n")
print("Exemplo:")
print("http://data.pr4e.org/romeo.txt\n")

while True:
    link = input("URL: ")
    try:
        html = urllib.request.urlopen(link, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        break
    except:
         print("Por favor digite o endereço do site (URL).")
         continue

cont = 0

# Retrieve all of the anchor tags
tags = soup('p')
for tag in tags:
    cont += 1

print(f"\nForam encontrada(s) {cont} tag(s) de link HTML\n")