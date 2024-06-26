from palindromo import is_palindromo


def teste_tres_letras():
    assert is_palindromo("ovo") == True # -> É um palíndromo

def teste_cinco_letras():
    assert is_palindromo("arara") == True #-> É um palíndromo

def teste_nao_palindromo():
    assert is_palindromo("reconhecer") == False #-> Não é um palíndromo

def teste_nao_palindromo_curta():
    assert is_palindromo("Python") == False #-> Não é um palíndromo

def teste_palindromo_frase():
    assert is_palindromo("A man, a plan, a canal, Panama!") == True #-> É um palíndromo
    
def teste_nao_palindromo_frase():
    assert is_palindromo("Anita lava a tina") == False # -> Não é um palíndromo

def teste_palindromo_frase_grande():
    assert is_palindromo("Was it a car or a cat I saw?") == True #-> É um palíndromo

def teste_palindromo_frase_com_sinais():
    assert is_palindromo("Hello, World!") == False # -> Não é um palíndromo


