
import os
import sys


def getFile(fileName):
    directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    # print(directory)

    return open(directory + "\\" + fileName, "r")
