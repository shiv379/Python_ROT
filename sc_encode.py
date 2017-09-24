import string
import os
from getkey import getKey

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

def menu():
    global plain_text
    while True:
        menu = {}
        menu['1']="Enter text" 
        menu['9']="Exit"
        if plain_text is not None:
            menu['2']="Fixed shift"
            menu['3']="Brute force"
            menu['4']="Output to file: OFF" 
        os.system('clear') 
        options=sorted(menu.keys()) 
        print('{:*^40}'.format('ROT Decoder'),"\n\n") 
        print("Input text: ",plain_text,"\n\n") 
        for entry in options: 
            print(entry, menu[entry])
        print("") 
        selection=getKey() 
        if selection not in options:
            print() 
        elif selection =='1': #Enter text
            plain_text = None
            while plain_text is None:
                plain_text = input("\nEnter message to encode: ").strip() 
        elif selection == '2': #Fixed shift
            shift = None
            while not isinstance(shift, int):
                try:
                    shift=int(input("Shift: "))
                except ValueError:
                    print("Please enter a valid whole number.") 
            print("\n", decode(plain_text, shift)) 
            getKey() 
        elif selection == '3': #Brute force
            brute_force(plain_text) 
        elif selection == '4': #File out
            print("Not implemented yet\nPress any key") 
            getKey() 
        elif selection == '9': #Exit
            break
      
plain_text = None
menu() 