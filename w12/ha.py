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


# # Half Adder
# def half_adder(a, b):
#     return a ^ b, a & b

# # Full Adder
# def full_adder(a, b, carry_in):
#     sum1, carry1 = half_adder(a, b)
#     sum2, carry2 = half_adder(sum1, carry_in)
#     carry_out = carry1 | carry2
#     return sum2, carry_out

# # Parallel Adder
# def parallel_adder(A, B):
#     n = len(A)
#     result = []
#     carry = 0
#     for i in range(n - 1, -1, -1):
#         sum_bit, carry = full_adder(A[i], B[i], carry)
#         result.insert(0, sum_bit)
#     result.insert(0, carry)
#     return result

# # Example: Half Adder
# print("Half Adder (1, 0):", half_adder(1, 0))

# # Example: Full Adder
# print("Full Adder (1, 1, 0):", full_adder(1, 1, 0))

# # Example: Parallel Adder
# A = [1, 0, 1, 1]  # Binary number 1011
# B = [1, 1, 1, 0]  # Binary number 1110
# print("Parallel Adder ([1011], [1110]):", parallel_adder(A, B))

# # Output:
# # Half Adder (1, 0): (1, 0)
# # Full Adder (1, 1, 0): (0, 1)
# # Parallel Adder ([1011], [1110]): [1, 1, 0, 0, 1]
