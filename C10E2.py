# P4E - Chapter 10, Exercise 2
# Programa que verifica o horario em que os emails foram recebidas e ordena
# de forma crescente

txt = open('mbox-short.txt')

horarios = list()

print("\nContagem de mensagens por horário:\n")

for linha in txt:
    linha = linha.rstrip()
    if linha.startswith('From '):
        linha = linha.split()
        linha = linha[5].split(':')
        horarios.append(linha[0])

cont = dict()

for hora in horarios:
    cont[hora] = cont.get(hora, 0) + 1

l = list()

for i in cont.items():
    l.append(i)

l.sort()

print("Hora | Qtd Msg")
for k, v in l:
    print(f" {k}  |   {v} ")

print()