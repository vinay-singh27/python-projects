x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Can't divide by Zero!")
finally:
    print('All Done!')