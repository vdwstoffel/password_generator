import string
import random


class PasswordGenerator():

    def generate_password(self):

        password_list = []

        letters = [i for i in string.ascii_letters]
        digits = [i for i in string.digits]
        symbols = [i for i in string.punctuation]

        for _ in range(8):
            password_list.append(random.choice(letters))

        for _ in range(4):
            password_list.append(random.choice(digits))

        for _ in range(4):
            password_list.append(random.choice(symbols))

        random.shuffle(password_list)
        
        return "".join(password_list)
    
if __name__ == "__main__":

    a = PasswordGenerator()
    pw = a.generate_password()
    print(pw)