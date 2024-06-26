import calculadora

def teste_basico_soma():
    resultado_atual = calculadora.calculadora("1 + 5")
    assert resultado_atual == 6

def teste_basico_subtracao():
    resultado_atual = calculadora.calculadora("5 - 1")
    assert resultado_atual == 4

def teste_basico_multipicacao():
    resultado_atual = calculadora.calculadora("2 x 30")
    assert resultado_atual == 60

def teste_basico_divisao():
    resultado_atual = calculadora.calculadora("21 / 7")
    assert resultado_atual == 3

def teste_divisao_zero():
    resultado_atual = calculadora.calculadora("10 / 0")
    assert resultado_atual == "Não é possível dividir por zero"

def teste_soma_negativo():
    resultado_atual = calculadora.calculadora("1 + -5")
    assert resultado_atual == -4

def teste_subtracao_negativo():
    resultado_atual = calculadora.calculadora("5 - -1")
    assert resultado_atual == 6

def teste_multiplicacao_negativo():
    resultado_atual = calculadora.calculadora("2 x -30")
    assert resultado_atual == -60

def teste_divisao_negativo():
    resultado_atual = calculadora.calculadora("-21 / 7")
    assert resultado_atual == -3

def teste_divisao_zero_negativo():
    resultado_atual = calculadora.calculadora("-10 / 0")
    assert resultado_atual == "Não é possível dividir por zero"
