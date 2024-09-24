def cumulative_product(numbers):
    result = []
    product = 1
    for num in numbers:
        product *= num
        result.append(product)
    return result

# Test the function
numbers = [1, 2, 3, 4, 5]
result = cumulative_product(numbers)
print(f"Input list: {numbers}")
print(f"Cumulative product: {result}")