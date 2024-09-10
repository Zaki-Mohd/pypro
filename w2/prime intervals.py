def prime(number):
    if number<=1:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True
def interval(start,end):
    print(f"These are the prime numbers between {start} & {end}: ")
    for i in range(start,end + 1):
        if prime(i):
            print(i)
            
a=int(input("Enter your starting interval: "))
b=int(input("Enter your ending interval: "))
interval(a,b)
