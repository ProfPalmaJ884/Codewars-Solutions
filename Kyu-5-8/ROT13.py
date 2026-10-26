abecedario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 
              'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 
              'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
              'z': 26}
ABECEDARIO = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
              10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q',
              18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
              26: 'z'}

def rot13(message):
    sentence = message.split(' ')
    result = []
    for i in range(len(sentence)):
            aux = list(sentence[i])
            word = []
            for char in aux:
                if char.isalpha():
                    mayuscula = char.isupper() 
                    char = char.lower()
                    indice = abecedario[char] + 13
                    if indice <= 26:
                        char = ABECEDARIO[indice]
                    else:
                        char = ABECEDARIO[indice - 26]
                    if mayuscula:
                         word.append(char.upper())
                    else: 
                         word.append(char)
                else:
                    word.append(char)
            aux1 = ''.join(word)
            result.append(aux1)

    return ' '.join(result)

print(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"))
        
