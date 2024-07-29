age = int(input('How old are you? '))
print(f'You are {age} years old.')
for year in range(10, 50, 10):
    print(f'In {year} years, you will be {age + year} years old.')
