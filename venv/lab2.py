import numpy as np

def decision(x, y, a):
    """
    Считаем количество нулей в столбцах и стркоах
    :param x: количетсво строк
    :param y: количество столбцов
    :param a: исходная матрциа
    :return:
    """
    k = (a == 0).sum(0)
    b = np.vstack([a, k])
    k = (b == 0).sum(1)
    c = np.column_stack([b, k])
    c[x][y] = 0
    print(c)
    return c


def output(c):
    """
    Вывод решения в файл
    :param c: Матрица
    :return:
    """
    with open('output.txt', 'w') as f:
        c = str(c)
        f.write(c)
        f.close()


print("Введите количество строк")
x = int(input())
print("Введите количество столбцов")
y = int(input())
a = np.random.randint(0, 2, (x, y))
print(a)
print("______")
c = decision(x, y, a)
output(c)
