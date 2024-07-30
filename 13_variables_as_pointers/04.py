dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# Will print [1, 42, 3]
# dict2 is a shallow copy of dict1. While they are different objects in memory,
# their keys reference the same objects unless / until one is reassigned.
# Mutating one of those objects is reflected when it is accessed using either variable.
