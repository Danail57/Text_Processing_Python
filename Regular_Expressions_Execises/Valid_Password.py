import re

username = input('Enter your username: ')
password = input('Enter your password: ')
special_symbols = "!@#$=^&()-_"

valid = True

if not (12 <= len(password) <= 24):
    print("The password must be between 12 and 24 characters long.")
    valid = False

if not any(c.isupper() for c in password):
    print("Password must contain at least one uppercase letter.")
    valid = False

if not any(c.islower() for c in password):
    print("Password must contain at least one lowercase letter.")
    valid = False

if not any(c in special_symbols for c in password):
    print(f"The password must contain at least one of these symbols: {special_symbols}")
    valid = False

if " " in password:
    print("Spaces are not allowed in the password.")
    valid = False

if re.search(r"(.)\1\1+", password):
    print("Password must not contain the same character repeated more than twice in a row.")
    valid = False

if username.lower() in password.lower():
    print("Password must not contain the username.")
    valid = False

if valid:
    print("Password is valid!")
