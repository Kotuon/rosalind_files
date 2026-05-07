
countArray = [0] * 4
def parseInput(fileStr) :
    countArray[0] = fileStr.count("A")
    countArray[1] = fileStr.count("C")
    countArray[2] = fileStr.count("G")
    countArray[3] = fileStr.count("T")

file_name = input("Enter file name: ")
print(file_name)

file = open(file_name, "r")
fileData = file.read()

parseInput(fileData)

print(str(countArray[0]) + " " + str(countArray[1]) + " " + str(countArray[2]) + " " + str(countArray[3]))
