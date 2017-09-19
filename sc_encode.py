def plain_alphabet():
    return "abcdefghijklmnopqrstuvwxyz" 

def encoded_alphabet():
    return "nopqrstuvwxyzabcdefghijklm" 
    
plain_text = None
encoded_text = "" 
while plain_text is None:
    plain_text = input("Enter message to encode: ")
print(plain_text,"¦")
p_alpha=plain_alphabet() 
e_alpha=encoded_alphabet() 
for index in range(len(plain_text)):
    plain_alphabet_index = p_alpha.upper().find(plain_text[index].upper())
    if plain_text[index].isupper():
        encoded_text += e_alpha[plain_alphabet_index].upper()
    else:
        encoded_text += e_alpha[plain_alphabet_index].lower() 
print("Encoded text: " + encoded_text)