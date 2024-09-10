def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# a=int(input("Enter A:"))
# b=int(input("Enter B:"))

print(f"The GCD of and is ",gcd(20,30))
