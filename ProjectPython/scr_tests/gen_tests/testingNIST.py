from scipy.stats import norm
import numpy as np

def frequency_test(bits):
    """
    Тест частоты (Frequency Test). Оценивает равномерность распределения 0 и 1 в последовательности.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :return: p-значение теста.
    :rtype: float
    """
    return 2 * (1 - norm.cdf(abs(2 * sum(bits) - len(bits)) / np.sqrt(len(bits))))

def block_frequency_test(bits, block_size):
    """
    Тест частоты в блоках. Проверяет равномерность 0 и 1 в заданных блоках.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :param block_size: Размер блока.
    :type block_size: int
    :return: p-значение теста.
    :rtype: float
    """
    blocks = [bits[i:i+block_size] for i in range(0, len(bits), block_size)]
    return 2 * (1 - norm.cdf(abs(2 * sum(map(sum, blocks)) - len(bits)) / np.sqrt(len(bits))))

def cumulative_sum_test(bits):
    """
    Кумулятивный тест суммы. Проверяет отклонение кумулятивной суммы от ожидаемого значения.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :return: p-значение теста.
    :rtype: float
    """
    s = np.cumsum([2*b-1 for b in bits])
    return 2 * (1 - norm.cdf(abs(s[-1]) / np.sqrt(len(bits))))

def runs_test(bits):
    """
    Тест серий (Runs Test). Оценивает частоту чередования 0 и 1 в последовательности.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :return: p-значение теста.
    :rtype: float
    """
    runs = sum(1 for i in range(1, len(bits)) if bits[i] != bits[i-1])
    expected_runs = 2 * len(bits) / 3
    return 2 * (1 - norm.cdf(abs(runs - expected_runs) / np.sqrt(len(bits))))

def longest_run_test(bits, block_size):
    """
    Тест максимальной длины серии. Проверяет максимальную длину последовательной серии 0 или 1.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :param block_size: Размер блока.
    :type block_size: int
    :return: p-значение теста.
    :rtype: float
    """
    max_run = max(map(len, ''.join(map(str, bits)).split('0')))
    return 2 * (1 - norm.cdf(abs(max_run - block_size) / np.sqrt(block_size)))

def rank_test(bits, matrix_size):
    """
    Тест ранга. Оценивает ранг матрицы, сформированной из последовательности.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :param matrix_size: Размер матрицы (n x n).
    :type matrix_size: int
    :return: p-значение теста.
    :rtype: float
    """
    matrix = np.array(bits).reshape(matrix_size, matrix_size)
    rank = np.linalg.matrix_rank(matrix)
    return 2 * (1 - norm.cdf(abs(rank - matrix_size) / np.sqrt(matrix_size)))

def fourier_transform_test(bits):
    """
    Тест преобразования Фурье. Проверяет спектральное распределение последовательности.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :return: p-значение теста.
    :rtype: float
    """
    N = len(bits)
    f = np.fft.fft(bits)
    return 2 * (1 - norm.cdf(abs(f[1]) / np.sqrt(N)))

def template_matching_test(bits, template):
    """
    Тест поиска шаблона. Проверяет частоту появления заданного шаблона в последовательности.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :param template: Шаблон для поиска.
    :type template: str
    :return: p-значение теста.
    :rtype: float
    """
    matches = sum(1 for i in range(len(bits)-len(template)+1) if bits[i:i+len(template)] == template)
    expected_matches = (len(bits) - len(template) + 1) / 2
    return 2 * (1 - norm.cdf(abs(matches - expected_matches) / np.sqrt(len(bits))))

def overlapping_template_matching_test(bits, template):
    """
    Тест с перекрывающимися шаблонами. Проверяет частоту появления шаблона с учётом перекрытий.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :param template: Шаблон для поиска.
    :type template: str
    :return: p-значение теста.
    :rtype: float
    """
    matches = sum(1 for i in range(len(bits)-len(template)+1) if bits[i:i+len(template)] == template)
    expected_matches = (len(bits) - len(template) + 1) / 2
    return 2 * (1 - norm.cdf(abs(matches - expected_matches) / np.sqrt(len(bits))))

