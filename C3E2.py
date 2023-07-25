# P4E - Chapter 3, Exercise 2

print("\nCalculadora de taxa de serviço\n")
horas = input("Digite a quantidade de horas trabalhadas: ")
taxa = input("Digite a taxa: ")

try:
    horas = float(horas)
    taxa = float(taxa)
except:
    print("\nPor favor, utilize apenas numeros!\n")
    quit()

if horas >= 40:
    he = horas - 40
    valorHE = he * taxa * 1.5
    valor = (horas - he) * taxa + valorHE
    print("\nValor a ser pago: ", valor)
else:
    valor = horas * taxa
    print("\nValor a ser pago: ", valor)