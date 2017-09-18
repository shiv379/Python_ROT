plain_text = None
encoded_text = "" 
while plain_text is None:
    plain_text = input("Enter message to encode: ")
print(plain_text,"¦")
plain_alphabet="abcdefghijklmnopqrstuvwxyz"
encoded_alphabet="nopqrstuvwxyzabcdefghijklm"
for index in range(len(plain_text)):
    plain_alphabet_index = plain_alphabet.upper().find(plain_text[index].upper())
    if plain_text[index].isupper():
        encoded_text += encoded_alphabet[plain_alphabet_index].upper()
    else:
        encoded_text += encoded_alphabet[plain_alphabet_index].lower() 
print("Encoded text: " + encoded_text)