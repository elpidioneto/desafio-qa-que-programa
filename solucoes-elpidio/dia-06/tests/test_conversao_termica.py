import conversao_termica

def teste_converter_zero_celsius_para_fahrenheit():
    resultado = conversao_termica.celsius_para_fahrenheit(0)
    assert resultado == 32.0
def teste_converter_celsius_para_fahrenheit():
    resultado = conversao_termica.celsius_para_fahrenheit(42)
    assert resultado == 107.6
def teste_converter_negativo_celsius_para_fahrenheit():
    resultado = conversao_termica.celsius_para_fahrenheit(-3)
    assert resultado == 26.6

def teste_converter_zero_fahrenheit_para_celsius():
    resultado = conversao_termica.fahrenheit_para_celsius(0)
    assert resultado == -17.7778

def teste_converter_fahrenheit_para_celsius():
    resultado = conversao_termica.fahrenheit_para_celsius(100)
    assert resultado == 37.7778

def teste_converter_negativo_fahrenheit_para_celsius():
    resultado = conversao_termica.fahrenheit_para_celsius(-11)
    assert resultado == -23.8889
    
# TESTE 05: Converter 0 graus Celsius para Fahrenheit -> Resultado da conversão: 32.0
# TESTE 06: Converter 42 graus Celsius para Fahrenheit -> Resultado da conversão: 107.6
# TESTE 07: Converter -3 graus Celsius para Fahrenheit -> Resultado da conversão: 26.6
# TESTE 08: Converter 0 graus Fahrenheit para Celsius -> Resultado da conversão: -17.7778
# TESTE 09: Converter 100 graus Fahrenheit para Celsius -> Resultado da conversão: 37.7778
# TESTE 10: Converter -11 graus Fahrenheit para Celsius -> Resultado da conversão: -23.8889