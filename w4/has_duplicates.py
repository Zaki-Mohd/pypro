def has_duplicates(string):
    return len(set(string)) != len(string)
data=[1,2,65,2]
print(has_duplicates(data))