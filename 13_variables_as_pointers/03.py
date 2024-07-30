dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

# Will print 'The Life of Brian'. dict2 is a shallow copy of dict1.
# Reassigning the value for the key 'Monty Python' in dict2 does not effect dict1
# as they are separate objects.
