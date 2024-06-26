def is_palindromo(txt):
    if(txt.isdigit()): 
        return "Tem que digitar um texto e não número"
    txt = txt.replace(" ", "")
    txt = txt.replace("!", "")
    txt = txt.replace("?", "")
    txt = txt.replace(",", "")
    txt = txt.replace(";", "")
    txt = txt.replace("-", "")
    txt = txt.replace("_", "")
    txt = txt.lower()
    print(txt)

    return txt == txt[::-1]

