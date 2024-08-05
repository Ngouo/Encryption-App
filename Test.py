import os
import base64
from tkinter import messagebox 
from tkinter import *


def decrypt():
  password = code.get()
  
  if password == '1234':
    screen2 = Toplevel(screen)
    screen2.title("Encryptage")
    screen2.geometry("400x200")
    screen2.configure(bg="#00bd56")
    
    message = text1.get(1.0, END)
    decode_message = message.encode("utf-8")
    base64_bytes = base64.b64decode(decode_message)
    decrypt = base64_bytes.decode("utf-8")
    
    
    Label(screen2, text='DECRYPTER', font='Arial', fg="white", bg='#00bd56').place(x=10, y=0)
    text2 = Text(screen2, font="Rpbote 10", bg='white', relief=GROOVE, wrap=WORD, bd=0)
    text2.place(x=10, y=40, width=380, height=150)
    
    text2.insert(END, decrypt)
    
  
  elif password == '':
    messagebox.showerror("ENCRYPTION", 'Insérer un mot de passe')
    
  elif password != "1234":
    messagebox.showerror('ENCRYPTION', 'mot de passe incorrect !')  

  
def encrypt():
  password = code.get()
  
  if password == '1234':
    screen1 = Toplevel(screen)
    screen1.title("Encryptage")
    screen1.geometry("400x200")
    screen1.configure(bg="#ed3833")
    
    message = text1.get(1.0, END)
    encode_message = message.encode("utf-8")
    base64_bytes = base64.b64encode(encode_message)
    encrypt = base64_bytes.decode("utf-8")
    
    
    Label(screen1, text='ENCRYPTER', font='Arial', fg="white", bg='#ed3833').place(x=10, y=0)
    text2 = Text(screen1, font="Rpbote 10", bg='white', relief=GROOVE, wrap=WORD, bd=0)
    text2.place(x=10, y=40, width=380, height=150)
    
    text2.insert(END, encrypt)
    
  
  elif password == '':
    messagebox.showerror("ENCRYPTION", 'Insérer un mot de passe')
    
  elif password != "1234":
    messagebox.showerror('ENCRYPTION', 'mot de passe incorrect !')  





#1ere fonction
def main_screen():
  
#On rend nos variables globales pour qu'elles soient accessible dans les deux autres fonctions  
  global screen
  global code
  global text1
  
  
  screen = Tk()
  screen.geometry('375x398+430+150')
  screen.title('AppEncodage')
  
  
  
  def reset():
    code.set("")
    text1.delete(1.0, END)
  
  #indication 
  Label(text="Entrer le texte pour cryptage ou décryptage", fg="black", font=("Calibri", 13)).place(x=10,y=10)
  
  #zone de saisie du texte que l'on veut en/décrypter
  text1 = Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
  text1.place(x=10, y=50, width=355, height=100)
  
  #Zone de saisie du mdp
  Label(text="Entrer le mot de passe", fg='black', font=("Calibri", 13)).place(x=10,y=170)
  
  code = StringVar()
  Entry(textvariable=code, width=19, bd=0, font=("Arial", 25), show='*').place(x=10, y=200)
  
  #Les 02 Boutons encrypter et decrypter
  Button(text="ENCRYPTER", height='2', width=23, bg='#ed3833', bd=1, command=encrypt).place(x=10, y=250)   #Encrypter
  Button(text="DECRYPTER", height='2', width=23, bg='#00bd56', bd=1, command=decrypt).place(x=200, y=250)   #Decrypter
  
  #Le Bouton Reset
  Button(text="RESET", height='2', width=50, bg="#1089ff", fg='white',bd=1, command=reset).place(x=10, y=300)
  
  
  
  screen.mainloop()
main_screen()