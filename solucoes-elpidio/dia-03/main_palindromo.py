from palindromo import is_palindromo

texto_recebido = input("Digite um texto e descubra se é ou não um palíndromo: ")

print("É um palíndromo" if is_palindromo(texto_recebido) else "Não é um palíndromo")