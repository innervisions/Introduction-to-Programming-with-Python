stuff = ('hello', 'world', 'bye', 'now')

values = list(stuff)
values[2] = 'goodbye'
stuff = tuple(values)
# stuff = stuff[0:2] + ('goodbye', stuff[3])

print(stuff)
