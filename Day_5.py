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
password = ""
for _ in range(0,nr_letters):
  i = random.randint(0,len(letters)-1)
  password += letters[i]
for _ in range(0,nr_symbols):
  i = random.randint(0,len(symbols)-1)
  password += symbols[i]
for _ in range(0,nr_numbers):
  i = random.randint(0,len(numbers)-1)
  password += numbers[i]
print(password)
  


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
new_password = ""
letter_len = 0
number_len = 0
symbol_len = 0
list = [letters,numbers,symbols]
for _ in range(nr_letters+nr_numbers+nr_symbols):
  choice  = random.choice(list)
  if choice == letters:
      i = random.randint(0,len(letters)-1)
      new_password += letters[i]
      letter_len += 1
      if letter_len == nr_letters:
        list.remove(letters)
  elif choice == numbers:
      i = random.randint(0,len(numbers)-1)
      new_password += numbers[i]
      number_len += 1
      if number_len == nr_numbers:
        list.remove(numbers)
  else:
      i = random.randint(0,len(symbols)-1)
      new_password += symbols[i]
      symbol_len += 1
      if symbol_len == nr_symbols:
        list.remove(symbols)
print(new_password)

#Method 2
password_list = []
for _ in range(0,nr_letters):
  password_list.append(random.choice(letters))
for _ in range(0,nr_symbols):
  password_list.append(random.choice(symbols))
for _ in range(0,nr_numbers):
  password_list.append(random.choice(numbers))
new_pass = ""
random.shuffle(password_list)
for char in password_list:
  new_pass += char
print(new_pass)
