import random
import string

ascii_pool = list(string.ascii_letters + string.digits + string.punctuation)
print(ascii_pool)

length = 10 #length of password

print("\n")
password = ""

for i in range(length):
   char = random.choice(ascii_pool)
   password += char


print("The password is: " + password)

