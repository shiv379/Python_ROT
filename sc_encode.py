import string

def plain_alphabet():
    return string.ascii_lowercase

def encoded_alphabet():
    return "nopqrstuvwxyzabcdefghijklm" 
    
def shifted_alphabet(shift):
    shifted = "" 
    for i in string.ascii_lowercase:
        shifted += string.ascii_lowercase[(string.ascii_lowercase.index(i) + shift) % 26]
    return shifted

plain_text = None
encoded_text = ""
while plain_text is None:
    plain_text = input("Enter message to encode: ").strip()
print(plain_text,"¦")
p_alpha=shifted_alphabet(0) 
e_alpha=shifted_alphabet(3) 
for index in range(len(plain_text)):
    plain_alphabet_index = p_alpha.upper().find(plain_text[index].upper())
    if plain_text[index].isupper():
        encoded_text += e_alpha[plain_alphabet_index].upper()
    else:
        encoded_text += e_alpha[plain_alphabet_index].lower() 
print("Encoded text: " + encoded_text)