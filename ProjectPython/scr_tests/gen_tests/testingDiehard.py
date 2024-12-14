import numpy as np
from scipy.stats import chisquare, norm

def birthday_spacings(samples, n, m):
    """
    Проверяет равномерность распределения расстояний между отсортированными образцами.

    :param samples: Массив образцов.
    :type samples: list[int] | np.ndarray
    :param n: Количество используемых образцов.
    :type n: int
    :param m: Число интервалов для гистограммы.
    :type m: int
    :return: p-значение теста хи-квадрат.
    :rtype: float
    """
    gaps = np.diff(np.sort(samples[:n]))[:m]
    counts, _ = np.histogram(gaps, bins=m)
    return chisquare(counts).pvalue

def overlapping_permutations(samples, k):
    """
    Оценивает частоту перекрывающихся перестановок длины `k`.

    :param samples: Массив образцов.
    :type samples: list[int] | np.ndarray
    :param k: Длина последовательности для перестановок.
    :type k: int
    :return: p-значение теста хи-квадрат.
    :rtype: float
    """
    seqs = [tuple(samples[i:i+k]) for i in range(len(samples) - k + 1)]
    counts = np.unique(seqs, axis=0, return_counts=True)[1]
    return chisquare(counts).pvalue

def overlapping_quadruples(samples):
    """
    Проверяет частоту появления перекрывающихся кортежей длины 4.

    :param samples: Массив образцов.
    :type samples: list[int] | np.ndarray
    :return: p-значение теста хи-квадрат.
    :rtype: float
    """
    quadruples = [tuple(samples[i:i+4]) for i in range(len(samples) - 3)]
    counts = np.unique(quadruples, axis=0, return_counts=True)[1]
    return chisquare(counts).pvalue

def count_the_1s(samples):
    """
    Проверяет распределение количества единиц в битовом представлении чисел.

    :param samples: Массив образцов.
    :type samples: list[int] | np.ndarray
    :return: p-значение теста хи-квадрат.
    :rtype: float
    """
    bit_counts = [bin(x).count('1') for x in samples]
    counts, _ = np.histogram(bit_counts, bins=range(max(bit_counts) + 2))
    return chisquare(counts).pvalue

def parking_lot_test(samples, n, size):
    """
    Проверяет плотность расположения точек в заданной области.

    :param samples: Массив образцов.
    :type samples: list[int] | np.ndarray
    :param n: Количество точек.
    :type n: int
    :param size: Размер области.
    :type size: int
    :return: Среднее расстояние между точками.
    :rtype: float
    """
    points = np.array(samples[:n]).reshape(-1, 2) * size
    occupied = [np.linalg.norm(p1 - p2) > 1 for i, p1 in enumerate(points) for p2 in points[i+1:]]
    return np.mean(occupied)

def minimum_distance_test(samples, n):
    """
    Проверяет минимальные расстояния между точками в выборке.

    :param samples: Массив образцов.
    :type samples: list[int] | np.ndarray
    :param n: Количество точек.
    :type n: int
    :return: p-значение теста хи-квадрат.
    :rtype: float
    """
    points = np.array(samples[:n]).reshape(-1, 2)
    min_dists = [np.min(np.linalg.norm(points[i] - points[:i], axis=1)) for i in range(1, len(points))]
    return chisquare(min_dists).pvalue

def overlapping_sums(samples, k):
    """
    Оценивает равномерность суммы перекрывающихся подвыборок длины `k`.

    :param samples: Массив образцов.
    :type samples: list[int] | np.ndarray
    :param k: Длина перекрывающихся подвыборок.
    :type k: int
    :return: p-значение теста хи-квадрат.
    :rtype: float
    """
    sums = [np.sum(samples[i:i+k]) for i in range(len(samples) - k + 1)]
    return chisquare(sums).pvalue

def diehard_tests(gen,num):
    """
    Выполняет серию тестов Diehard для проверки качества генератора псевдослучайных чисел.

    :param gen: Генератор псевдослучайных чисел.
    :type gen: generator
    :param num: Количество генерируемых чисел для тестов.
    :type num: int
    :return: Средний процент успешности тестов.
    :rtype: str
    """
    posled = []
    for i in range(num):
        posled.append(next(gen))
    res = []
    res.append(birthday_spacings(posled,500,50))
    res.append(overlapping_permutations(posled,4))
    res.append(overlapping_quadruples(posled))
    res.append(count_the_1s(posled))
    res.append(parking_lot_test(posled,100,10))
    res.append(minimum_distance_test(posled,100))
    res.append(overlapping_sums(posled,10))
    return round((sum(res)/7)*100,2)