letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['@','#','$','*','+','-']

print("welcome to password generator!")
nu_letters = int(input("how many number of letters would you like?\n"))
nu_numbers = int(input("how many numbers would you like?\n"))
nu_symbols = int(input("how many number of symbols would you like?\n"))

password_list = []
import random
for char in range(0,nu_letters):
    password_list.append( random.choice(letters))

for char in range(0,nu_symbols):
    password_list.append(random.choice(symbols))

for char in range(0,nu_numbers):
    password_list.append( random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)
    
password = ""
for char in password_list:
    password += char

print(f"your password is : {password}")
    