#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# rnd_ind = random.randrange(len(nr_letters))
# rnd_letter = letters[rnd_ind]
rnd_letters = []
combined_random_list = []
for n in range(0, nr_letters):  
    rnd_letter = random.choice(letters)
    rnd_letters.append(rnd_letter)
    combined_random_list.append(rnd_letter)
sym = []
for n in range(0, nr_symbols):  
    symbol = random.choice(symbols)
    sym.append(symbol)
    combined_random_list.append(symbol)
numb = []
for n in range(0, nr_numbers):  
    numbr = random.choice(numbers)
    numb.append(numbr)
    combined_random_list.append(numbr)

# print(f'random letters {rnd_letters}\n')
# print(f'random symbols {sym}\n')
# print(f'random numbers {numb}\n')
# print(f'combined random numbers {combined_random_list}\n')

total = nr_letters + nr_symbols + nr_numbers
print(total)
# combined_random_list = [rnd_letters, sym, numb]

# for n in range(0, total+1):

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pwd_str = ''
for n in range(0, total):
    indx = random.randrange(len(combined_random_list))
    pwd = str(combined_random_list[indx])
    pwd_str += pwd
print(f'Here is your password is {pwd_str}')
