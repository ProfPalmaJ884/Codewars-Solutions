def sum_strings(x, y):
    X = len(x)
    Y = len(y)
    if X == Y == 0:
        return '0'
    elif X == 0:
        return y
    elif Y == 0:
        return x
    elif X > Y:
        y = y.zfill(X)
        long = X
    elif X < Y:
        x = x.zfill(Y)
        long = Y
    else:
        long = X
    num1 = [int(char) for char in x ]
    num2 = [int(char) for char in y ]
    num1 = num1[::-1]
    num2 = num2[::-1]
    carry = 0
    result = []
    for i in range (long):
        aux = (num1[i] + num2[i] + carry) % 10
        carry = (num1[i] + num2[i] + carry) // 10
        result.append(str(aux))
    if carry == 1:
        result.append(str(carry))
    respuesta = "".join(result[::-1]).lstrip('0')
    return respuesta if respuesta != "" else "0"

print(sum_strings("00012355", "99"))
