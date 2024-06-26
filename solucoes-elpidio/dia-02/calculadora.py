def calculadora(expressao):
    try:
        expressao = expressao.replace("x", "*")
        expressao = expressao.replace(",", ".")
        return(eval(expressao))

    except ZeroDivisionError as e:
        return("Não é possível dividir por zero")
    except Exception as e:
        return("Valor digitado invalido! Tente novamente")

