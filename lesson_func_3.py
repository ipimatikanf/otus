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