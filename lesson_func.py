def probel(a: int) ->str:
    my_list = list(str(a))
    if len(str(a)) % 3 == 0:
        for i in range(2, len(str(a)) - 1, 3):
            my_list[i] = my_list[i] + ' '
    elif len(str(a)) % 3 == 1:
        for i in range(0, len(str(a)) - 1, 3):
            my_list[i] = my_list[i] + ' '
    else:
        for i in range(1, len(str(a)) - 1, 3):
            my_list[i] = my_list[i] + ' '
    return f'Разделение на разряды\nВведено: {a}\nРезультат: {"".join(my_list)}\n'

print(probel(1234567890))


def camel(b: str):
    num = len(b)
    my_list = list(str(b))
    if my_list[0].isupper() == True:
        for i in range(1,num):
            if my_list[i].isupper() == True:
                my_list[i] = '_' + my_list[i]
            else:
                continue
        return f'КамелКейс на Cнейк_кейс\nВведено: {b}\nРезультат: {"".join(my_list).lower()}\n'
    else:
        my_replace = b.replace('_', ' ')
        my_upper = [i[0].upper() + i[1:] for i in my_replace.split()]
        result = " ".join(my_upper)
        return f'Cнейк_кейс на КамелКейс\nВведено: {b}\nРезультат: {result.replace(" ", "")}\n'

print(camel('MyFirstFunc'))

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

import re
def uravnenie(g: str):
    my_list = re.split('=|-|\+|\*|x|X| ', g)
    num_list = []
    for i in my_list:
        if i.strip() == '':
            pass
        else:
            if int(i.strip()) > 0:
                num_list.append(int(i.strip()))
    k_a, k_b, k_c = int(num_list[0]), int(num_list[2]), int(num_list[3])
    k_d = k_b**2 - 4*k_a*k_c
    if k_d > 0:
        x_1 = (k_b - sqrt(k_d)) // (2 * k_a)
        x_2 = (k_b + sqrt(k_d)) // (2 * k_a)
        return f'Квадратное уравнение\nВведено: {g}\nРезультат: x_1 = {x_1}, x_2 = {x_2}'
    elif k_d == 0:
        x_1 = k_b // (2 * k_a)
        return f'Квадратное уравнение\nВведено: {g}\nРезультат: x_1 = {x_1}'
    else:
        return f'Квадратное уравнение\nВведено: {g}\nРезультат: "Корней нет"'

print(uravnenie('3*x**2 - 4*x + 9 = 0'))