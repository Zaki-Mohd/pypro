
a = 15
b = 10

if a > b:
    max = a
else:
    max = b


g = 1


for i in range(1, max + 1):
    if a % i == 0 and b % i == 0:
        g = i

print("GCD:", g)

L = (a * b) // g
print("LCM:", L)
