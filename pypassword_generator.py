import random

print("Welcome to the PyPassword Generator!")

# Taking user input for password composition
l = int(input("How many letters would you like in your password?: "))
s = int(input("How many symbols would you like in your password?: "))
n = int(input("How many numbers would you like in your password?: "))

# Defining character sets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Randomly selecting characters
random_letters = random.choices(letters, k=l)
random_symbols = random.choices(symbols, k=s)
random_numbers = random.choices(numbers, k=n)

# Combining selected characters
password_generator = random_letters + random_symbols + random_numbers

# Shuffling to ensure randomness
random.shuffle(password_generator)

# Converting list to string
password = ''.join(map(str, password_generator))

# Displaying the generated password
print("Generated password is:", password)
