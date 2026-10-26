def wave(people):
    result = []
    if people == "":
        return result
    else:
        for i in range(len(people)):
            if people[i] == " ":
                continue
            else:
                sentence  = people[:i] + people[i].upper() + people[i+1:]
                result.append(sentence)
        return result

print(wave(" s p a c e s "))