import random as rand


numberoftries = 3

print('Welcome to Guess the animal. You have 5 tries to guess the animal.')

allOptions = ("dog", "cat", "owl")

indexoption = rand.randint(0,len(allOptions) - 1)

answer = allOptions[indexoption]

indexanswer = rand.randint(0,len(answer) - 1)

characteranswer = answer[indexanswer]

option = answer.replace(characteranswer, "_")



def validinput(userinput):
    if userinput.isnumeric():
        return False
    else:
        return True



for x in range (0,numberoftries):
    numberoftriesleft = numberoftries - x
    print("You have {} number of tries left".format(str(numberoftriesleft)))
    print(option)
    youranswer: str = input("what is your answer\n")
    isvalid = validinput(youranswer)
    if isvalid:
        if youranswer.lower() != answer.lower():
            print("Wrong answer! Try again!")
        else:
            print("You got it! Good Job!")
            break
    else:
        print("Sorry! This answer is not valid! Try again!")
