import random
parol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
p = int(input("выберите длину пароя(в цифрах)"))
password = ""
for i in range(p):
    password += random.choice(parol)
print(password)
