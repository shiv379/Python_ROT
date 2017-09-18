plain_text = None
encoded_text = "" 
while plain_text is None:
    plain_text = input("Enter message to encode: ")
print(plain_text,"¦")
plain_alphabet="abcdefghijklmnopqrstuvwxyz"
encoded_alphabet="nopqrstuvwxyzabcdefghijklm"
for index in range(len(plain_text)):
    plain_alphabet_index = plain_alphabet.find(plain_text[index])
    encoded_text += encoded_alphabet[plain_alphabet_index]
print("Encoded text: " + encoded_text) 