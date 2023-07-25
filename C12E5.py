# P4E - Chapter 12, Exercise 5
# Altere o programa de socket1.py para que ele apenas mostre uma informação depois dos cabeçalhos
# e uma linha em branco ser recebida. Lembre que recv recebe caracteres (newlines e etc), não linhas.

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from bs4 import BeautifulSoup
import socket

# biblioteca importada para resolver erro "collections.Callable" do BeatifulSoup
import collections
collections.Callable = collections.abc.Callable


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

pagina = ''

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    pagina += data.decode()

mysock.close()

soup = BeautifulSoup(pagina, 'html.parser')

print(soup.prettify())

#print(f"\n{soup}\n")