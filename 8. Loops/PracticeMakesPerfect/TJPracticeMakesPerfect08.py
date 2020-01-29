def anti_vowel(text):
    r = ""
    vowels = "aeiouyAEIOUY"
    for char in text:
        if char not in vowels:
            r += char
    return r


print(anti_vowel("Hello book!"))  # H !
