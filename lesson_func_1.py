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