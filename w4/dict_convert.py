
def invert(dictq):
    inverted= {v : k for k,v in dictq.items()}
    return inverted
data={
    1:'Akhil',2:'Sai',3:'Rohith'
}
print("Original Data:\n",data)
print("Inverted Data:")
print(invert(data))



# def invert_dictionary(input_dict):
#     inverted_dict = {value: key for key, value in input_dict.items()}
#     return inverted_dict

# def get_dictionary_from_user():
#     input_dict = {}
#     num_entries = int(input("Enter the number of dictionary entries: "))
#     for i in range(num_entries):
#         key = input(f"Enter key {i + 1}: ")
#         value = input(f"Enter value {i + 1}: ")
#         input_dict[key] = value
#     return input_dict

# # Get dictionary values from the user
# user_dictionary = get_dictionary_from_user()
# print("Original Dictionary:", user_dictionary)

# # Invert the dictionary
# inverted_dictionary = invert_dictionary(user_dictionary)
# print("Inverted Dictionary:", inverted_dictionary)