def square_digits(num):
    result = []
    if not isinstance(num, int):
        return 'You must enter a number'
    else:
        aux = list(str(num))
        for numero in aux:
            result.append(str(int(numero) ** 2))
        return int("".join(result))   

print(square_digits(222))