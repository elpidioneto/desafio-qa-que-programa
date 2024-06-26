import conversao_metrica

def teste_converter_quilometro_para_milhas():
    resultado = conversao_metrica.quilometro_para_milhas(10)
    assert resultado == 6.2137

def teste_converter_milhas_para_quilometro():
    resultado = conversao_metrica.milhas_para_quilometro(20)
    assert resultado == 32.18

def teste_converter_metros_para_pes():
    resultado = conversao_metrica.metro_para_pes(5)
    assert resultado == 16.4042

def teste_converter_pes_para_metros():
    resultado = conversao_metrica.pes_para_metro(100)
    assert resultado == 30.48
# TESTE 01: Converter 10 quilômetros para milhas -> Resultado da conversão: 6.21371
# TESTE 02: Converter 20 milhas para quilômetros -> Resultado da conversão: 32.1868
# TESTE 03: Converter 5 metros para pés -> Resultado da conversão: 16.4042
# TESTE 04: Converter 100 pés para metros -> Resultado da conversão: 30.48