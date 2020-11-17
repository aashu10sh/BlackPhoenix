import random
import termcolor
import optparse

class Encryptor:

  def __init__(self, password):
    self.password = password
    

  def file(self, filename):
    passw = self.passw
    f = open(filename)
    for lines in f:
        a = password + lines


  def word (self, word):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    enc = ""
    passw = self.password
    
    for w in word:
      aword = ord(w) + random.choice(nums)
      aword = chr(aword)
      enc += aword
    print(enc)
      
class Decryptor:

  def __init__(self, password)
    self.password = password
    
  def word (self, enc):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    passw = self.password
    for k in enc:
      dword = ord(k) - random.choice(nums)
      dword = chr(dword)
    print(dword)

    

def encrypt():
  message = str(input("Enter Your Message to Encrypt \n >> "))
  password = input("Enter the password for the message to be decrypted \n >> ")
  inst = Encrypt(password)


a = Encryptor("test")
a.word("Samrat")

def  
#/The Message below is a help message for the program/#
helpc = '''--h or "help" for help
-e or "encrypt" for encryption
-d or "decrypt" for decryption
"clear" for clear
"exit" or "CTRL + C" for close
-f for file 
-w for words
'''
while True:
  usr_input = str(input("[Black Pheonix]#"))
  firsts = usr_input[:7]
  seconds = usr_input[7:9]
