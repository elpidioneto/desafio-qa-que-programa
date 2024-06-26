import conversao_metrica
import conversao_termica

print('================ Calculadora de conversão =====================')

opcao = input("""Escolha uma das opções abaixo: \n 0. Conversão Termica \n 1. Conversão Metrica\n""")

if opcao == "0":
    op_temp= input("""Escolha a conversão desejada: \n 0. Celsius para Fahrenheit \n 1. Fahrenheit para Celsius\n""")
    valor = int(input("Digite o valor para conversão: "))
    if op_temp == "0":
        print(f"debug valor é {valor}")
        print(f"Valor de {valor} Celsius em Fahrenheit é {conversao_termica.celsius_para_fahrenheit(valor)}")

    if op_temp == "1":
        print(f"Valor de {valor} Fahrenheit em Celsius é {conversao_termica.fahrenheit_para_celsius(valor)}")

if opcao == "1":
    op_met=input("""Escolha a conversão desejada:
0. Quilometros para milhas
1. Milhas para Quilometros
2. Metros para pês
3. Pês para metros\n
""")
    valor = int(input("Digite o valor desejado: "))

    if op_met == "0":
        print(f"A conversão de {valor} quilometros em milhas é {conversao_metrica.quilometro_para_milhas(valor)}")
    if op_met == "1":
        print(f"A conversão de {valor} milhas em quilometro é {conversao_metrica.milhas_para_quilometro(valor)}")
    if op_met == "2":
        print(f"A conversão de {valor} Metros para pês é {conversao_metrica.metro_para_pes(valor)}")
    if op_met == "3":
        print(f"A conversão de {valor} pês para metros é {conversao_metrica.pes_para_metro(valor)}")

