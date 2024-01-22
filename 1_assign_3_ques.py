'''3 Write a Python program to check the validity of password input by users.
Validation:
(i) At least 1 letter between [a-z] and 1 letter between [A-Z].
(ii) At least 1 number between [0-9].
(iii) At least 1 character from [$#@].
(iv) Minimum length 6 characters.
(v) Maximum length 16 characters.
'''

def validity(password):
    is_upper_case = any(p.isupper() for p in password)
    is_lower_case = any(p.islower() for p in password)
    number = any(p.isdigit() for p in password)
    symbol = any(p in '$#@' for p in password)
    length = 6<=len(password)<=16

    return is_upper_case and is_lower_case and number and symbol and length

def main():
    password = input('enter the password ')

    if(validity(password)):
        print(f'{password} is valid')
    else:
        print(f'{password} is invalid')

if __name__ == '__main__':
    main()