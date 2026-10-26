#Usando el metodo tradicional de matematicas
def to_Hexa (n):
    hexa = {0: '0',1:  '1',2:  '2',3:  '3',4:  '4',5:  '5',6:  '6',7:  '7',8:  '8',9:  '9',10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = []
    cociente = n
    resto = 0
    while True:
        resto = cociente % 16
        cociente = cociente // 16   
        if (cociente < 16):
            result.append(hexa[resto])
            result.append(hexa[cociente])
            break
        elif (cociente < 10):
            result.append(hexa[resto])
        else:
            result.append(hexa[resto])
    aux1 = "".join(result)
    result = aux1[::-1]
    return result

def rgb(r, g, b):
    aux = [r,g,b]
    result = [0,0,0]
    for i in range (3):
        if aux[i] > 255:
            result[i] = to_Hexa(255)
        elif aux[i] < 0:
            result[i] = to_Hexa(0)
        else:
            result[i] = to_Hexa(aux[i])
    return "".join(result)
            
#print(f' 255, 255, 255 : {rgb(255, 255, 255)}')
#print(f' 255, 255, 300 : {rgb(255, 255, 300)}')
#print(f' 0, 0, 0 : {rgb(0, 0, 0)}')
#print(f' 148, 0, 211 : {rgb(148, 0, 211)}')

#Usando los metodos y funciones de Python:
def To_Hexa(n):
    numero = max(0,min(255,n))
    return f'{numero:02X}'

def RGB(r, g, b):
    return "".join(map(To_Hexa, [r,g,b]))

print(f' 255, 255, 255 : {RGB(255, 255, 255)}')
print(f' 255, 255, 300 : {RGB(255, 255, 300)}')
print(f' 0, 0, 0 : {RGB(0, 0, 0)}')
print(f' 148, 0, 211 : {RGB(148, 0, 211)}')