import random

print("how to generate a strong password")

chars = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM~!@#$%^&*()_?/\|.:123456789"


number = int(input("how many password is generate : "))

length = int(input("length of the password : "))


print("it is your password : ")

for i in range(number):
    
     passwords = " "
     
     for c_choice in range(length):
        
         passwords += random.choice(chars)
    
print(passwords)
