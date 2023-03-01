from random import randint
import random
import string

amount = []
checker = 1
password = ""
while checker <= 127:
    amount.append(checker)
    checker += 1


while True:
    numberOfChar = input("What length do you want the password (up to 127)? ")
    try:
        int(numberOfChar)
    except:
        print("Please type an integer from 1-127 in number form. ", end="")
        continue

    if (int(numberOfChar)>=1 and int(numberOfChar)<=127):
        break
    else:
        print("Please type a number from 1-127 in number form. ", end="")
        
            

def check(data):
    if data in ("Y", "y"):
        return True
    if data in ("N", "n"):
        return False
    
    data = input("Please type Y or N. ")
    return check(data)

print("")
print("It will now ask you to enter which of the 4 types of characters you want. If you say no to first 3, you are stuck with the 4th.")
print("")
    
upperCase = input("Do you want uppercase letters? Y/N: ")
upperCase = check(upperCase)

lowerCase = input("Do you want lowercase letters? Y/N: ")
lowerCase = check(lowerCase)

symbols = input("Do you want symbols? Y/N: ")
symbols = check(symbols)

if (symbols == True) or (lowerCase==True) or (upperCase==True):
    numbers = input("Do you want numbers? Y/N: ")
    numbers = check(numbers)
else:
    print("You said no to everything else, you have to have numbers!!")
    print("")
    numbers = True


randNeeded = 0
inputter = [upperCase, lowerCase, symbols, numbers]

for i in range(4):
    if inputter[i] == True:
        randNeeded += 1
        if i == 0:
            upperCase = randNeeded-1
        elif i==1:
            lowerCase = randNeeded-1
        elif i==2:
            symbols = randNeeded-1
        elif i==3:
            numbers = randNeeded-1
    else:
        if i == 0:
            upperCase = 5
        elif i==1:
            lowerCase = 5
        elif i==2:
            symbols = 5
        elif i==3:
            numbers = 5


randomNumbers = [0]*randNeeded

for i in range(int(numberOfChar)):
    randomNumbers[randint(0,randNeeded-1)] +=1

char = string.punctuation
print(randomNumbers)
if upperCase in (0,1):
    for x in range(randomNumbers[upperCase]):
        password += chr(random.randint(65,90))

if lowerCase in (0,1):
    for x in range(randomNumbers[lowerCase]):
        password += chr(random.randint(97,122))

if symbols in (0,1,2):
    for x in range(randomNumbers[symbols]):
        password += random.choice(char)

if numbers in (0,1,2,3):
    for x in range(randomNumbers[numbers]):
        password += chr(random.randint(48,57))

print(password)
passList = list(password)
random.shuffle(passList)
password = "".join(passList)
print("Your randomly generated password with " + numberOfChar + " digits is: " + password)




