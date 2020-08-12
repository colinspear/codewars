# New methods learned: string.translate()
# str.translate() is a lot more powerful than demonstrated here. 
# It seems that typically a user will make their own translation
# table using `maketrans()` that specifies how to translate characters.

# My solution (5 minutes)

def disemvowel(string):
    vowels = [
        'a', 'e', 'i', 'o', 'u',
        'A', 'E', 'I', 'O', 'U'
    ]
    for v in vowels:
        string = string.replace(v, '')
    return string


# Top solution

def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
