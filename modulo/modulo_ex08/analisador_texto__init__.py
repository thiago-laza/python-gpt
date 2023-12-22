def contador_palavras(t):
    global cont_espaco
    cont_espaco = 0
    if t[0] == ' ':
        cont_espaco -= 1
    if t[len(t) - 1] == ' ':
        cont_espaco -= 1
    for n in t:
        if n == ' ':
            cont_espaco += 1
    return f'Foram identificadas {cont_espaco + 1} palavras.'


def media_palavras(t):
    media = round((len(t) - cont_espaco) / (cont_espaco + 1))
    return f'As palavras tem em media {media} letras.'

