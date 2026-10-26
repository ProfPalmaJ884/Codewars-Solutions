# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
# which is the number of times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
# 4 --> 0 (because 4 is already a one-digit number, there is no multiplication)

def persistence(n):
    count = 0
    #Convertimos el numero a una lista de digitos
    aux = [int(x) for x in str(n)]
    #Verificamos si hay mas de un digito y en el caso de que si comenzamos a iterar sobre la lista de digitos
    while len(aux) > 1:
        #Inicializamos la varible que almacenara los productos. Inicia en 1 que es el elemento neutro de la multiplicaion
        result = 1
        #Recorremos la lista multiplicando cada elemento por el siguiente
        for digito in aux:
            result *= digito
        #Concluido el recorrido actualizamos la lista del numero original al resultado obtenido de ir multiplicando cada digito
        aux = [int(x) for x in str(result)]
        #Aumentamos el contador, con cada ciclo de multiplicacion completado
        count += 1
    #Una vez se cumpla la condicion de retorna el valor del contador que solicita la funcion
    return count

print(persistence(999))

# aux = 1234567890
# aux1 = [int(x) for x in str(aux)]
# print(len(aux1))