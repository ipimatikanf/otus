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