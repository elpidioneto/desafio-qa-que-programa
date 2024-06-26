from contador_palavras import contador_palavras

def teste_basico():
    assert contador_palavras("Isso é um teste.") == 4 # -> O texto contém 4 palavras.

def teste_com_espacos_no_comeco():
    assert contador_palavras("   Olá,    mundo!   ") == 2 # -> O texto contém 2 palavras.

def teste_palavra_repetida():
    assert contador_palavras("Palavra Palavra palavra") == 3 # -> O texto contém 3 palavras.

def teste_contagem_frase_media():
    assert contador_palavras("Este é um teste de contagem de palavras.") == 8 # -> O texto contém 8 palavras.

def teste_string_vazia():
    assert contador_palavras("") == 0 # -> Número de palavras: O texto contém 0 palavras.

def teste_com_numero():
    assert contador_palavras("Maria tem 10 anos.") == 4 # -> O texto contém 4 palavras.

def teste_com_virgula_espacada():
    assert contador_palavras("Olá ,  Mundo") == 3 # -> O texto contém 3 palavras.

def teste_frase_muito_comprida():
    assert contador_palavras("Em uma tarde ensolarada, 3 crianças brincavam no parque. De repente, encontraram um mapa misterioso, com anotações enigmáticas: 'Vire à esquerda, depois à direita, e avance 100 passos!' Eles, empolgados, seguiram as instruções cuidadosamente, contando cada passo com atenção. No caminho , encontraram diversos obstáculos: pedras, galhos e até um riacho raso. O mapa os levou a uma árvore antiga, com raízes grossas e folhas densas. 'Aqui deve ser!', exclamou João, o mais velho. Mas,   sob a árvore, só encontraram uma caixa vazia e um bilhete: 'A verdadeira aventura está na jornada, não no destino. Parabéns por chegarem até aqui!' Desapontados, mas ainda animados, decidiram continuar explorando. 'Vamos ver o que mais podemos descobrir!', disse Maria, a mais aventureira do grupo. E assim, a busca por tesouros se transformou em uma tarde de descobertas e diversão. No final, o que realmente importava era a amizade e as memórias que criaram juntos.") == 151 # -> O texto contém 151 palavras.

def teste_uma_palavra():
    assert contador_palavras("Oi") == 1 # -> O texto contém 1 palavras.