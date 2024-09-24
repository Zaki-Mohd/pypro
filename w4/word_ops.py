def replace_first_letter(sentence):
    result = ''
    new_word = True  # Flag to identify the start of a new word

    for char in sentence:
        if char.isalpha():
            if new_word:
                result += char.upper()
                new_word = False
            else:
                result += char.lower()
        else:
            result += char
            new_word = True  # Set flag for the next word

    return result

# Example usage:
input_sentence = "hello world!"
result = replace_first_letter(input_sentence)
print("Result:", result)