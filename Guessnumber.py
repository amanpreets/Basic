import random as rand
# numberOfTries variable defines how many times user can enter.
numberOfTries: int = 5
# answer generated by the random library of python.
answer = rand.randint(1, 10)

print('''Welcome to Guess The Number. You have 5 attempts to guess the number!
Guess a number from 1 to 10''')
# Checks if the input by the user is valid or not. User should only enter numeric input between 1 to 10
def validinput(userinput):
    if not userinput.isnumeric():
        return False
    elif int(userinput) > 10 or int(userinput) < 0:
        return False
    else:
        return True

for x in range(0,numberOfTries):
    numberoftriesleft = numberOfTries - x
#    print("You have " + str(numberoftriesleft) + " number of tries left.")
    print("You have {} number of tries left.".format(str(numberoftriesleft)))
    youranswer: str = input('what is your answer\n')
    isvalid = validinput(youranswer)
    if isvalid:
        youranswer = int(youranswer)
        if youranswer < answer:
            print('go higher and try again')

        elif youranswer > answer:
            print('go lower and try again')
        else:
            print("you got it. good job")
            break
    else:
        print("your answer is out of  range . please enter between 1 to 10")