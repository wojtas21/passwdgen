import random

small_letters = "abcdefghijklmnopqrstuwxyz"
big_letters = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()"

length = int(input("Type password length you want: "))

all = small_letters+big_letters+numbers+symbols

password = "".join(random.choice(all) for i in range(length))

where = input("For what is this password: ")
print(password)

with open("password.txt", "w") as file:
  file.write(f"Password is for: {where}\n")
  file.write(password)

print("Write your password on paper!!!")