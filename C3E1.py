print("\nCalculadora de taxa de serviço\n")
horas = float(input("Digite a quantidade de horas trabalhadas: "))
taxa = float(input("Digite a taxa: "))

if horas >= 40:
    he = (horas - 40)
    valorHE = he * taxa * 1.5
    valor = (horas - he) * taxa + valorHE
    print("\nValor a ser pago: ", valor)
else:
    valor = horas * taxa
    print("\nValor a ser pago: ", valor)