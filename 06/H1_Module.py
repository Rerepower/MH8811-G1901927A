import random
def genPassword(n):
    uppercase = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lowercase = ('abcdefghijklmnopqrstuvwxyz')
    number = ('0123456789')
    special = ('~!@#$%^&*()_+}{|:,.<>?')
    sample_sets = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+}{|:,.<>?')
    i = -1
    password = ''
    if n < 4:
        print('Your password has to be at least 4 digits')
    elif n >= 4:
        while i < n - 1:
            i = i + 1
            if i == 0:
                password += random.choice(uppercase)
            if i == 1:
                password += random.choice(lowercase)
            if i == 2:
                password += random.choice(number)
            if i == 3:
                password += random.choice(special)
            elif i >= 4:
                password += random.choice(sample_sets)
        else:
            l = list(password)
            random.shuffle(l)
            password = ''.join(l)
            print('Your password is ' + password)
if __name__ == '__main__':
    genPassword(12)