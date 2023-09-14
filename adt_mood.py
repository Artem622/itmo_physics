import matplotlib.pyplot as plt
import math
import scipy

data = sorted(
    [715, 1050, 829, 853, 1014, 872, 886, 861, 852, 787, 857, 838, 810, 839, 808, 821, 833, 868, 847, 899, 843,
     839, 835, 826, 827, 814, 816, 819, 816, 776, 781, 773, 789, 777, 782, 795, 797, 801, 765, 796, 862, 869, 825, 796,
     809, 739, 743, 872, 811, 789, 801, 752, 784, 787, 820, 843, 892, 948, 923, 931, 895, 894, 852, 835, 861, 841, 862,
     873, 980, 888, 939, 908, 959, 874, 776, 791, 890, 855, 904, 898, 894, 901, 904, 891, 948, 888, 928, 1012,
     837, 800, 843, 864, 854, 810, 784, 835, 844, 912, 810, 844, 892, 780, 797, 827, 799, 801, 843, 819, 780, 859, 841,
     827, 806, 868, 863, 803, 779, 787, 853, 798, 813, 833, 654, 727, 823, 827, 854, 868, 846, 817, 849]
)
data = list(map(lambda point: point / 1000, data))


def tN(points):
    return sum(points) / len(points)


pointsBest = [tN(data)] * (len(data) - 1)
pointsBest.append(data[1])


def qN(points):
    return math.sqrt(
        sum(list(map(lambda point: (point - tN(points)) ** 2, points))) / (len(points) - 1)
    )


def qMax(points):
    return 1 / (qN(points) * math.sqrt(2 * math.pi))


def p(points):
    return list(
        map(lambda point: (qMax(points) * math.exp(-((point - tN(points)) ** 2) / (2 * qN(points) ** 2))), points)
    )


middleLine = [i for i in range(0, int(qMax(data)) + 1)]

fig, ax = plt.subplots()

ax.plot(data, p(data), linewidth=2.0)
ax.plot([tN(data)] * (int(qMax(data)) + 1), middleLine, linestyle="dashed")
ax.hist(data, int(math.sqrt(len(data))),  color="black")
print("", qN(data))
print(qMax(data))
print(len(data))
plt.show()

points = data
def calculate(point):
    return (qMax(points) * math.exp(-((point - tN(points)) ** 2) / (2 * qN(points) ** 2)))

scipy.integrate.quad()
