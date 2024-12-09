from collections import Counter

def most_frequent_word(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        word_counts = Counter(words)
        most_common = word_counts.most_common(1)
        if most_common:
            print("Most frequent word:", most_common[0][0], "\nOccurrences:", most_common[0][1])
        else:
            print("No words found.")

# Example Usage
most_frequent_word(r'w8\test.txt')
