import string

def shifted_alphabet(shift):
    shifted = "" 
    for i in string.ascii_lowercase:
        shifted += string.ascii_lowercase[(string.ascii_lowercase.index(i) + shift) % 26]
    return shifted

def decode(plain_text, shift):
    e_alpha=shifted_alphabet(shift) 
    encoded_text = ""
    for c in plain_text:
        if c in string.ascii_lowercase:
            plain_alphabet_index = string.ascii_lowercase.find(c.lower())
            if c.isupper():
                encoded_text += e_alpha[plain_alphabet_index].upper()
            else:
                encoded_text += e_alpha[plain_alphabet_index].lower()
        else:
            encoded_text += c
    return encoded_text

def brute_force(plain_text):
    for i in range(0,26):
        print(decode(plain_text, i)) 

plain_text = None
while plain_text is None:
    plain_text = input("Enter message to encode: ").strip() 
#print(decode(plain_text, 1))
brute_force(plain_text) 