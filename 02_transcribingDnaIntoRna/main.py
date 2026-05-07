
fileName = input("Enter file name: ")

file = open(fileName, "r")
fileData = file.read()

print(fileData)
result = fileData.replace("T", "U")

print(result)
