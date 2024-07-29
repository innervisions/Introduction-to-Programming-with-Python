my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

def odd_or_even(number):
    if number %2 == 0:
        return 'Even'
    return 'Odd'

new_list = [odd_or_even(number) for number in my_list]
print(new_list)
