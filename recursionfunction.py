def addchain(number, increment):
    if number <= 0:
        return 0
    else:
        return number + addchain(number-increment, increment)
print(addchain(100,1))