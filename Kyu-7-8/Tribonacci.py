def tribonacci(signature, n):
    if n == 0:
        result = []
    else:
        result = signature[:]
        for i in range (n):
            aux = result[i] + result [i + 1] + result [i + 2]
            result.append(aux)
    return result[:n]

print(tribonacci([0,0,1], 10))