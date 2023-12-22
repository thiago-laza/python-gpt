def media(l):
    acu = 0
    for n in l:
        acu += n
    media_valores = acu / len(l)
    return f'A media dos valores de {l} e igual a {media_valores}'
