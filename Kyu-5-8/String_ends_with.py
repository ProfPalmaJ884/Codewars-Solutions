# Inputs: "abc", "bc"
# Output: true

# Inputs: "abc", "d"
# Output: false

def solution(text, ending):
    if text.endswith(ending):
        return True
    else:
        return False

print(solution("abc", "bc"))
print(solution("abc", "d"))