from gens.LCM import *

def maclaren_marsaliya_generator():
    """
    Генератор псевдослучайных чисел на основе алгоритма Макларена-Марсальи.

    Алгоритм:
    - Использует два линейных конгруэнтных генератора (`genX` и `genY`) с различными параметрами.
    - Создает массив `v` длиной `k`, инициализируемый числами из `genX`.
    - На каждой итерации выбирает значение из `v` по индексу `j`, вычисленному на основе значения `genY`.
    - Замещает значение в массиве `v[j]` новым числом из `genX`.

    :yield: Следующее псевдослучайное число из массива `v`.
    :rtype: int

    Примечания:
    - Размер массива `v` задается параметром `k` (в данном случае `k = 128`).
    - Индекс `j` вычисляется по формуле:  
      `j = (k * y) // mY + ((k * y) % mY >= 0.5)`,  
      где `y` — очередное значение из `genY`, а `mY` — модуль генератора `genY`.
    """
    mX: int = 2_147_483_648
    aX: int = 594_156_893
    cX: int = 75_692
    seedX: int = 123_456_789
    genX = linear_congruential_generator(mX, aX, cX, seedX)

    mY: int = 2**32
    aY: int = 1_103_515_245
    cY: int = 12_345
    seedY: int = 436_524_372
    genY = linear_congruential_generator(mY, aY, cY, seedY)

    k = 128 #или 64, 256

    v = [0]
    for i in range(k):
        v.append(next(genX))
    while True:
        x = next(genX)
        y = next(genY)
        j = (k*y)//mY + ((k*y)%mY >= 0.5)
        yield v[j]
        v[j] = x