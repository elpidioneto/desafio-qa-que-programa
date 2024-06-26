
def paridade(numero):
    try:
        numero = int(numero)

        print (f"Numéro {numero} é par!" if numero % 2 == 0 else f"Numéro {numero} é ímpar")

    except:

        print("Valor tem que ser numérico! Refaça a operação")
        paridade(input("digite um número: "))

paridade(input("digite um número: "))