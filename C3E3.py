# P4E - Chapter 3, Exercise 3

print("\nConversão de pontução para nota\n")

ponto = input("Digite uma pontuação entre 0.0 e 1.0: ")

try:
    ponto = float(ponto)
except:
    print("\nFavor utilizar apenas números!\n")
    quit()

if ponto >= 0.9:
    print("Nota: A")
elif ponto >= 0.8:
    print("Nota: B")
elif ponto >= 0.7:
    print("Nota: C")
elif ponto >= 0.6:
    print("Nota: D")
else:
    print("Nota: F")