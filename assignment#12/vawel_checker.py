string = input("inter any string: ")

def is_vowels(string):
    for char in string:
        if char in "aeiouAEIOU":
            print(char, "is a vowel")
        else:
            print(char, "is a consonant")
    
    return char

is_vowels(string)



ch = input("enter the Alphabet: ")

if ch in ("a","e","i","o","u"):
    print(ch, "is a vowel")

else:
    print(ch, "is a consonant")




alp = input("inter the alphabet: ")

alpha_lower = alp.lower()
vowels = "aeiou"
if alpha_lower in vowels:
    print(alp, "is a vowel")

else:
    print(alp, "is a consonant")



alp = input("inter the alphabet: ")

vowels = "aeiouAEIOU"
if alp in vowels:
    print(alp, "is a vowel")

else:
    print(alp, "is a consonant")
    
