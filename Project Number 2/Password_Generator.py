#Muhammad Hammad
#mhammmad.503@gmail.com

#problem statement 
#generate a strong password based on user input.input length should be between 8 and 15

import random

class PasswordGenerator:
    def __init__(self, length=8):
        self.length = length
        self.lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        self.uppercase_letters = self.lowercase_letters.upper()
        self.digits = '0123456789'
        self.special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    def generate_password(self):
        password = ''
        while len(password) < self.length:
            choice = random.randint(1, 4)    
            if choice == 1:
                password += random.choice(self.lowercase_letters)
            elif choice == 2:
                password += random.choice(self.uppercase_letters)
            elif choice == 3:
                password += random.choice(self.digits)
            elif choice == 4:
                password += random.choice(self.special_characters)
        return password

if __name__ == "__main__":

     # Prompt the user for a password length within the specified range

    while True:
        try:
            length = int(input("Enter the length of the password (min 8, max 20): "))
     # Prompt the user for a password length within the specified range
       
            if length < 8 or length > 20:
                raise ValueError("Length should be between 8 and 20")
            break
        except ValueError as e:
            print(e)
     # Create an instance of the PasswordGenerator class
    generator = PasswordGenerator(length)
     # Generate the password
    password = generator.generate_password()
     # Print the generated password
    print("Generated Password:", password)
