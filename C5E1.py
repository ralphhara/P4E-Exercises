# P4E - Chapter 5, Exercise 1
# Programa que coleta entradas numéricas e retorna a quantidade de números,
# a soma e a média

num = 0
soma = 0
contador = 0

print('\nDigite um número ou "pronto" quando quiser parar o programa\n')

while True:
    num = input("Digite um número: ")
    if num == "pronto" or num == "Pronto":
        break
    try:
        num = float(num)
        print(num)
    except:
        print('\nDigite apenas números ou "pronto" para parar o programa.\n')
        continue
    
    contador += 1
    soma = soma + num

print("\nPrograma Finalizado\n")
print("Quantidade de números digitados: ", contador)
print("Soma dos números digitados: ", soma)
print("Media: ", soma / contador)