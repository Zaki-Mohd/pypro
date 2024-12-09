def reverse_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        print(line.strip()[::-1])

# Example Usage
reverse_lines(r'w8\sample.txt')
