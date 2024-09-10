import matplotlib.pyplot as plt
import numpy as np

# a = 10
# print(a)

# for i in range(1, 8, 2):
#     print(i)
#
# a= [1, 5, 10, 8]
# length = len(a)
# for i in range(length):
#     print(a[i], end=" ")

# a = np.random.rand(3, 5)
# print(a)

a = np.random.randint(1, 5, size=(3, 6))
# print(a)

meanOfEveryCol = np.mean(a, axis=0)
# print(meanOfEveryCol)

meanOfSpecificCol = np.mean(a, axis=0)[3]
# print(meanOfSpecificCol)

meanOfSpecificRow = np.mean(a, axis=1)[1]
# print(meanOfSpecificRow)

a = np.zeros((2, 3), dtype=int)
# print(a)

# a = np.ones((2, 3), dtype=int)

a = np.ones(3, dtype=int)
# print(a)

# x = [1, 2, 3]
# y = [2, 4, 6]
# plt.plot(x, y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
# plt.show()

# x = [0, np.pi / 2, np.pi, 3 / 2 * np.pi, 2 * np.pi]
# y = np.sin(x)
# plt.plot(x, y)
# plt.show()
# print(y)


x = np.linspace(0, np.pi * 2, 100)
y = np.sin(x)


# plt.plot(x, y)
# plt.show()


def har(n):
    c = []
    for i in range(1, n + 1):
        term = 1 / i
        c.append(term)
    return c


# print(har(4))

def harMean(n):
    firstNTerms = har(n)
    sumOfNTerms = np.sum(firstNTerms)

    mean = n/sumOfNTerms
    return mean

print(harMean(4))
