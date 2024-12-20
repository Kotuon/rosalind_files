
import os
import sys
import operator


def hammingDistance(s, t):
    result = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            result += 1
    return result


def main():
    directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(directory)

    fileName = input("Enter file name: ")

    file = open(directory + "\\" + fileName, "r")

    line1 = file.readline().replace("\n", "")
    line2 = file.readline().replace("\n", "")

    output = sum(map(operator.ne, line1, line2))
    print(output)


main()
