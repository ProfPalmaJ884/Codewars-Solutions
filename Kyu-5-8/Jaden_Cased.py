def Jaden_Cased (sentence):
    result = []
    if not isinstance(sentence, str):
        return 'The sentence must be a string'
    else:
        aux = sentence.split(" ")
        for word in aux:
            aux1 = word.capitalize()
            result.append(aux1)
        return " ".join(result)   


print(Jaden_Cased ("How can mirrors be real if our eyes aren't real"))   