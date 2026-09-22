#ths is loop whichi is autopassword

import random
import time
import string

random_chars = string.ascii_letters + string.digits

while True:
    random_part = ""

    name = input("Enter your name: ")
    age = input("Your age: ")

    for i in range(10):
        random_part += random.choice(random_chars)

    password = name + age + "@"  + "whisgatys" + random_part

    print("Generating your password...")
    time.sleep(4)

    print("Your generated password is: " + password)

    again = input("Do you want to try again? (yes/no): ")

    if again == "no":
        print("Thank you for using the password generator!")
        break

    elif again == "yes":
        print("Generating a new password...")
        time.sleep(2)

    else:
        print("Please enter yes or no.")