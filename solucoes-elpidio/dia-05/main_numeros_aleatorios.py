import random

numeros = []
while len(numeros) < 6:
    numero_random = random.randint(1,60)
    if numero_random not in numeros:
        numeros.append(numero_random)
    


print("Números da Mega-Sena:", sorted(numeros))