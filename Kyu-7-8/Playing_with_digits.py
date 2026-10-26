# Dados dos números enteros positivos n y p, queremos encontrar un número entero positivo k,
# si existe, tal que la suma de los dígitos de n elevados a potencias consecutivas a partir 
# de p sea igual a k * n.

def dig_pow(n, p):
    result = -1
    suma = 0
    numero = [int(digito) for digito in str(n)]
    for i in range (len(numero)):
            suma += (numero[i])**(p + i)
    if suma % n == 0:
        result = suma // n
    return result

print(dig_pow(695, 2))