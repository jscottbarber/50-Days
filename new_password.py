from cmath import isnan
import string
import random

def password_generator():
  a = string.ascii_letters + string.digits + string.punctuation
  password1 = []
  valid_pass = False
  while not valid_pass:
    length = input("Provide your desired password length (5-16): ")

    if length.isnumeric():
      length = int(length)
      if length >= 5 and length <= 16:
        valid_pass = True

    if not valid_pass:
      print("\nInvalid selection, please try again...\n")

  invalid_password_chars = ["0","O","1","l","'","`"," ","\\"]
  for i in range(length):
    valid_char = False
    while not valid_char:
      password = str(random.choice(a))
      if password not in invalid_password_chars:
        valid_char = True
      else:
        print(f"Bad character found '{password}', trying again...")
    password1.append(password)
  return 'Your password is', ''.join(password1)

print(password_generator())