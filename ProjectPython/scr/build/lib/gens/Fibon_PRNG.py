from gens.LCM import *

def preferences():
    """
    Генерирует начальную базу чисел для Lagged Fibonacci Generator (LFG).

    Использует линейный конгруэнтный генератор для создания последовательности чисел, 
    которая служит базой для работы LFG.

    :return: Список из 55 начальных чисел для Lagged Fibonacci Generator.
    :rtype: list[int]

    Алгоритм:
    - Используется линейный конгруэнтный генератор (`linear_congruential_generator`) с параметрами:
        - `m`: Модуль.
        - `a`: Множитель.
        - `c`: Приращение.
        - `seed`: Начальное значение (seed).
    - Генерируется 55 чисел, которые сохраняются в список `base`.
    """
    m: int = 2_147_483_648
    a: int = 594_156_893
    c: int = 75_692
    seed: int = 123_456_789
    gen = linear_congruential_generator(m, a, c, seed)
    size = 55
    base = []
    for i in range(size):
        x = next(gen)
        base.append(x)
    return base

def lagged_fibonacci_generator():
    """
    Генератор псевдослучайных чисел на основе Lagged Fibonacci Generator (LFG).

    Алгоритм основан на формуле:
        `x[n] = (x[n-24] + x[n-55]) % (2^m)`
    где `base` — начальная база из 55 чисел.

    :yield: Следующее псевдослучайное число в последовательности.
    :rtype: int

    Примечания:
    - Начальная база чисел создается с помощью функции `preferences`.
    - Размер базы составляет 55 чисел.
    - Используется сдвиг значений базы, чтобы обновлять последовательность в процессе генерации.
    """
    base = preferences()
    m: int = 8
    x = 0
    while True:
        x = (base[24] + base[-1])%(2**m)
        for i in range(54,0,-1):
            base[i] = base[i-1]
        base[0] = x
        yield x