import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#set blank string as start then iterate through list until user inputs reach 0
password = ''
while nr_letters > 0:
    rletters = random.choice(letters)
    password = password + rletters
    nr_letters -= 1
while nr_symbols > 0:
    rsymbols = random.choice(symbols)
    password = password + rsymbols
    nr_symbols -= 1
while nr_numbers > 0:
    rnumbers = random.choice(numbers)
    password = password + rnumbers
    nr_numbers -= 1

# Easy version of password
print(password)
#Randomize the order of the password by first converting to string
list_of_pw = list(password)
random.shuffle(list_of_pw)
randompassword = "".join(list_of_pw)
print(randompassword)