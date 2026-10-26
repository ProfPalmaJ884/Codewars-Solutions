# two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)
# two_sum([3, 2, 4], 6) # returns (1, 2) or (2, 1)

def two_sum(numbers, target):
    flag = False
    for i in range (len(numbers)):
        for j in range (len(numbers)):
            if i == j:
                continue
            elif numbers[i] + numbers[j] == target:
                result = (i , j)
                flag = True
                break
        if flag:
            break
    return result
    


print(two_sum([3, 2, 4], 6))
print(two_sum([1, 2, 3], 4))
print(two_sum([1234,5678,9012], 14690,))