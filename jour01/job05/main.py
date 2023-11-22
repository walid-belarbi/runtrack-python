import string

def reversedAlphabet():
    alphabet_reverse = list(reversed(string.ascii_lowercase))
    return alphabet_reverse

print(reversedAlphabet())