def is_valid_IP(strng):
    aux = strng.split('.')
    if len(aux) != 4:
        return False
    for num in aux:
        if not (num.isdigit()):
            return False
        if len(num) > 1 and num[0] == "0":
            return False
        if int(num) < 0 or int(num) > 255:
            return False
    return True
            


print(is_valid_IP("123.456.78.90"))