my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

name_lengths = { name: len(name)
                 for name in my_set
                 if len(name) % 2 != 0 }
print(name_lengths)
