import random


print("Welcome stranger to my Password Generator")

characters = "0123456789yxcvbnmlkjhgfdsaqwertzuiopYXCVBNMLKJHGFDSAQWERTZUIOP?:_'/(%!=+*#&$@"	
password_lenght= input("Your passwords lenght")
password_lenght= int(password_lenght)
number_of_passwords= input("How many passwords do we want ?")
number_of_passwords=int(number_of_passwords)

print("Here we go")

for o in range(number_of_passwords):
    passwords = ""
    for k in range(password_lenght):
        passwords += random.choice(characters)
    print(passwords)

