import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password 

if __name__ == '__main__':
    try:
        password_length = int (input('Enter the desire password length'))
        if password_length <= 0: 
            print ('Please enter a valid password length')
        else:
            generated_password = generate_random_password(password_length)
            print(f'Your generated password is {generated_password}')
    except ValueError:
        print('Invalid input, please enter a valid integer for password length: ')