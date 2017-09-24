import string
import os
from getkey import getKey

def shifted_alphabet(shift):
    shifted = string.ascii_lowercase[shift:] +string.ascii_lowercase[:shift]
    return shifted

def decode(plain_text, shift):
    e_alpha=shifted_alphabet(shift) 
    encoded_text = ""
    trans_table = "".maketrans(string.ascii_lowercase, e_alpha) 
    return plain_text.translate(trans_table)

def brute_force(plain_text):
    for i in range(0,26):
        print(decode(plain_text, i))
    input("\n Press any key.") 

def menu():
    global plain_text
    selected_menu=98
    menu = {}
    menu['1']="Enter text" 
    menu['2']="Fixed shift"
    menu['3']="Brute force"
    menu['4']="Exit"
    while True: 
      os.system('clear') 
      options=sorted(menu.keys()) 
      print('{:*^40}'.format('ROT Decoder'),"\n\n") 
      print("Input text: ",plain_text,"\n\n") 
      for entry in options: 
          #print(entry, int(entry) ==selected_menu) 
          print("*"*(int(entry)==selected_menu)," "*(int(entry)!=selected_menu), entry, menu[entry])

      #selection=input("\nPlease Select: ") 
      selection=getKey() 
      if selection =='1': 
          plain_text = None
          while plain_text is None:
              plain_text = input("\nEnter message to encode: ").strip() 
      elif selection == '2': 
          print(decode(plain_text, 1)) 
          input() 
      elif selection == '3':
          brute_force(plain_text) 
      elif selection == '4': 
          break
      
plain_text ="abcdef"
menu() 