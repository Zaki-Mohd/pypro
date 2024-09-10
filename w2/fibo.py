n=int(input("Enter number for fibonacci values: "))
a=0
b=1
print(a,b,end=" ")
s=a+b
while s<=n:
    print(s,end=" ")
    a=b
    b=s
    s=a+b
      
