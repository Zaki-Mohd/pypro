def cmp(p, r, n):
    amount = p*(1+r/100)**n
    ci=amount-p
    print(f"Your Principal Amount is {p}.")
    print(f"Your Rate Of Interest is {r}.")
    print(f"Your Tenure Is {n}.")
    print("Compound Interest Is : ",ci)

p=int(input("Enter Principal Amount: "))
r=float(input("Enter Rate Of Interest: "))
n=int(input("Enter Tenure: "))

cmp(p, r, n)