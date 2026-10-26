# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    result = []
    sentence = text.split(" ")
    for word in sentence:
        if word.isalpha():
            aux = word[1:] + word[0] + 'ay'
            result.append(aux)
        else:
            result.append(word)
    return ' '.join(result)
        
print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !') )