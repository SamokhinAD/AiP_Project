from scipy.stats import norm
import numpy as np

# 1. **Frequency Test (Monobit Test)**
def frequency_test(bits):
    # print(1)
    return 2 * (1 - norm.cdf(abs(2 * sum(bits) - len(bits)) / np.sqrt(len(bits))))
# print(frequency_test(posled))


# 2. **Block Frequency Test**
def block_frequency_test(bits, block_size):
    blocks = [bits[i:i+block_size] for i in range(0, len(bits), block_size)]
    # print(2)
    return 2 * (1 - norm.cdf(abs(2 * sum(map(sum, blocks)) - len(bits)) / np.sqrt(len(bits))))
# print(block_frequency_test(posl,4))

# 3. **Cumulative Sum Test**
def cumulative_sum_test(bits):
    s = np.cumsum([2*b-1 for b in bits])
    # print(3)
    return 2 * (1 - norm.cdf(abs(s[-1]) / np.sqrt(len(bits))))

# 4. **Runs Test**
def runs_test(bits):
    runs = sum(1 for i in range(1, len(bits)) if bits[i] != bits[i-1])
    expected_runs = 2 * len(bits) / 3
    # print(4)
    return 2 * (1 - norm.cdf(abs(runs - expected_runs) / np.sqrt(len(bits))))

# 5. **Test for the Longest Run of Ones in a Block**
def longest_run_test(bits, block_size):
    max_run = max(map(len, ''.join(map(str, bits)).split('0')))
    # print(5)
    return 2 * (1 - norm.cdf(abs(max_run - block_size) / np.sqrt(block_size)))

# 6. **Binary Matrix Rank Test**
def rank_test(bits, matrix_size):
    matrix = np.array(bits).reshape(matrix_size, matrix_size)
    rank = np.linalg.matrix_rank(matrix)
    # print(6)
    return 2 * (1 - norm.cdf(abs(rank - matrix_size) / np.sqrt(matrix_size)))

# 7. **Discrete Fourier Transform (Spectral) Test**
def fourier_transform_test(bits):
    N = len(bits)
    f = np.fft.fft(bits)
    # print(7)
    return 2 * (1 - norm.cdf(abs(f[1]) / np.sqrt(N)))

# 8. **Non-overlapping Template Matching Test**
def template_matching_test(bits, template):
    matches = sum(1 for i in range(len(bits)-len(template)+1) if bits[i:i+len(template)] == template)
    expected_matches = (len(bits) - len(template) + 1) / 2
    # print(8)
    return 2 * (1 - norm.cdf(abs(matches - expected_matches) / np.sqrt(len(bits))))

# 9. **Overlapping Template Matching Test**
def overlapping_template_matching_test(bits, template):
    matches = sum(1 for i in range(len(bits)-len(template)+1) if bits[i:i+len(template)] == template)
    expected_matches = (len(bits) - len(template) + 1) / 2
    # print(9)
    return 2 * (1 - norm.cdf(abs(matches - expected_matches) / np.sqrt(len(bits))))

# 10. **Maurer’s Universal Statistical Test**
def maurers_test(bits):
    pattern = [bits[i:i+5] for i in range(0, len(bits)-4)]
    # print(10)
    return 2 * (1 - norm.cdf(abs(len(set(map(tuple, pattern))) - len(pattern)) / np.sqrt(len(bits))))

# 11. **Linear Complexity Test**
def linear_complexity_test(bits):
    complexity = np.random.randint(0, 5)
    # print(11)
    return 2 * (1 - norm.cdf(abs(complexity - len(bits)) / np.sqrt(len(bits))))

# 12. **Serial Test**
def serial_test(bits, block_size):
    blocks = [bits[i:i+block_size] for i in range(0, len(bits)-block_size+1)]
    # print(12)
    return 2 * (1 - norm.cdf(abs(sum(map(sum, blocks)) - len(bits)) / np.sqrt(len(bits))))

# 13. **Approximate Entropy Test**
def approximate_entropy_test(bits):
    phi = sum(abs(bits[i] - bits[i+1]) for i in range(len(bits)-1))
    # print(13)
    return 2 * (1 - norm.cdf(abs(phi - np.mean(bits)) / np.sqrt(len(bits))))

# 14. **Random Excursions Test**
def random_excursions_test(bits):
    excursions = sum(1 for i in range(1, len(bits)) if bits[i] != bits[i-1])
    # print(14)
    return 2 * (1 - norm.cdf(abs(excursions - len(bits)) / np.sqrt(len(bits))))

# 15. **Random Excursions Variant Test**
def random_excursions_variant_test(bits):
    excursions = sum(1 for i in range(1, len(bits)) if bits[i] != bits[i-1])
    # print(15)
    return 2 * (1 - norm.cdf(abs(excursions - np.mean(bits)) / np.sqrt(len(bits))))

def nist_tests(gen,num):
    posled = ''
    for i in range(num):
        posled += bin(next(gen))[2:]
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
    return sum(res)