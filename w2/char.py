char=input("Enter Your Desired Character: ")
if char.isdigit():
    print("Your entererd a number")
elif char.islower():
    print("Your character is a lowercase letter")

elif char.isupper():
    print("Your character is a uppercase letter")
else:
    print("You entered a special character")
