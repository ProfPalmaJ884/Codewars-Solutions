romanos = {0: '', 1:'I', 2: 'II', 3: 'III', 4: 'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX',
           10:'X',20: 'XX', 30: 'XXX', 40:'XL', 50:'L', 60: 'LX', 70:'LXX', 80:'LXXX', 90:'XC',
           100:'C', 200: 'CC', 300: 'CCC', 400:'CD', 500:'D', 600: 'DC', 700: 'DCC', 800:'DCCC',
           900:'CM', 1000:'M' }

def solution(n, rom = romanos):
    result = []
    if n <= 99:
            unidad = n % 10
            decena = (n // 10 % 10)*10
            result.append(romanos[decena])
            result.append(romanos[unidad])
    elif n <= 999:
            unidad = n % 10
            decena = (n // 10 % 10)*10
            centena = (n // 100 % 10)*100
            result.append(romanos[centena])
            result.append(romanos[decena])
            result.append(romanos[unidad])
    elif n <= 3999:
            unidad = n % 10
            decena = (n // 10 % 10)*10
            centena = (n // 100 % 10)*100
            U_mil = (n // 1000 % 10)
            for i in range(U_mil):
                result.append(romanos[1000])
            result.append(romanos[centena])
            result.append(romanos[decena])
            result.append(romanos[unidad])
    return "".join(result)

print(solution(9))
