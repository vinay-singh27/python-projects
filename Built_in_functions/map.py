'''
map() is a built-in Python function that takes in two or more arguments: a function and one or more iterables, in the form:
    map(function, iterable, ...)
map() returns an *iterator* - that is, map() returns a special object that yields one result at a time as needed.
'''

def fahrenheit(celsius):
    return (9/5)*celsius + 32
    
temps = [0, 22.5, 40, 100]

print(list(map(lambda x: (9/5)*x + 32, temps)))