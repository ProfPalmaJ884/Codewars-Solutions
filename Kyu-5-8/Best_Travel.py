import itertools

def choose_best_sum(t, k, ls):
    if k > len(ls):
        return None
    mejor_suma = None
    for combinacion in itertools.combinations(ls, k):
        suma_actual = sum(combinacion)
        if suma_actual <= t:
            if mejor_suma is None or suma_actual > mejor_suma:
                mejor_suma = suma_actual
    return mejor_suma

ts = [91, 74, 73, 85, 73, 81, 87]
print(choose_best_sum(230, 3, ts))