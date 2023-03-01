from random import randint
import random

amount = []
checker = 0
password = ""
while checker <= 127:
    amount.append(checker)
    checker += 1


while True:
    numberOfChar = input("What length do you want the password (up to 127)? ")
    try:
        int(numberOfChar)
    except:
        print("Please type an integer from 0-127 in number form. ", end="")
        continue

    if (int(numberOfChar)>=0 and int(numberOfChar)<=127):
        break
    else:
        print("Please type a number from 0-127 in number form. ", end="")
        
            

def check(data):
    if data in ("Y", "y"):
        return True
    if data in ("N", "n"):
        return False
    
    data = input("Please type Y or N. ")
    return check(data)
    
upperCase = input("Do you want uppercase letters? Y/N: ")
upperCase = check(upperCase)

lowerCase = input("Do you want lowercase letters? Y/N: ")
lowerCase = check(lowerCase)

symbols = input("Do you want symbols? Y/N: ")
symbols = check(symbols)

numbers = input("Do you want numbers? Y/N: ")
numbers = check(numbers)



randNeeded = 0
inputter = [up, low, sym, num]

for i in range(4):
    if inputter[i] == True:
        randNeeded += 1
            

randNumbers = [0]*randNeeded


    for i in range(numChar):
        randNumbers[randint(0,randNeeded-1)] +=1


upperCase, lowerCase, symbols, numbers, int(numberOfCha

print(randomNumbers)
if upperCase == True:
    for x in range(randomNumbers[0]):
        password += chr(random.randint(65,90))

if lowerCase == True:
    for x in range(randomNumbers[1]):
        password += chr(random.randint(97,122))

if symbols == True:
    for x in range(randomNumbers[2]):
        password += chr(random.randint(33,47))

if numbers == True:
    for x in range(randomNumbers[3]):
        password += chr(random.randint(48,57))

print(password)
passList = list(password)
random.shuffle(passList)
password = "".join(passList)
print(password)




