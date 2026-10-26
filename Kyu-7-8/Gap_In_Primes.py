def primo(num):
    if num < 2: 
        return False
    if num == 2: 
        return True
    if num % 2 == 0: 
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def gap(g, m, n):
    gap = 0
    numeroPrimo = None
    for i in range(m, n + 1):
        if primo(i):
            if numeroPrimo != None and abs(i - numeroPrimo) == g:
                return [numeroPrimo, i]
            else:
                numeroPrimo = i
    return None
 
print(gap(2,100,103))

