
import numpy as np
import sys
sys.path.append('../rosalind_files')

import filereader  # nopep8


def mortalRabbits(n, m):
    table = np.zeros([n, m], dtype=np.int64)
    table[0][0] = 1

    for month in range(1, n):
        table[month][0] = np.sum(table[month - 1, 1:])
        for age in range(1, m):
            table[month][age] = table[month - 1][age - 1]

    return np.sum(table[n-1])


def main():
    fileName = input("Enter file name: ")

    file = filereader.getFile(fileName)
    fileData = file.read().replace("\n", "")

    n, m = map(int, fileData.split(' '))

    print("n = " + str(n) + ", m = " + str(m))

    result = mortalRabbits(n, m)
    print(result)


main()
