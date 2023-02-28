amount = []
checker = 0
while checker <= 127:
    amount.append(checker)
    checker += 1


while True:
    numberOfChar = input("What length do you want the password (up to 127)? ")
    if int(numberOfChar) in amount:
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


print(upperCase)
print(lowerCase)
print(symbols)
print(numbers)
