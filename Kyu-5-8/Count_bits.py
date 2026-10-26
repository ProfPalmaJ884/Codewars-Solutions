def to_binary(n):
    aux = n
    result = []
    while True:
         result.append(aux % 2)
         aux = aux // 2
         if aux < 2 and aux // 2 == 0:
            result.append(aux % 2)
            break
    aux1 = (str(x) for x in result)
    aux1 = "".join(aux1)
    result = aux1[::-1]
    return result

def count_bits(n):
    # la funcion bin() devuelve un string con la representacion binaria de un int con el prefijo "0b"
    binary = bin(n)
    # Se recorta el prefijo 0b y queda el string del numero binario del int
    binary = binary[2:]
    count = 0
    for i in range (len(binary)):
        if binary[i] == "1":
            count += 1
    return count

print(count_bits(1234))