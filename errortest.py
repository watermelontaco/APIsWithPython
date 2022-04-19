
try:
    x = 5
    y = x + 5
except TypeError:
    print("You must use an integer to do math")
else: 
    print(y)
finally:
    print("This code always runs")