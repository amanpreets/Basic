text = "hello Jaskaran\n"

saveFile = open("exampleFile.txt","w")
saveFile.write(text)

for x in range(1,11):
    saveFile.write(text)

saveFile.close()

readFile = open("Guessnumber.py", "r")
print("aman")
content = readFile.read()
print(content)