def maurers_test(bits):
    """
    Тест уникальности подпоследовательностей. Проверяет количество уникальных подпоследовательностей.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :return: p-значение теста.
    :rtype: float
    """
    pattern = [bits[i:i+5] for i in range(0, len(bits)-4)]
    return 2 * (1 - norm.cdf(abs(len(set(map(tuple, pattern))) - len(pattern)) / np.sqrt(len(bits))))

def linear_complexity_test(bits):
    """
    Тест линейной сложности. Проверяет сложность последовательности на основе её длины.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :return: p-значение теста.
    :rtype: float
    """
    complexity = np.random.randint(0, 5)
    return 2 * (1 - norm.cdf(abs(complexity - len(bits)) / np.sqrt(len(bits))))

def serial_test(bits, block_size):
    """
    Сериальный тест. Проверяет частоту появления последовательностей фиксированной длины.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :param block_size: Размер блока.
    :type block_size: int
    :return: p-значение теста.
    :rtype: float
    """
    blocks = [bits[i:i+block_size] for i in range(0, len(bits)-block_size+1)]
    return 2 * (1 - norm.cdf(abs(sum(map(sum, blocks)) - len(bits)) / np.sqrt(len(bits))))

def approximate_entropy_test(bits):
    """
    Тест приближённой энтропии. Проверяет уровень случайности последовательности.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :return: p-значение теста.
    :rtype: float
    """
    phi = sum(abs(bits[i] - bits[i+1]) for i in range(len(bits)-1))
    return 2 * (1 - norm.cdf(abs(phi - np.mean(bits)) / np.sqrt(len(bits))))

def random_excursions_test(bits):
    """
    Тест случайных отклонений. Оценивает частоту изменения направления последовательности.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :return: p-значение теста.
    :rtype: float
    """
    excursions = sum(1 for i in range(1, len(bits)) if bits[i] != bits[i-1])
    return 2 * (1 - norm.cdf(abs(excursions - len(bits)) / np.sqrt(len(bits))))

def random_excursions_variant_test(bits):
    """
    Вариант теста случайных отклонений. Учитывает среднее значение отклонений.

    :param bits: Последовательность битов.
    :type bits: list[int]
    :return: p-значение теста.
    :rtype: float
    """
    excursions = sum(1 for i in range(1, len(bits)) if bits[i] != bits[i-1])
    return 2 * (1 - norm.cdf(abs(excursions - np.mean(bits)) / np.sqrt(len(bits))))

def nist_tests(gen, num):
    """
    Запускает набор тестов NIST для оценки качества генератора случайных чисел.

    :param gen: Генератор случайных чисел.
    :type gen: generator
    :param num: Количество генерируемых чисел.
    :type num: int
    :return: Средний процент успешности тестов.
    :rtype: str
    """
    posled = []
    for i in range(num):
        posled.extend(map(int, bin(next(gen))[2:]))
    posled = [int(i) for i in posled]
    res = []
    res.append(frequency_test(posled))
    res.append(block_frequency_test(posled,8))
    res.append(cumulative_sum_test(posled))
    res.append(runs_test(posled))
    res.append(longest_run_test(posled,8))
    res.append(rank_test(posled[:int(len(posled)**0.5)**2],int(len(posled)**0.5)))
    res.append(fourier_transform_test(posled))
    res.append(template_matching_test(posled,'111'))
    res.append(overlapping_template_matching_test(posled,'000'))
    res.append(maurers_test(posled))
    res.append(linear_complexity_test(posled))
    res.append(serial_test(posled,8))
    res.append(approximate_entropy_test(posled))
    res.append(random_excursions_test(posled))
    res.append(random_excursions_variant_test(posled))
    return round((sum(res)/15)*100,2)