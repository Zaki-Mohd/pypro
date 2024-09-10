def simp(p, t, r):
    interest=p*t*r/100
    print(interest)

p=int(input("Enter Your Principal amount: " ))
t=int(input("Enter Your Tenure: " ))
r=float(input("Enter Rate Of Interest: " ))

simp(p,t,r)
