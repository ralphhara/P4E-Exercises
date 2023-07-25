# P4E - Chapter 5, Exercise 2
# Programa que coleta entradas numéricas e retorna o número máximo e o mínimo

num = 0
max = 0
min = None

print('\nDigite um número ou "pronto" quando quiser parar o programa\n')

while True:
    num = input("Digite um número: ")
    if num == "pronto" or num == "Pronto":
        break
    try:
        num = int(num)
        print(num)
    except:
        print('\nDigite apenas números ou "pronto" para parar o programa.\n')
        continue
    
    if num > max:
        max = num
    if min is None:
        min = num
    elif num < min:
        min = num
    
    


print("\nPrograma Finalizado\n")
print("Maior número digitado: ", max)
print("Menor número digitado: ", min)