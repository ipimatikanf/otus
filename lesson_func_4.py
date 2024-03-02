def shifr(c: str, d: int):
    slov = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    my_list = list(c.lower())
    for i in range(len(my_list)):
        var = int(slov.index(my_list[i])) + d
        if var > 25:
            var = var - 26
            my_list[i] = slov[var]
        else:
            my_list[i] = str(slov[var])
    return f'Кодирование\nВведено: слово-{c}, код-{d}.\nРезультат: "{"".join(my_list)}"\n'

print(shifr('Dog', 5))

def decoder(e: str, f: int):
    slov = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    my_list = list(e.lower())
    for i in range(len(my_list)):
        var = int(slov.index(my_list[i])) - f
        if var < 0:
            var = var + 26
            my_list[i] = slov[var]
        else:
            my_list[i] = str(slov[var])
    return f'Декодирование\nВведено: слово-{e}, код-{f}.\nРезультат: "{"".join(my_list)}"\n'

print(decoder('itl', 5))