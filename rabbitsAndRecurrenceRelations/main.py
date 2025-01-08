
import os
import sys


def fibonacci(x, growth):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fibonacci(x - 1, growth) + growth*(fibonacci(x - 2, growth))


def main():
    directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(directory)

    fileName = input("Enter file name: ")

    file = open(directory + "\\" + fileName, "r")
    fileData = file.read()

    nkValues = fileData.split(' ')

    n = int(nkValues[0])
    k = int(nkValues[1])

    print("n = " + str(n) + ", k = " + str(k))

    result = fibonacci(n, k)
    print(result)


main()
