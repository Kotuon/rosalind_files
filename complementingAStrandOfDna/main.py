
fileName = input("Enter file name: ")

file = open(fileName, "r")
fileData = file.read()

print(fileData)



complement = (fileData.replace('A', 't').replace('T', 'a')
              .replace('C', 'g').replace('G','c').upper()[::-1])

print(complement)
