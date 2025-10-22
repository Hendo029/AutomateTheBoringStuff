import re

while True:
    password = input('Input your strong password> ')
    
    # Use 3 regexes
    # password must be 8 characters long
    passwordLength = re.compile(r'(.{8,})')
    if passwordLength.search(password) == None:
        print('Password should be 8 characters long.')
        continue

    # Must contain both upper and lowercase characters
    passwordUpper = re.compile(r'[A-Z]')
    passwordLower = re.compile(r'[a-z]')
    if passwordUpper.search(password) == None or passwordLower.search(password) == None:
        print('Password must contain both an upper and lower case character.')
        continue

    # Have at least 1 digit
    passwordDigit = re.compile(r'\d+')
    if passwordDigit.search(password) == None:
        print('Password must contain at least one digit')
        continue
    
    print('Your password is Strong.')
    break