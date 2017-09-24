import os
import sc_encode
from getkey import getKey

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
            print("\n", sc_encode.decode(plain_text, shift)) 
            getKey() 
        elif selection == '3': #Brute force
            os.system('clear') 
            sc_encode.brute_force(plain_text) 
        elif selection == '4': #File out
            print("Not implemented yet\nPress any key") 
            getKey() 
        elif selection == '9': #Exit
            os.system('clear') 
            break
      
plain_text = None
menu() 