'''
Use of try, except & finally for error handling
'''

def askint(a):
    try:
        val = int(a)
    except:
        print("Looks like you did not enter an integer!")
    else :
        return val + 5


a = input("Please enter an integer: ")
b = askint(a)
print(b)