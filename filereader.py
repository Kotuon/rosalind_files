
import os
import sys


def getFile():
    directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(directory)

    fileName = input("Enter file name: ")

    return open(directory + "\\" + fileName, "r")
