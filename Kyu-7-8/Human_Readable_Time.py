# Write a function, which takes a non-negative integer (seconds) as 
# input and returns the time in a human-readable format (HH:MM:SS)
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

def make_readable(seconds):
    segundos = seconds % 60
    aux = seconds // 60
    horas = aux // 60
    minutos = aux % 60
    return(f'{horas:02d}:{minutos:02d}:{segundos:02d}')

print(make_readable(359999))