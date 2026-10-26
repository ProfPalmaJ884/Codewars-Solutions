def move_zeros(lst):
    zero = 0
    count = 0
    while zero in lst:
        lst.remove(zero)
        count += 1
    for i in range(count):
        lst.append(zero)
    return lst

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))