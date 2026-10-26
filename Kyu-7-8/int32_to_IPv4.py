def int32_to_ip(int32):
    result = []
    binario = bin(int32)
    binario = binario[2:].zfill(32)
    for i in range(0,len(binario) - 7,8):
        aux = binario[i:i + 8]
        result.append(int(aux, 2))
    
    return ".".join(str(n) for n in result)


print(int32_to_ip(0))