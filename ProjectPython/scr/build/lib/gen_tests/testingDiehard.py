import numpy as np
from scipy.stats import chisquare, norm

# 1. Birthday Spacings
def birthday_spacings(samples, n, m):
    gaps = np.diff(np.sort(samples[:n]))[:m]
    counts, _ = np.histogram(gaps, bins=m)
    return chisquare(counts).pvalue

# 2. Overlapping Permutations
def overlapping_permutations(samples, k):
    seqs = [tuple(samples[i:i+k]) for i in range(len(samples) - k + 1)]
    counts = np.unique(seqs, axis=0, return_counts=True)[1]
    return chisquare(counts).pvalue

# 3. Ranks of Matrices
def ranks_of_matrices(samples, rows, cols):
    matrices = np.array(samples[:rows * cols]).reshape(-1, rows, cols)
    ranks = [np.linalg.matrix_rank(m) for m in matrices]
    unique, counts = np.unique(ranks, return_counts=True)
    return chisquare(counts).pvalue

# 4. Overlapping Quadruples (Monkey Test)
def overlapping_quadruples(samples):
    quadruples = [tuple(samples[i:i+4]) for i in range(len(samples) - 3)]
    counts = np.unique(quadruples, axis=0, return_counts=True)[1]
    return chisquare(counts).pvalue

# 5. Count the 1s
def count_the_1s(samples):
    bit_counts = [bin(x).count('1') for x in samples]
    counts, _ = np.histogram(bit_counts, bins=range(max(bit_counts)+2))
    return chisquare(counts).pvalue

# 6. Parking Lot Test
def parking_lot_test(samples, n, size):
    points = np.array(samples[:n]).reshape(-1, 2) * size
    occupied = [np.linalg.norm(p1 - p2) > 1 for i, p1 in enumerate(points) for p2 in points[i+1:]]
    return np.mean(occupied)

# 7. Minimum Distance Test
def minimum_distance_test(samples, n):
    points = np.array(samples[:n]).reshape(-1, 2)
    min_dists = [np.min(np.linalg.norm(points[i] - points[:i], axis=1)) for i in range(1, len(points))]
    return chisquare(min_dists).pvalue

# 8. Random Spheres
def random_spheres(samples, n):
    radii = samples[:n]
    counts = [np.sum(samples[i:i+n]) < r for i, r in enumerate(radii)]
    return chisquare(counts).pvalue

# 9. Squeeze Test
def squeeze_test(samples):
    x = 1.0
    for s in samples:
        x *= s
    return x

# 10. Overlapping Sums
def overlapping_sums(samples, k):
    sums = [np.sum(samples[i:i+k]) for i in range(len(samples) - k + 1)]
    return chisquare(sums).pvalue

# 11. Runs Test
def runs_test(samples):
    runs = np.diff(samples > 0.5).astype(int)
    counts, _ = np.histogram(runs, bins=2)
    return chisquare(counts).pvalue

# 12. Craps Test
def craps_test(samples, n):
    wins = 0
    for i in range(n):
        roll = samples[i:i+2]
        wins += roll[0] + roll[1] in [7, 11]
    return wins / n


def diehard_tests(gen,num):
    posled = []
    for i in range(num):
        posled.append(next(gen))
    res = []
    res.append(birthday_spacings(posled,500,50))
    res.append(overlapping_permutations(posled,4))
    # res.append(ranks_of_matrices(posled,15,10))
    res.append(overlapping_quadruples(posled))
    res.append(count_the_1s(posled))
    res.append(parking_lot_test(posled,100,10))
    res.append(minimum_distance_test(posled,100))
    # res.append(random_spheres(posled,100))
    # res.append(squeeze_test(posled))
    res.append(overlapping_sums(posled,10))
    # # res.append(runs_test(posled))
    res.append(craps_test(posled,100))
    return sum(res)