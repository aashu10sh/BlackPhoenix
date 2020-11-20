#Importing platform module for finding out the os they are using
import platform
import random #Importing random for getting random numbers
from os import system as terminal #Importing this module to run system commands
from termcolor import colored

#Creating a Object called Encryptor which encrypts 
class Encryptor:

    #As all the instance needs password taking it while initializing it
    def __init__(self, password):
        self.password = password
    
    #Creating a instance which encrypts a file
    def file(self, filename):
        passw = self.password #Acessing password from init
        f = open(filename) #Opening the file which name is given by the user
        for lines in f:
            a = password + lines

    #Creating another instance which encrypts words
    def word (self, word):
        #Generating random six digit code
        passw = self.password
        enc = "" #Creating a variable for final word
        finpass = ""
        #Looping for every letter in the word
        for w in word:
            i = 0
            aword = ord(w) + ord(passw[i % len(passw)])
            #Changing it into its ascii code and adding a rando number
            aword = chr(aword) #Changing back to normal character
            enc += aword #Adding all the letters to final enc
            i += 1
        return enc

#Creating another object for decrypting
class Decryptor:
    #Initializing and taking the password value
    def __init__(self, password):
        self.password = password
    
    #Creating a instance for the word
    def word (self, enc):
        passw = self.password #Getting the password from init
        final = ""
        #Looping for every word given by the user
        for k in enc:
            i = 0
            dword = ord(k) - ord(passw[i % len(passw)])
            #Converting into ASCII and subtracting what was added while encrypinng
            dword = chr(dword) #Converting back into character
            i += 1
            final += dword
        return final

    
#Creating a constructor function which constructs the object from user input
def construct(ctype, tail, passvalue):
    cond = True #Creating a variable called cond and setting it to true
    usr_hash = input("Enter the password >> ")
    if ctype == "encrypt": #Encrypting if the user types encrypt
        enc = Encryptor(usr_hash)
    elif ctype == 'decrypt': #Decryping if the user types decrypt
        enc = Decryptor(usr_hash)
    else: # If the arguement is wrong setting cond to false
        cond = False
    if (cond): #Setting condition for files and words
        if tail == '-w':
            finword = enc.word(passvalue)
            print(finword)
        elif tail == '-f':
            enc.file(passvalue)
        else: 
            print("Invalid Command")#Priniting Invalid if the command does not exist

        
 
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
    usr_input = input(colored("[Black Pheonix]# ",'red')) #Printing it to look like a console
    firsts = usr_input[:7] #Taking first seven character from user input
    seconds = usr_input[7:9] #Taking 8-9 letter from user input
    if usr_input[:4] == "help": #If users type help printing the help string
        print(colored(helpc, 'green'))
    elif usr_input[:4] == "exit":
    	print(colored("Bye See You Again :)",'red'))
    	exit()#If user types exit, breaking the loop
    
    elif usr_input == "clear":
        if (platform.system() == "Windows"):
            terminal("cls")
        else:
            terminal("clear")
    elif usr_input[:7] in ["encrypt", "decrypt"]: #Checking if the user input is in the list or not
        ctype = usr_input[:7]#Filtering the type of command into ctype
        tail = usr_input[8:10] #Taking the tail of command(file or word)
        latt = usr_input[11:] #Taking the file name or word
        construct(ctype,tail, latt) #Passing it all to construct function
    else:
        terminal(usr_input)





  





