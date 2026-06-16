import random
import string

print("=" * 35)
print("      PASSWORD GENERATOR")
print("=" * 35)

length = int(input("Enter password length: "))

print("\nSelect Password Type:")
print("1. Letters Only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    characters = string.ascii_letters

elif choice == "2":
    characters = string.ascii_letters + string.digits

elif choice == "3":
    characters = string.ascii_letters + string.digits + string.punctuation

else:
    print("Invalid Choice!")
    exit()

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)

print("\nPassword Length:", len(password))