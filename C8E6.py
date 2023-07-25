# P4E - Chapter 8, Exercise 6
# Programa que coleta entradas numéricas em uma lista e retorna o maior e o menor número.

#num = 0
contador = 0

listaNum = list()

print('\nDigite um número ou "pronto" quando quiser parar o programa\n')

while True:
    num = input("Digite um número: ")
    if num == "pronto" or num == "Pronto":
        break
    try:
        num = int(num)
        listaNum.append(num)
        contador += 1
    except:
        print('\nDigite apenas números ou "pronto" para parar o programa.\n')
        continue
    
print("\nPrograma Finalizado\n")
print("Quantidade de números digitados: ", contador)
print("Maior número digitado: ", max(listaNum))
print("Menor número digitado: ", min(listaNum))
print()