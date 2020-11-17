import platform
print(platform.system())


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
      aword = ord(w) + 0
      aword = chr(aword)
      enc += aword
    print(enc)
      
class Decryptor:

    def __init__(self, password):
        self.password = password
    
    def word (self, enc):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        passw = self.password
        for k in enc:
            dword = ord(k) - 0
            dword = chr(dword)
        print(dword)

    

def construct(ctype, tail, passw, passvalue):
    cond = True
    if ctype == "encrypt":
        enc = Encryptor(passw)
    elif ctype == 'decrypt':
        enc = Decryptor(passw)
    else:
        cond = False
    if (cond):
        if tail == '-w':
            enc.word(passvalue)
        elif tail == '-f':
            enc.file(passvalue)
    else:
        print("Invalid Command")

        




a = Encryptor("test")
a.word("Samrat")
 
#The Message below is a help message for the program
helpc = '''
######################################
##  --h or "help" for help          ##
##  -e or "encrypt" for encryption  ##
##  -d or "decrypt" for decryption  ##
##  "clear" for clear               ##
##  "exit" or "CTRL + C" for close  ##
##  -f for file                     ##
##  -w for words                    ##
######################################
'''
while True:
    usr_input = input("[Black Pheonix]# ")
    firsts = usr_input[:7]
    seconds = usr_input[7:9]
    if usr_input[:4] == "help":
        print(helpc)
    elif usr_input[:4] == "exit":
        break
    elif usr_input[:7] in ["encrypt", "decrypt"]:
        passw = input("Enter the password : ")
        ctype = usr_input[:7]
        tail = usr_input[8:10]
        latt = usr_input[11:]
        construct("encrypt",tail, passw, latt)





  





