import numpy as np


def cal_euclidean(a, b):
    square = np.square(a - b)
    sum_square = np.sum(square)
    distance = np.sqrt(sum_square)
    return distance

def cal_manhattan(a, b):
    modul = np.abs(a - b)
    distance = np.sum(modul)
    return distance

def cal_cosine(a, b):
    umno = np.dot(a, b)
    n1 = np.linalg.norm(a)
    n2 = np.linalg.norm(b)
    distance = 1 - (umno / (n1 * n2))
    return distance

a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))