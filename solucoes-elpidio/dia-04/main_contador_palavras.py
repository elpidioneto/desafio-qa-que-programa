from contador_palavras import contador_palavras

texto = input ("Digite sua palavra ou texto para contarmos as palavras: ")

count = contador_palavras(texto)

print(f"Seu texto possui {count} palavras" if count > 1 else f"Seu texto possui {count} palavra")