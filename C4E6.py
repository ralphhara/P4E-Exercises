# P4E - Chapter 4, Exercise 6

def calculoPagamento(horas, taxaHora):
    if horas >= 40:
        he = horas - 40
        valorHE =  he * taxaHora * 1.5
        valor = (horas - he) * taxaHora + valorHE
    else:
        valor = horas * taxaHora
    return valor

print("\nCalculadora de taxa de serviço\n")
hr = input("Digite a quantidade de horas trabalhadas: ")
tx = input("Digite a taxa: ")

try:
    hr = float(hr)
    tx = float(tx)
except:
    print("\nPor favor, utilize apenas numeros!\n")
    quit()

print("\nValor a ser pago: ", calculoPagamento(hr, tx), "\n")