def demo(a,b,c):
    if(c == 1):
        return a+b
    elif( c == 2):
        return a-b
    elif( c == 3):
        return a*b
    elif( c == 4):
        return a%b
    else:
        return a/b

print("List of Operations available: ")
print("""
1) Addition '+'
2) Subtraction '-'
3) Multiplication '*'
4) Remainder 
      """)
op=int(input("Enter Number of the Operation to be performed: "))
a=int(input("Enter A: "))
b=int(input("Enter B: "))
print(demo(a,b,op))