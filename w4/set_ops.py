A={1,2,3,5,8}
B={4,5,6,3,2}

uni=A.union(B)
inte=A.intersection(B)
diff=A.symmetric_difference(B)

print(uni)
print(inte)
print(diff)
print("_____________________")
print(A | B)
print(A & B)
print(A - B)
print(A ^ B)