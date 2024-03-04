
def share_bread(N, K):
    x = round(K // N)
    y = K - N * x
    return x, y

# если в функции всё верно, то после выполнения этой строчки, не должно выскакивать ошибок
assert share_bread(N=3, K=14) == (4, 2)


def leap_year(year):
    if year % 400 == 0:
        text_result = 'YOU SHALL PASS'
    elif year % 100 == 0:
        text_result = 'YOU SHALL NOT PASS'
    elif year % 4 == 0:
        text_result = 'YOU SHALL PASS'
    else:
        text_result = 'YOU SHALL NOT PASS'
    return text_result

assert leap_year(5) == 'YOU SHALL NOT PASS'


a = np.random.randint(-10, 10, size=10)
print(a)
