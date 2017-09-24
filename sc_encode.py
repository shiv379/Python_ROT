import string

def shifted_alphabet(shift):
    shifted = string.ascii_lowercase[shift:] +string.ascii_lowercase[:shift]
    return shifted

def decode(plain_text, shift):
    e_alpha=shifted_alphabet(shift) 
    encoded_text = ""
    trans_table = "".maketrans(string.ascii_lowercase + string.ascii_uppercase, e_alpha+e_alpha.upper()) 
    return plain_text.translate(trans_table)

def brute_force(plain_text):
    for i in range(0,26):
        print(i, decode(plain_text, i))
    input() 