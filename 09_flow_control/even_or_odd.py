# def even_or_odd(number):
#     if number % 2:
#         print('odd')
#     else:
#         print('even')

def even_or_odd(number):
    print('even' if number % 2 == 0 else 'odd')

value = int(input('Enter a number: '))
even_or_odd(value)
