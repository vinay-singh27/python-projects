'''
The collections module is a built-in module that implements specialized container data types providing 
alternatives to Python’s general purpose built-in containers. 
We've already gone over the basics: dict, list, set, and tuple.
'''

'''
1. Counter - is a *dict* subclass which helps count hashable objects
'''
from collections import Counter

lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
print(Counter(lst))

#split a sentence into words
s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()
print(Counter(words))


'''
2. default dict - A defaultdict will never raise a KeyError. 
Any key that does not exist gets the value returned by the default factory
'''
from collections import defaultdict
d = defaultdict(lambda: 0)
print(d['one'])


'''
3. named Tuple - A namedtuple assigns names, as well as the numerical index, to each member. 
'''
from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])

sam = Dog(age=2,breed='Lab',name='Sammy')
frank = Dog(age=2,breed='Shepard',name="Frankie")

print(sam.age, sam.name)
print(frank.breed)

