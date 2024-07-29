my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer_idx = 0
while outer_idx < len(my_list):
    inner_list = my_list[outer_idx]
    inner_idx = 0
    while inner_idx < len(inner_list):
        number = inner_list[inner_idx]
        if number % 2 == 0:
            print(number)
        inner_idx += 1
    outer_idx += 1
