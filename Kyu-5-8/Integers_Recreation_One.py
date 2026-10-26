# Encontrar números en un rango [m, n] cuya suma de sus divisores al cuadrado sea un número cuadrado perfecto 

def divisores (num):
    dividers = []
    for i in range (1, int(num**0.5) + 1):
        if num % i == 0:
            dividers.append(i)
            aux = num // i
            if i != aux:
                dividers.append(aux)
    suma = 0
    for numero in dividers:
        suma += numero**2
    aux = suma ** 0.5
    if aux % 1 == 0:
        return [num, suma]
    return False

def list_squared(m, n):
    result = []
    for i in range(m,n):
        if divisores(i):
            result.append(divisores(i))
    return result


print(list_squared(1, 250))