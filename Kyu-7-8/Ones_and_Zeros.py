# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

def binary_array_to_number(arr):
    result = []
    for X in arr:
        result.append(str(X)) 
    result = "".join(result)
    return int(result, 2)

print(binary_array_to_number([0, 0, 0, 1]))