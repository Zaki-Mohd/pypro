def file_analysis(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = len(content.split())
        vowels = sum(1 for char in content if char.lower() in 'aeiou')
        spaces = content.count(' ')
        lowercase = sum(1 for char in content if char.islower())
        uppercase = sum(1 for char in content if char.isupper())
    print(f"Words: {words}, Vowels: {vowels}, Spaces: {spaces}, Lowercase: {lowercase}, Uppercase: {uppercase}")

# Example Usage
file_analysis(r'w8\test.txt')
