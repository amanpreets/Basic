readFile = open("words.txt", "r")
content = readFile.readlines()
writeFile = open("exampleFile.txt", "w")
print(content)
listofwords = []
for line in content:
    strippedline =line.strip()
    if(len(strippedline) == 5) :
        listofwords.append(strippedline)
        print(strippedline)
        writeLine = strippedline + "\n"
        writeFile.write(writeLine)

writeFile.close()
