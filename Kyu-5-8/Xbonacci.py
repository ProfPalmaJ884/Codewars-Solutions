# Tienes que construir una función Xbonacci que tome una firma de X elementos (y recuerda que cada elemento siguiente es la suma 
# de los últimos X elementos) y devuelva los primeros n elementos de la secuencia inicializada.

def Xbonacci(signature, n):
    if n == 0:
        result = []
    else:
        result = signature[:]
        for i in range (n):
            aux = result[i] + result [i + 1] + result [i + 2]
            result.append(aux)
    return result[:n]

print(Xbonacci([0,0,1], 10))