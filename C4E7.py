# P4E - Chapter 4, Exercise 7

def computarNotas(ponto):
    if ponto >= 0.9:
        return "A"
    elif ponto >= 0.8:
        return "B"
    elif ponto >= 0.7:
        return "C"
    elif ponto >= 0.6:
        return "D"
    else:
        return "F"
    
print("\nConversão de pontução para nota\n")

pt = input("Digite uma pontuação entre 0.0 e 1.0: ")

try:
    pt = float(pt)
except:
    print("\nFavor utilizar apenas números!\n")
    quit()

print(f"\n{pt} pontos é equivalente a nota {computarNotas(pt)}\n")