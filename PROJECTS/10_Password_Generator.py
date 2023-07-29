# Password generator
import random

keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
num = ['0','1','2','3','4','5', '6', '7', '8', '9']
len = random.randint(8, 17)
password = ""
for i in range(0, len):
    password += random.choice(keys)
count = 0
if password.isalnum():
    for char in password:
        if char in symbols:
            count += 1
        

any_no = random.choice(0,10)

if count == 0:
    password.replace(password[2], any_no)
else:
    pass


    
print(f"Password: {password} of length: {len}")


