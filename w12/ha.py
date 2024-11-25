# Half Adder
def half_adder(a, b):
    return a ^ b, a & b

# Full Adder
def full_adder(a, b, carry_in):
    sum1, carry1 = half_adder(a, b)
    sum2, carry2 = half_adder(sum1, carry_in)
    carry_out = carry1 | carry2
    return sum2, carry_out

# Example: Half Adder
print("Half Adder (1, 0):", half_adder(1, 0))


print("Full Adder (1, 1, 0):", full_adder(1, 1, 0))
